class PromptText:
    SYSTEM_PROMPT = "Given a CV and job description, write a cover letter for the job."
    USER_PROMPT = "The CV is \n{}\n. The job description is \n{}\n"


class LLamaPrompt:
    @staticmethod
    def generate_prompt(cv, jd):
        system = PromptText.SYSTEM_PROMPT.format(cv, jd)
        return "<s>[INST] <<SYS>>\n" + system + "\n[/INST]"
