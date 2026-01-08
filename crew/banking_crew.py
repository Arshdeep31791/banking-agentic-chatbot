from crewai import Crew, Task

crew = Crew(
    agents=[intent_agent, retrieval_agent, compliance_agent, response_agent],
    tasks=[
        Task(description="Understand user intent"),
        Task(description="Retrieve relevant policy info"),
        Task(description="Check compliance"),
        Task(description="Generate final answer")
    ],
    verbose=True
)
