from api.ai.llms import get_open_ai_llm
from api.ai.schemas import EmailMessageSchema


def generate_email_message(query:str) -> EmailMessageSchema:
    llm_base = get_open_ai_llm()
    llm= llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response only plaintext.",
        ),
        ("human", f"{query}. Do not use markdown in your response only plaintext.")
    ]

    return llm.invoke(messages)

