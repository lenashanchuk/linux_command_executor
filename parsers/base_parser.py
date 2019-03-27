import re
import json


class BaseParser:
    def __init__(self, df_res, df_error, return_code):
        self.df_res = df_res
        self.df_error = df_error
        self.return_code = return_code

    def parse(self):
        if self.return_code:
            result_dict = {
                "status": "failure",
                "error": f"Error with return code {self.return_code}",
                "result": "None"
            }
        elif self.df_error:
            result_dict = {
                "status": "failure",
                "error": f"Error {self.df_error}",
                "result": "None"
            }
        else:
            data = self.df_res.decode("utf-8")
            rows = []
            for line in data.split('\n'):
                line = re.sub('\s+', ' ', line)
                rows.append(line.split(' '))
            keys = rows.pop(0)
            result_list = []
            for row in rows:
                result_list.append(dict(zip(keys, row)))
            result_dict = {
                "status": "success",
                "error": "None",
                "result": result_list
            }
        json_result = json.dumps(result_dict, indent=4)
        return json_result



