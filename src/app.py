from fastapi import FastAPI, UploadFile, File
from llm import LLM
import uvicorn
from prompts import LLamaPrompt
from parsers import Parser
from typing import Annotated
import io
from routers import router

app = FastAPI(debug=True)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app)
