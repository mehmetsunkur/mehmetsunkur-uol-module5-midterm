from dataclasses import dataclass
from typing import List
from task import Task

@dataclass
class Assignment:
    name: str
    tasks: List[Task]