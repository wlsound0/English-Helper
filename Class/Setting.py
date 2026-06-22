class Settings:
    file_mode: str
    draw_mode: str
    def __init__(self, file_mode = '', draw_mode = '', use_dict = '') -> None:
        self.file_mode = file_mode
        self.draw_mode = draw_mode
        self.use_dict = use_dict
    def to_dict(self) -> dict:
        re: dict = {}
        re['file_mode'] = self.file_mode
        re['draw_mode'] = self.draw_mode
        re['use_dict'] = self.use_dict
        return re
    def dict_to(self, d: dict) -> None:
        self.file_mode = d['file_mode']
        self.draw_mode = d['draw_mode']
        self.use_dict = d['use_dict']
    def change(self, mode: str, num: str) -> None:
        setattr(self, mode, num)