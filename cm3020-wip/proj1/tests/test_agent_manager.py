import pytest
from agent_manager import AgentManager
from assignment import Assignment, Task

def test_execute_assignment():
    tasks = [
        Task(name="Test Task 1", description="Description for task 1"),
        Task(name="Test Task 2", description="Description for task 2")
    ]
    assignment = Assignment(name="Test Assignment", tasks=tasks)
    agent_manager = AgentManager()
    agent_manager.execute_assignment(assignment)
    # Add assertions to verify task execution if needed