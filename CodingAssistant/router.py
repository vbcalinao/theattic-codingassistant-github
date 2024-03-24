from pydantic import BaseModel

from .env_config import config
from fastapi.middleware.cors import CORSMiddleware

from langchain.llms import Clarifai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from CodingAssistant import app

class Generate(BaseModel):
    text:str

def generate_text(prompt: str):
    if prompt == "":
        return {"detail": "Please provide a prompt."}
    else:
        prompt = PromptTemplate(template=prompt, input_variables=['Prompt'])

        llm = Clarifai(
            pat = config.CLARIFAI_PAT,
            user_id = config.USER_ID,
            app_id = config.APP_ID, 
            model_id = config.MODEL_ID,
            model_version_id=config.MODEL_VERSION_ID,
        )

        llmchain = LLMChain(
            prompt=prompt,
            llm=llm
        )

        llm_response = llmchain.run({"Prompt": prompt})
        return Generate(text=llm_response)

        

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Home"])
def api_home():
    return {'detail': 'Welcome! This is your Coding Assistant. If you are in the Hugging Face interface, please go to the direct link, https://vbcalinao-theattic-clm-codingassistant.hf.space/docs and try out /api/generate!'}

@app.post("/api/generate", summary="Generate text from prompt", tags=["Generate"], response_model=Generate)
def inference(input_prompt: str):
    return generate_text(prompt=input_prompt)