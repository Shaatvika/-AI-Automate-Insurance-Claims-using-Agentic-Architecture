from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class AiAutomatedClaims():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def claim_processing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['claim_processing_agent'],
            verbose=True,
            multimodal=True
        )

    @agent
    def claim_approval_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['claim_approval_agent'],
            verbose=True
        )

    @agent
    def chatbot_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chatbot_agent'],
            verbose=True
            
        )

    @agent
    def monitoring_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['monitoring_agent'],
            verbose=True
            
        )

    @task
    def claim_filing_task(self) -> Task:
        return Task(
            config=self.tasks_config['claim_filing_task'],
        )

    @task
    def claim_approval_task(self) -> Task:
        return Task(
            config=self.tasks_config['claim_approval_task'],
        )

    @task
    def chatbot_task(self) -> Task:
        return Task(
            config=self.tasks_config['chatbot_task'],
        )

    @task
    def monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['monitoring_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
