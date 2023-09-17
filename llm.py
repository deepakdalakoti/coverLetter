from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import openai
import os
from prompts import PromptText, LLamaPrompt


class LLM:
    _instance = None

    def __new__(cls, model_name=None, engine="openai", **kwargs):
        if cls._instance is None:
            cls._instance = super(LLM, cls).__new__(cls)
            cls._instance.engine = engine
            if engine != "openai":
                cls._instance.load_models(model_name, **kwargs)

        return cls._instance

    def load_models(self, model_name, **kwargs) -> None:
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map=kwargs.get("device_map", "cuda"),
            torch_dtype=kwargs.get("torch_dtype", torch.bfloat16),
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def generate_output(self, cv, jd, **kwargs):
        print("HERE")
        if self.engine == "openai":
            return self.generate_output_openai(cv, jd, **kwargs)
        else:
            return self.generate_output_hf(cv, jd, **kwargs)

    def generate_output_openai(self, cv, jd, **kwargs):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        print("HERE")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": PromptText.SYSTEM_PROMPT},
                {"role": "user", "content": PromptText.USER_PROMPT.format(cv, jd)},
            ],
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_new_tokens", 1000),
            top_p=kwargs.get("top_p", 1.0),
            frequency_penalty=0,
            presence_penalty=0,
        )
        # print(response)
        return response["choices"][0]["message"]["content"]

    def generate_output_hf(self, cv, jd, **kwargs):
        prompt = LLamaPrompt.generate_prompt(cv, jd)
        tokens = self.tokenizer(prompt, add_special_tokens=False, return_tensors="pt")

        output = self.model.generate(
            input_ids=tokens["input_ids"],
            attention_mask=tokens["attention_mask"],
            do_sample=kwargs.get("do_sample", True),
            temperature=kwargs.get("temperature", 0.7),
            top_p=kwargs.get("top_p", 1.0),
            top_k=kwargs.get("top_k", 5),
            max_new_tokens=kwargs.get("max_new_tokens", 100),
        )

        output_text = self.tokenizer.batch_decode(output)
        return output_text[0]
