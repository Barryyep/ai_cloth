from ai_cloth.parser import BaseParse
import json

class InputParser(BaseParse):
    def __init__(self, args):
        super().__init__(args)
# parse to get a json from a string
    def parse(self, input_str):
        return json.loads(input_str)
        