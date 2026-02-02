# 调用对话模型
from langchain_openai import ChatOpenAI
import os

chat_model = ChatOpenAI(
    model="deepseek-chat",  #默认使用的是  gpt-3.5-turbo
    # 说明 ： 使用环境变量的方式在jupyter中执行不合适，需要在.py文件中执行
    base_url=os.environ['CHAT_BASE_URL'],
    api_key=os.environ['CHAT_API_KEY'],
)

# 调用模型
chat = chat_model.invoke("什么是LangChain？")

# 响应文本
print(chat.content)
print("---------------------------------------------------------")
print(chat)