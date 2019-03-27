from .base_executor import BaseExecution


class DFInodeExecutor(BaseExecution):
    def __init__(self):
        super().__init__('-i')


if __name__ == '__main__':
    a = DFInodeExecutor()
    a.execute()
    a.flag



