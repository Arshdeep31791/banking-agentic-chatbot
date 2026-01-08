from crewai import Crew, Task
from agents.intent_agent import intent_agent

crew = Crew(
    agents=[intent_agent],
    tasks=[Task(description="Understand user intent")],
    verbose=True
)
