from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

information = """
Vladimir Vladimirovitch Putin (russo: Влади́мир Влади́мирович Пу́тинⓘ, AFI: [vɫɐˈdʲimʲɪr vɫɐˈdʲimʲɪrəvʲɪtɕ ˈputʲɪn]; Leningrado, 7 de outubro de 1952) é um político russo, ex-advogado e ex-oficial de inteligência que atua como presidente da Rússia desde 2012. Putin ocupou cargos contínuos como presidente ou primeiro-ministro desde 1999: como primeiro-ministro de 1999 a 2000 e de 2008 a 2012, e como presidente de 2000 a 2008. Ele é o líder russo ou soviético que permanece há mais tempo no poder desde Josef Stalin.

Formado em Direito pela Universidade Estatal de São Petersburgo (1975), Putin também já trabalhou como advogado.[4] Posteriormente, atuou como oficial de inteligência estrangeira da KGB durante 16 anos, ascendendo ao posto de tenente-coronel antes de renunciar em 1991 para iniciar uma carreira política em São Petersburgo. Em 1996, mudou-se para Moscou para ingressar na administração do presidente Boris Yeltsin. Ele serviu brevemente como diretor do Serviço Federal de Segurança (FSB) e depois como secretário do Conselho de Segurança da Rússia antes de ser nomeado primeiro-ministro em agosto de 1999. Após a renúncia de Yeltsin, Putin tornou-se presidente interino e, em menos de quatro meses, foi eleito para o seu primeiro mandato como presidente. Posteriormente, foi reeleito em 2004. Devido às limitações constitucionais de dois mandatos presidenciais consecutivos, Putin serviu novamente como primeiro-ministro de 2008 a 2012 no governo de Dmitry Medvedev. Retornou à presidência em 2012, após uma eleição marcada por denúncias de fraudes e protestos, sendo reeleito em 2018. Em abril de 2021, após um referendo, ele sancionou emendas constitucionais que lhe permitiam concorrer à reeleição mais duas vezes, potencialmente estendendo sua presidência até 2036.
"""

if __name__ == "__main__":
    load_dotenv()

    print("Hello, LangChain! 🦜🔗")

    summary_prompt = """
        Fornecida informações {information} sobre uma pessoa, quero que você crie:
        1. um pequeno resumo
        2. dois fatos interessantes sobre ela
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_prompt
    )

    llm = ChatGroq(temperature=0, model="llama3-70b-8192")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
