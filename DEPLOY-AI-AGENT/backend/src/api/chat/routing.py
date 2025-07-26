from fastapi import APIRouter, Depends
import sqlmodel 
from sqlmodel import Session, select

from typing import List
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session

from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message

router = APIRouter()

@router.get("/")
def chat_health():
    return {"sttaus": "ok!"}


@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

# curl.exe -X POST -d "{\`"message\`": \`"hello World\`"}" -H "Content-Type: application/json" http://localhost:8080/api/chats/

# curl.exe -X POST -d "{\`"message\`": \`"Give me a summary why summer is better than winter\`"}" -H "Content-Type: application/json" http://localhost:8080/api/chats/


@router.post("/", response_model = EmailMessageSchema)
def chat_create_message(
    payload:ChatMessagePayload,
    session:Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    #session.refresh(obj)

    response = generate_email_message(payload.message)

    return response
