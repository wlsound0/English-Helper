class SettingOption:
    key: str    # json里的键
    name: str   # 中文名
    choises: dict   # {json存储值:值的中文名}
    def __init__(self, key: str, name: str, choises: dict) -> None:
        self.key = key
        self.name = name
        self.choises = choises