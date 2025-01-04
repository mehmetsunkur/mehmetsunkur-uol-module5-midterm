from llama_agent import LlamaAgent
from assignment import Assignment

class AgentManager:
    def __init__(self):
        self.agent = LlamaAgent()

    def execute_assignment(self, assignment: Assignment):
        for task in assignment.tasks:
            self.agent.execute_task(task)