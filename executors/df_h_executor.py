from .base_executor import BaseExecution


class DFHumanReadableExecutor(BaseExecution):
    def __init__(self):
        super().__init__('-h')


if __name__ == '__main__':
    a = DFHumanReadableExecutor()
    a.execute()
    a.flag
