from executors.base_executor import BaseExecution
from parsers import DfParser


class DFExecutor(BaseExecution):
    def __init__(self):
        super().__init__('', DfParser)




