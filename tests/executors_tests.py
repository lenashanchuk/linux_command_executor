import unittest
import json
from executors.base_executor import BaseExecution
from parsers import DfParser
from unittest import mock


def communicate():
    res_str = b'Filesystem    512-blocks      Used Available Capacity iused        ' \
                   b'       ifree %iused  Mounted ' \
                   b'on\n/dev/disk1s1   976695384 804093856 152315664 ' \
                   b'   85% 2934521 9223372036851841286    0%   /\n'
    return res_str, None


class TestExecutorMethod(unittest.TestCase):
    def setUp(self):
        self.df_executor = BaseExecution('', DfParser)
        self.res_dict = {
                "status": "success",
                "error": None,
                "result": [
        {
            "Filesystem": "/dev/disk1s1",
            "512-blocks": "976695384",
            "Used": "804093856",
            "Available": "152315664",
            "Capacity": "85%",
            "iused": "2934521",
            "ifree": "9223372036851841286",
            "%iused": "0%",
            "Mounted_on": "/"
        }]
            }

    def test_executor(self):
        with mock.patch('executors.base_executor.subprocess') as subprocess:
            subprocess.Popen.return_value.returncode = 0
            subprocess.Popen.return_value.communicate = communicate
            self.assertEqual(self.df_executor.execute(), json.dumps(self.res_dict, indent=4))


if __name__ == "__main__":
    unittest.main()
