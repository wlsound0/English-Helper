from .storage import Json
import json

def init() -> None:
    new: dict = {
        'file_mode': 'txt', 
        'draw_mode': 'sure', 
        'use_dict': 'sure'
    }
    Json.write('settings.json', new)
    
def read() -> dict:
    re = Json.read('settings.json')
    return re

def write(new: dict) -> None:
    Json.write('settings.json', new)
    
def check() -> int:
    '''
    1. 文件缺失
    2. 格式错误
    3. 参数缺失
    0. 正常
    '''
    try:
        data = read()
        name = ('file_mode', 'draw_mode', 'use_dict')
        for k in range(len(name)):
            a = data[name[k]]
    except FileNotFoundError:
        return 1
    except json.JSONDecodeError:
        return 2
    except KeyError:
        return 3
    return 0        
    