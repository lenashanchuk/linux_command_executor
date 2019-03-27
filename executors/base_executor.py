import subprocess


class BaseExecution:
    def __init__(self, flag, parser):
        self.flag = flag
        self.parser = parser

    def execute(self):
        process = subprocess.Popen(f'df {self.flag}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = process.communicate()
        print(output, err)

