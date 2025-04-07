from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from information import INFORMATION as information

from loguru import logger


if __name__ == "__main__":
    load_dotenv()

    logger.info("Hello, LangChain! 🦜🔗")

    class Output(BaseModel):
        resume: str = Field(description="A resposta contendo o pequeno resumo.")
        factories: list[str] = Field(
            description="A lista contendo os fatos interessantes."
        )

    summary_prompt = """
        Fornecida informações {information} sobre uma pessoa, quero que você crie:
        1. um pequeno resumo
        2. dois fatos interessantes sobre ela
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_prompt
    )

    llm = ChatGroq(temperature=0, model="llama3-70b-8192").with_structured_output(
        Output
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
