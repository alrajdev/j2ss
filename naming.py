import re
from typing import List

ALPHANUM = re.compile(pattern="[A-Za-z0-9]")

def pascalCase(input: str) -> str:
    output: List[str] = []
    for i in range(0, len(input)):
        previous = input[i - 1] if i > 0 else None
        current = input[i]

        if not ALPHANUM.match(current):
            continue

        if len(output) ==  0: # first word first letter shoud be lower
            output.append(current.lower())
        elif previous == "_": # word's first letter should be upper
            output.append(current.upper()) 
        elif previous.isupper(): # remaining char should be lower
            output.append(current.lower())
        else:
            output.append(current)
        
    return "".join(output)