class Settings:
    file_mode: str
    draw_mode: str
    def __init__(self, file_mode = '', draw_mode = '') -> None:
        self.file_mode = file_mode
        self.draw_mode = draw_mode
    def to_dict(self) -> dict:
        re: dict = {}
        re['file_mode'] = self.file_mode
        re['draw_mode'] = self.draw_mode
        return re
    def dict_to(self, d: dict) -> None:
        self.file_mode = d['file_mode']
        self.draw_mode = d['draw_mode']
    def change(self, mode: str, num: str) -> None:
        setattr(self, mode, num)