import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from pprint import pprint

from langchain_core.prompts import PromptTemplate

load_dotenv()


def main():
    print("Hello from ai-agent-hello-world!")

    information = "Artemis III is an upcoming lunar mission, planned to be the second crewed mission in NASA's Artemis exploration program, with a targeted launch in mid-2027. The crew will launch aboard the Space Launch System (SLS) rocket carrying the Orion spacecraft.The mission will rendezvous in Earth orbit with one or both commercially developed Human Landing System (HLS) vehicles—SpaceX's Starship HLS and Blue Origin's Blue Moon—which will be launched separately by their commercial providers. The mission will test rendezvous and docking operations and may also include evaluation of the Axiom Extravehicular Mobility Unit (AxEMU) space suit. It is broadly comparable to Apollo 9 in the Apollo program. Artemis III was originally planned as the first crewed lunar landing since Apollo 17 in 1972.[6] By 2023, however, NASA had indicated the mission could proceed without a landing due to Orion spacecraft heat shield concerns and delays in the development of the Starship HLS. Alternative concepts studied included a crewed visit to the now-cancelled Lunar Gateway space station and a low Earth-orbit docking test between Orion and the Starship HLS.[7] On February 27, 2026, NASA administrator Jared Isaacman confirmed a revised plan for Artemis III to perform tests with one or both landers in Earth orbit, with Artemis IV tentatively designated as the first crewed lunar landing mission of the Artemis program, scheduled for 2028."

    summary_template = "Given the following information {information}, create the following:" \
    "1. A concise summary of the information in 1-2 sentences." \
    "2. A list of 3-5 key points from the information." \
    
    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=["information"])

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    pprint(response)
    pprint(response.content)

if __name__ == "__main__":
    main()
