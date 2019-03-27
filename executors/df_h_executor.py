from .base_executor import BaseExecution


class DFHumanReadableExecutor(BaseExecution):
    def __init__(self):
        super().__init__('-h')

