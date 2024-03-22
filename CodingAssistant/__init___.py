from fastapi import FastAPI

app = FastAPI(title="Deploying my own CodingAssistant with FastAPI on Huggingface")

from TextGen import router