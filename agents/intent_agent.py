from crewai import Agent

intent_agent = Agent(
    role="Intent Classifier",
    goal="Identify banking-related user intent",
    backstory="Expert in banking customer queries",
    verbose=True
)
