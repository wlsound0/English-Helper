import json

def read(name: str) -> dict:
    re: dict = {}
    with open(name, 'r') as f:
        re = json.load(f)
    return re

def write(name: str, num: dict) -> None:
    with open(name, 'w') as f:
        json.dump(num, f)
