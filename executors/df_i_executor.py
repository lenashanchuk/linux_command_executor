from .base_executor import BaseExecution
from parsers import DfInodeParser


class DFInodeExecutor(BaseExecution):
    def __init__(self):
        super().__init__('-i', DfInodeParser)
