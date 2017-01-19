# coding: utf-8
from ui_class import *
from generate_code import *
from conn_sqlite import ConnSqlite
from ui_conf import maincenter, mainsize
from input_view import InputView


class MainUI(ui.View):
    def __init__(self):
        self.name = 'AUFPY'
        self.background_color = 'white'
        self.conn = ConnSqlite()
        self.names = self.conn.select_all()
        self.name_count = len(self.names)
        self.present('123')
        # self._init_view()
        self._init_views()

    def _init_views(self):
        """
        根据 sqlite 中项的数量初始化界面
        :return: None
        """
        for c in range(0, self.name_count):
            code_text_name = 'code_text_%s' % c
            code_text = ntextfield(self)
            code_text = center_and_size(self, code_text, 'code_text', maincenter, mainsize, 0.1*c)
            code_text.enable = False
            code_text.name = code_text_name

            name_label_name = 'name_label_%s' % c
            name_label = nlabel(self)
            name_label = center_and_size(self, name_label, 'name_label', maincenter, mainsize, 0.1*c)
            name_label.enabled = False
            name_label.name = name_label_name

            self.add_subview(code_text)
            self.add_subview(name_label)

    def _init_view(self):
        """
        初始化界面
        :return: None
        """
        self.code_text = ntextfield(self)
        self.code_text.center = (self.width * maincenter['code_text'][0], self.height * maincenter['code_text'][1])
        self.code_text.width *= mainsize['code_text'][0]
        self.code_text.height *= mainsize['code_text'][1]
        self.code_text.enabled = False

        self.name_label = nlabel(self)
        self.name_label.width *= mainsize['name_label'][0]
        self.name_label.height *= mainsize['name_label'][1]
        self.name_label.center = (self.width * maincenter['name_label'][0], self.height * maincenter['name_label'][1])
        self.name_label.enabled = False

        self.add_button = nbutton(self)
        self.add_button.width *= mainsize['add_button'][0]
        self.add_button.height *= mainsize['add_button'][1]
        self.add_button.center = (self.width * maincenter['add_button'][0], self.height * maincenter['add_button'][1])
        self.add_button.action = self.add_tapped

        self.add_subview(self.name_label)
        self.add_subview(self.code_text)
        self.add_subview(self.add_button)

    def add_tapped(self, sender):
        InputView()

    def _set_text(self, code_text, name_text):
        """
        将 code_text 和 name_text 显示到界面上
        :param code_text: 生成的随机码
        :param name_text: 项名
        :return: None
        """
        self.code_text.text = code_text
        self.name_label.text = name_text

    def _set_texts(self, code_texts, name_texts):
        """
        将 code_texts 和 name_texts 显示到界面上
        :param code_texts:  生成的随机码 list
        :param name_texts: 项名 list
        :return:
        """
        for c in range(0, self.name_count):
            self['code_text_%s' % c].text = code_texts[c]
            self['name_label_%s' % c].text = name_texts[c]

    def get_text(self, name_text):
        """
        根据名称获取code_text 并调用 _set_text
        :param name_text: 名称
        :return: None
        """
        secret_code = self.conn.select_code(name_text)[0]
        code_text, _ = get_code(secret_code)
        self._set_text(code_text, name_text)

    def get_texts(self, name_texts):
        """
        根据名称 list 获取 code_texts 列表并调用 _set_texts
        :param name_texts: 名称 list
        :return: None
        """
        code_texts = []
        for c in range(0, self.name_count):
            code_text, _ = get_code(self.conn.select_code(name_texts[c])[0])
            code_texts.append(code_text)
        self._set_texts(code_texts, name_texts)

    def get_all(self):
        """
        从sqlite 中获取所有名称 并调用get_texts
        :return: None
        """
        names = self.conn.select_all()
        self.get_texts([name[0] for name in names])

if __name__ == '__main__':
    mui = MainUI()
    # mui.get_text('test')
    mui.get_all()
