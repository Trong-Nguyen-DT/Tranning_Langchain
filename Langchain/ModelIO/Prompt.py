from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

prompt = SystemMessage(content="Bạn là một trợ lý ảo. Bạn có thể trả lời các câu hỏi của người dùng.")

new_prompt = (
    prompt + HumanMessage(content="Bạn là ai?") + AIMessage(content="Tôi là một trợ lý ảo?") + HumanMessage(content="{input}")
)
new_prompt.format_messages(input="Python là gì?")

print(new_prompt)

# chain = LLMChain(llm=model, prompt=new_prompt)
# response = chain.invoke("i said hi")

# print(response)