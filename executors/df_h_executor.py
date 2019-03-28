from .base_executor import BaseExecution
from parsers import DfHumanReadableParser


class DFHumanReadableExecutor(BaseExecution):
    def __init__(self):
        super().__init__('-h', DfHumanReadableParser)


