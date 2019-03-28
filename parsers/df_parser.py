from .base_parser import BaseParser


class DfParser(BaseParser):
    def __init__(self, df_res, df_error, return_code):
        super().__init__(df_res, df_error, return_code)
