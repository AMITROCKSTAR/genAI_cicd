from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile")


prompt = PromptTemplate(
    input_variables =   ["question"],
    template = "Answer the question clearly: \n Question : {question}"

)


chain = prompt | llm

def ask_llm(question: str) -> str:
    return chain.invoke(question).content



# answer = ask_llm({"question":"new about ai"})

# print(answer)