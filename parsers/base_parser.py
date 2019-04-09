import re
import json


class BaseParser:
    def __init__(self, df_res, df_error, return_code):
        self.df_res = df_res
        self.df_error = df_error
        self.return_code = return_code

    def parse(self):
        if self.return_code:
            status = "failure"
            error = f"Error with return code {self.return_code}"
            result = None
        elif self.df_error:
            status = "failure"
            error = f"Error {self.df_error}"
            result = None
        else:
            data = self.df_res.decode("utf-8").replace("Mounted on", "Mounted_on")
            rows = []
            for line in data.split('\n'):
                line = re.sub('\s+', ' ', line)
                rows.append(line.split(' '))
            keys = rows.pop(0)
            result_list = []
            for row in rows[:len(rows)-1]:
                result_list.append(dict(zip(keys, row)))
            status = "success"
            error = None
            result = result_list

        result_dict = {
            "status": status,
            "error": error,
            "result": result
        }
        json_result = json.dumps(result_dict, indent=4)
        return json_result



