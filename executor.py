from executors import DFHumanReadableExecutor, DFExecutor, DFInodeExecutor


class Executor:
    @staticmethod
    def execute(flag):
        if flag == 'human':
            executor_type = DFHumanReadableExecutor
        elif flag == 'inode':
            executor_type = DFInodeExecutor
        else:
            executor_type = DFExecutor
        df_executor = executor_type()
        return df_executor.execute()
