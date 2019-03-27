from .base_executor import BaseExecution


class DFExecutor(BaseExecution):
    def __init__(self):
        super().__init__('')


if __name__ == '__main__':
    a = DFExecutor()
    a.execute()
    a.flag
