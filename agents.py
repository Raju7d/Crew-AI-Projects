from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm = LLM(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini/gemini-1.5-flash"  
)
print(llm)

# Creating a senior researcher agent with memory and verbose mode
news_researcher_agent=Agent(
    role="Senior researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, You're at the forefront of"
        "innovation, eager to explore and share kowlege that could"
        "change the world"
    ),
    tools=[],
    llm=llm,
    allow_delegation=True
)

# Creating a write agent with custom tools responsible in writing new blog

news_writer_agent=Agent(
    role="News writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"

    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)
