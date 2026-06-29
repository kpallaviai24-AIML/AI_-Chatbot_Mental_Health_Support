
from fastapi import APIRouter
from pydantic import BaseModel

from services.ai_service import generate_ai_response
from services.safety_service import is_dangerous

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/ask")
def ask_question(data: Question):

    if is_dangerous(data.question):
        return {
            "error": "Emergency or harmful medical queries require a licensed doctor."
        }

    response = generate_ai_response(data.question)

    return {
        "response": response
    }
