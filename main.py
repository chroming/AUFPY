# coding: utf-8
import dialogs
import notification
from ui_class import *
from generate_code import *
from conn_sqlite import ConnSqlite
from ui_conf import maincenter, mainsize


class MainUI(ui.View):
    def __init__(self):
        self.name = 'AUFPY'
        self.background_color = 'white'
        self.conn = ConnSqlite()
        self.all_accounts = self.conn.select_all()
        self.accounts_count = len(self.all_accounts)
        self.present('123')
        # self._init_view()
        self._init_views()

    def _init_views(self):
        """
        根据 sqlite 中项的数量初始化界面
        :return: None
        """
        for c in range(0, self.accounts_count):
            code_text_name = 'code_text_%s' % c
            code_text = ntextfield(self)
            code_text = center_and_size(self, code_text, 'code_text', maincenter, mainsize, 0.1*c)
            code_text.enable = False
            code_text.name = code_text_name

            account_label_name = 'name_label_%s' % c
            account_label = nlabel(self)
            account_label = center_and_size(self, account_label, 'account_label', maincenter, mainsize, 0.1*c)
            account_label.enabled = False
            account_label.name = account_label_name

            self.add_subview(code_text)
            self.add_subview(account_label)

        self.add_button = nbutton(self)
        self.button.title = 'ADD'
        self.add_button.width *= mainsize['add_button'][0]
        self.add_button.height *= mainsize['add_button'][1]
        self.add_button.center = (self.width * maincenter['add_button'][0], self.height * maincenter['add_button'][1])
        self.add_button.action = self.add_button_tapped

        self.add_subview(self.add_button)



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

        self.account_label = nlabel(self)
        self.account_label.width *= mainsize['account_label'][0]
        self.account_label.height *= mainsize['account_label'][1]
        self.account_label.center = (self.width * maincenter['account_label'][0], self.height * maincenter['account_label'][1])
        self.account_label.enabled = False

        self.add_button = nbutton(self)
        self.add_button.width *= mainsize['add_button'][0]
        self.add_button.height *= mainsize['add_button'][1]
        self.add_button.center = (self.width * maincenter['add_button'][0], self.height * maincenter['add_button'][1])
        self.add_button.action = self.add_button_tapped

        self.add_subview(self.account_label)
        self.add_subview(self.code_text)
        self.add_subview(self.add_button)

    def show_input_dialog(self):
        return dialogs.form_dialog(fields=[{'type': 'text', 'key': 'account', 'title': 'account'},
                                   {'type': 'text', 'key': 'key', 'title': 'secret key'}])

    def add_button_tapped(self, sender):
        get_input_dict = self.show_input_dialog()
        self._save_to_db(get_input_dict) if get_input_dict else None

    def _save_to_db(self, new_dict):
        self.conn = ConnSqlite()
        account = new_dict['account']
        key = new_dict['key']
        if account and key:
            self.conn.insert_value(account, key)
            notification.schedule('Add success!', 1)
        self.conn.close_conn()

    def _show_text(self, code_text, name_text):
        """
        将 code_text 和 name_text 显示到界面上
        :param code_text: 生成的随机码
        :param name_text: 项名
        :return: None
        """
        self.code_text.text = code_text
        self.account_label.text = name_text

    def _show_all_texts(self, code_texts, all_accounts):
        """
        将 code_texts 和 all_accounts 显示到界面上
        :param code_texts:  生成的随机码 list
        :param all_accounts: 项名 list
        :return:
        """
        for c in range(0, self.accounts_count):
            self['code_text_%s' % c].text = code_texts[c]
            self['name_label_%s' % c].text = all_accounts[c]

    def _get_code(self, account):
        """
        根据名称获取code_text 并调用 _show_text
        :param account: 名称
        :return: None
        """
        secret_code = self.conn.select_code(account)[0]
        code_text, _ = get_code(secret_code)
        self._show_text(code_text, account)

    def _get_all_codes(self, name_texts):
        """
        根据名称 list 获取 code_texts 列表并调用 _show_all_texts
        :param name_texts: 名称 list
        :return: None
        """
        code_texts = []
        for c in range(0, self.accounts_count):
            code_text, _ = get_code(self.conn.select_code(name_texts[c])[0])
            code_texts.append(code_text)
        self._show_all_texts(code_texts, name_texts)

    def get_all_accounts(self):
        """
        从sqlite 中获取所有名称 并调用get_texts
        :return: None
        """
        names = self.conn.select_all()
        self._get_all_codes([name[0] for name in names])

if __name__ == '__main__':
    mui = MainUI()
    # mui._get_code('test')
    mui.get_all_accounts()
