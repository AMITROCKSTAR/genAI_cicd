from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os


llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)


prompt = PromptTemplate(
    input_variables =   ["question"],
    template = "Answer the question clearly and accurately: \n Question : {question}"

)


chain = prompt | llm

def ask_llm(question: str) -> str:
    return chain.invoke({"question":question}).content

