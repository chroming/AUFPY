# coding: utf-8
from ui_class import *
from generate_code import *
from conn_sqlite import ConnSqlite
from ui_conf import maincenter, mainsize


class MainUI(ui.View):
    def __init__(self):
        self.name = 'AUFPY'
        self.background_color = 'white'
        self.conn = ConnSqlite()
        self._init_view()
        self.present('123')

    def _init_view(self):
        """
        初始化界面
        :return: None
        """
        self.code_text = ntextfield(self)
        self.code_text.center = (self.width * maincenter['code_text'][0], self.height * maincenter['code_text'][1])
        self.code_text.enabled = False
        self.name_text = ntextfield(self)
        self.name_text.width *= mainsize['code_text'][0]
        self.name_text.height *= mainsize['code_text'][1]
        self.name_text.center = (self.width * maincenter['name_text'][0], self.height * maincenter['name_text'][1])
        self.name_text.enabled = False
        self.add_subview(self.name_text)
        self.add_subview(self.code_text)

    def _set_text(self, code_text, name_text):
        self.code_text.text = code_text
        self.name_text.text = name_text

    def get_text(self, name_text):
        """
        根据名称获取secret_code 并调用 _set_text
        :param name_text: 名称
        :return: None
        """
        secret_code = self.conn.select_code(name_text)[0]
        code_text, _ = get_code(secret_code)
        self._set_text(code_text, name_text)


if __name__ == '__main__':
    mui = MainUI()
    mui.get_text('test')
