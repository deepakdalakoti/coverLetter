class PromptText:
    SYSTEM_PROMPT = """Given a CV and job description, write a cover letter for the job. The cover letter should be rougly 300 words long.
      The cover letter should include all the relevant details of the candidate. 
      Fill the candidate name and other personal details from the CV where available. Also fill the company name if available in the job description. The cover should be written in a professional language"""
    USER_PROMPT = "The CV is \n{}\n. The job description is \n{}\n"

    UPDATE_PROMPT = """You are given a CV of a candidate, a job description and a cover letter written for that
     job by the candidate. Your job is to improve the cover letter based on the comments from the user. 
      The CV is \n{}\n The job description is \n{}\n. The cover letter which needs to be improved is \n{}\n.
       Improve this cover letter based on user's inputs """


class LLamaPrompt:
    @staticmethod
    def generate_prompt(cv, jd):
        system = PromptText.SYSTEM_PROMPT.format(cv, jd)
        return "<s>[INST] <<SYS>>\n" + system + "\n[/INST]"
