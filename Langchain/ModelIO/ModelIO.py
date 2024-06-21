import os

from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from langchain_core.messages import SystemMessage, AIMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

memory = ConversationBufferMemory()

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "Bạn là một trợ lý ở giúp trả lời các câu hỏi. Nếu không biết hãy trả lời không biết đừng cố tạo ra câu trả lời."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
messages = chat_template.format_messages(text="Python là gì?")

llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response =  llm.invoke(messages)

new_prompt = (
    messages,
    AIMessage(content=response)
)
print(new_prompt)