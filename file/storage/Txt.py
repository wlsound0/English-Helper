def read(name: str) -> str:
    re = ''
    with open(name, 'r') as f:
        re = f.read()
    return re

def write(name: str, num: str) -> None:
    with open(name, 'w') as f:
        f.write(num)

def append(name: str, num: str) -> None:
    with open(name, 'a') as f:
        f.write(num)