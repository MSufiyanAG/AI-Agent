from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor


from api.ai.llms import get_open_ai_llm

from api.ai.tools import (
    send_me_email,
    get_unread_emails,
    research_email
)

EMAIL_TOOLS = {
    "send_me_email": send_me_email,
    "get_unread_emails": get_unread_emails,
}

EMAIL_TOOLS_LIST = list(EMAIL_TOOLS.values())

def get_email_agent():
    model = get_open_ai_llm()
    agent = create_react_agent(
        model=model,  
        tools=EMAIL_TOOLS_LIST,  
        prompt="You are a helpful agent for managing my email inbox for genrating, sending and reviewing mails",
        name = 'email_agent' 
    )
    return agent

def get_research_agent():
    model = get_open_ai_llm()
    agent = create_react_agent(
        model=model,  
        tools=[research_email],  
        prompt="You are a helpful research agent for preparaing email data.",
        name = 'research_agent' 
    )
    return agent

# from api.ai.agents import *
# sup = get_supervisor()
#  sup.invoke({"messages":[{"role":"user", "content":"Find out how to make butter chicken aand email me."}]})
def get_supervisor():
    llm = get_open_ai_llm()
    email_agent = get_email_agent()
    research_agent = get_research_agent()

    supe = create_supervisor(
        agents =[email_agent, research_agent],
        model=llm,
        prompt=(
            "You manage a research assistant and a"
            "email inbox manager assitant. Assign work to them."
            "Once content is ready email to the added email address immediately."
        )
    ).compile()
    return supe