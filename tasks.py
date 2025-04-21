from crewai import Task
from agents import news_researcher_agent, news_writer_agent
from tools import tool

# Research task
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "It's market oppourtunities, and potential risks."
    ),
    expected_output='A Comprehensive 3 paragraphs long report on the latest AI trends.',   
    tools=[tool],
    agent=news_researcher_agent
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer_agent,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)

