import json
import sys
from typing import Dict

from converter import convert2swift

def main():
    input_json: Dict[str, str] = json.loads(sys.stdin.read())

    print(convert2swift(input_json))

main()
