from fastapi import APIRouter, Depends
import sqlmodel 
from sqlmodel import Session, select

from typing import List
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session

router = APIRouter()

@router.get("/")
def chat_health():
    return {"sttaus": "ok!"}


@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results

# curl -X POST -d '{"message": "hello World"}' -H "Content-Type: application/json" http://localhost:8080/api/chats/

@router.post("/", response_model = ChatMessage)
def chat_create_message(
    payload:ChatMessagePayload,
    session:Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj
