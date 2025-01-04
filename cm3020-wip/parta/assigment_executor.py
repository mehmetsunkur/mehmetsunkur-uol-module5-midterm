

class AssigmentExecutor:
    def __init__(self):
        self.executor = None
    
    def execute(self, data):
        if self.executor is None:
            self.executor = TeamBuilder()

