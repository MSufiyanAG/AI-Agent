from fastapi import APIRouter, Depends, HTTPException
import sqlmodel 
from sqlmodel import Session, select

from typing import List
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session
from api.ai.agents import get_supervisor

from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message

from api.ai.schemas import SupervisorMessageSchema

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

# curl.exe -X POST -d "{\`"message\`": \`"Give me a summary why summer is better than winter\`"}" -H "Content-Type: application/json" https://ai-agent-production-470a.up.railway.app/api/chats/

# curl.exe -X POST -d "{\`"message\`": \`"Research why snow doesnt melt for days after snowfall and email me the results\`"}" -H "Content-Type: application/json" http://localhost:8080/api/chats/

# curl.exe -X POST -d "{\`"message\`": \`"Research why snow doesnt melt for days after snowfall and email me the results\`"}" -H "Content-Type: application/json" https://ai-agent-production-ff71.up.railway.app/api/chats/
@router.post("/", response_model = SupervisorMessageSchema)
def chat_create_message(
    payload:ChatMessagePayload,
    session:Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    #session.refresh(obj)

    sup = get_supervisor()
    msg_data = {
        "messages": [
            {"role" : "user",
             "content":f"{payload.message}"},
        ]
    }
    results = sup.invoke(msg_data)

    if not results:
        raise HTTPException(status_code = 400, detail="Error with supervisor")
    messages = results.get("messages")
    if not messages:
        raise HTTPException(status_code = 400, detail="Error with supervisor")
    
    return messages[-1]