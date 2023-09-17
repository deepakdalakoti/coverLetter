from fastapi import FastAPI, UploadFile, File
from llm import LLM
import uvicorn
from prompts import LLamaPrompt
from parsers import Parser
from typing import Annotated
import io


app = FastAPI(debug=True)
doc_parser = Parser()


@app.on_event("startup")
async def load_models():
    LLM(model_name="databricks/dolly-v2-3b", engine="openai", device_map="cpu")


@app.get("/ping")
async def ping():
    return "pong"


@app.get("/generate")
async def generate(cv, jd):
    output = LLM().generate_output(cv, jd)
    return output


@app.post("/generate_file")
async def generate_file(cv: UploadFile, jd: str):
    content = await cv.read()
    with open("cv.pdf", "wb") as f:
        f.write(content)
    text = doc_parser.parse("cv.pdf", "cv.pdf")

    output = LLM().generate_output(text, jd)
    return output


if __name__ == "__main__":
    uvicorn.run(app)
