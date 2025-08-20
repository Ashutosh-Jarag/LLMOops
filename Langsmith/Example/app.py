from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_PROJECT"] = "TEST_LLM_APP"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"input": "What is the capital of france?"})

print(result)