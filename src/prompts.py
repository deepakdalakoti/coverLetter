class PromptText:
    SYSTEM_PROMPT = """Given a CV and job description, write a cover letter for the job. The cover letter should be rougly 300 words long.
      The cover letter should include all the relevant details of the candidate. 
      Fill the candidate name and other personal details from the CV where available. Also fill the company name if available in the job description. The cover should be written in a professional language"""
    USER_PROMPT = "The CV is \n{}\n. The job description is \n{}\n"


class LLamaPrompt:
    @staticmethod
    def generate_prompt(cv, jd):
        system = PromptText.SYSTEM_PROMPT.format(cv, jd)
        return "<s>[INST] <<SYS>>\n" + system + "\n[/INST]"
