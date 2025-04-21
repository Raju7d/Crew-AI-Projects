from crewai import Crew,Process
from tasks import research_task, write_task
from agents import news_researcher_agent, news_writer_agent

# Formatting thetech focused with some enhanced config

crew=Crew(
    agents=[news_researcher_agent, news_writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential,
)


# Starting the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)