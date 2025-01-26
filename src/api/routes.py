from fastapi import APIRouter
from src.api.schema import Hello, Lms
from src.api.logic import get_hello_message, post_lms_studio

router = APIRouter()

@router.get("/", response_model=Hello)
def hello_wrld():
    return get_hello_message()

@router.post("/llm", response_model=Lms)
def lm_studio(context: str, query: str):
    return post_lms_studio(context, query)