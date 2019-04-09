import unittest
import json
from parsers.base_parser import BaseParser


class TestParserMethod(unittest.TestCase):
    def setUp(self):
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
        self.error_res = {
                "status": "failure",
                "error": "Error ERROR",
                "result": None
            }
        self.code_res = {
                "status": "failure",
                "error": "Error with return code 1",
                "result": None
            }
        self.res_str = b'Filesystem    512-blocks      Used Available Capacity iused        ' \
                       b'       ifree %iused  Mounted ' \
                       b'on\n/dev/disk1s1   976695384 804093856 152315664 ' \
                       b'   85% 2934521 9223372036851841286    0%   /\n'
        self.parser_with_error = BaseParser(None, "ERROR", 0)
        self.parser_without_error = BaseParser(self.res_str, None, 0)
        self.parser_with_nonzero_code = BaseParser('', None, 1)

    def test_parse(self):
        self.assertEqual(self.parser_with_error.parse(), json.dumps(self.error_res, indent=4))
        self.assertEqual(self.parser_without_error.parse(), json.dumps(self.res_dict, indent=4))
        self.assertEqual(self.parser_with_nonzero_code.parse(), json.dumps(self.code_res, indent=4))


if __name__ == "__main__":
    unittest.main()

