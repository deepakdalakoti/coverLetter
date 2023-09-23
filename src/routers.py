from fastapi import APIRouter, UploadFile

from llm import LLM
from parsers import Parser

router = APIRouter()

# @app.on_event("startup")
# async def load_models():
#     LLM(model_name="databricks/dolly-v2-3b", engine="openai", device_map="cpu")


@router.get("/ping")
async def ping():
    return "pong"


@router.get("/generate")
async def generate(cv, jd):
    output = LLM().generate_output(cv, jd)
    return output


@router.post("/generate_file")
async def generate_file(cv: UploadFile, jd: str):
    content = await cv.read()
    with open("cv.pdf", "wb") as f:
        f.write(content)
    doc_parser = Parser()

    text = doc_parser.parse("cv.pdf", "cv.pdf")

    output = LLM().generate_output(text, jd)
    return output
