from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
import yaml
from dotenv import load_dotenv
  # type: ignore[import]
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FraudDetectionBot():
    """FraudDetectionBot crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    llm = LLM(model ="gemini/gemini-1.5-flash", api_key= "AIzaSyBb2Srx5nvzf4C-TLjOaGNkvIGx3np6m14")  # type: ignore[assignment]

    

    def __init__(self):
        # Load agents and tasks configuration from YAML files
        with open(os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml'), 'r') as f:
            self.agents_config = yaml.safe_load(f)
        
        with open(os.path.join(os.path.dirname(__file__), 'config', 'tasks.yaml'), 'r') as f:
            self.tasks_config = yaml.safe_load(f)
     

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def detector(self) -> Agent:
        return Agent(
            config=self.agents_config['detector'], # type: ignore[index]
            verbose=True,
            llm = self.llm, # type: ignore[index]
            api_key=os.getenv("GEMINI_API_KEY") # type: ignore[index]
        )
    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True,
            llm = self.llm, # type: ignore[index]
            api_key=os.getenv("GEMINI_API_KEY") # type: ignore[index]
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def detection_task(self) -> Task:
        return Task(
            config=self.tasks_config['detection_task'], # type: ignore[index]
        )
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewer_task'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the FraudDetectionBot crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
