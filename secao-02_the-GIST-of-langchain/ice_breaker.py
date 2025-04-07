from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from loguru import logger
from pydantic import BaseModel, Field

from information import INFORMATION

if __name__ == '__main__':
    # carregando as variáveis de ambiente do .env
    load_dotenv()

    # logando mensagem
    logger.info('Hello, LangChain! 🦜🔗')

    # classe de output, estrutura de retorno
    class Output(BaseModel):
        # campo string que será um resumo
        resume: str = Field(
            description='A resposta contendo o pequeno resumo.'
        )

        # lista de strings
        factories: list[str] = Field(
            description='A lista contendo os fatos interessantes.'
        )

    # template, com {variavel} que será inserida no PromptTemplate
    summary_prompt = """
        Fornecida informações {information} sobre uma pessoa,
        quero que você crie:
        1. um pequeno resumo
        2. dois fatos interessantes sobre ela
    """

    # PromptTemplate
    summary_prompt_template = PromptTemplate(
        # variáveis dispostas no summary_template
        input_variables=['information'],
        # summary_template
        template=summary_prompt,
    )

    # modelo de linguagem
    llm = ChatGroq(
        # temperatura - nível de criatividade do modelo
        temperature=0,
        # modelo utilizado
        model='llama3-70b-8192',
        # utilizando o pydantic model como retorno estruturado
    ).with_structured_output(Output)

    # criação da chain com o prompt e o modelo
    chain = summary_prompt_template | llm

    # perguntando
    res = chain.invoke(
        # a constante INFORMATION será usada no lugar de {information}
        # no summary_prompt, como definimos no PromptTemplate
        input={'information': INFORMATION}
    )

    # printa a resposta
    print(res)
