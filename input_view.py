# coding: utf-8
from ui_class import *
from ui_conf import inputcenter, inputsize
from conn_sqlite import *
import notification

class InputView(ui.View):
    def __init__(self):
        self.name = "INPUT NAME & CODE"
        self.background_color = 'white'
        # self.conn = ConnSqlite()
        self.present('123')
        self._init_view()

    def _init_view(self):
        self.name_label = nlabel(self)
        self.name_label.center = (self.width * inputcenter['account_label'][0], self.height * inputcenter['account_label'][1])
        self.name_label.text = "ACCOUNT"
        self.name_textfield = ntextfield(self)
        self.name_textfield.center = (self.width * inputcenter['name_textfield'][0],
                                      self.height * inputcenter['name_textfield'][1])

        self.secret_label = nlabel(self)
        self.secret_label.center = (self.width * inputcenter['code_label'][0], self.height * inputcenter['code_label'][1])
        self.secret_label.text = "SECRET"
        self.secret_textfield = ntextfield(self)
        self.secret_textfield.center = (self.width * inputcenter['code_textfield'][0],
                                        self.height * inputcenter['code_textfield'][1])

        self.ok_button = nbutton(self)
        self.ok_button.title = 'OK'
        self.ok_button.center = (self.width * inputcenter['ok_button'][0], self.height * inputcenter['ok_button'][1])
        self.ok_button.action = self.ok_tapped

        self.cancel_button = nbutton(self)
        self.cancel_button.title = 'CANCEL'
        self.cancel_button.center = (self.width * inputcenter['cancel_button'][0],
                                     self.height * inputcenter['cancel_button'][1])
        self.cancel_button.action = self.cancel_tapped

        self.add_subview(self.name_label)
        self.add_subview(self.name_textfield)
        self.add_subview(self.secret_label)
        self.add_subview(self.secret_textfield)
        self.add_subview(self.ok_button)
        self.add_subview(self.cancel_button)

    def ok_tapped(self, sender):
        """
        内容保存到sqlite
        :param sender:
        :return: True
        """
        self.conn = ConnSqlite()
        name_text = self.name_textfield.text
        secret_text = self.secret_textfield.text
        if name_text and secret_text:
            self.conn.insert_value(name_text, secret_text)
            notification.schedule('Add success!', 1)
        self.conn.close_conn()

    def cancel_tapped(self, sender):
        self.close()

if __name__ == '__main__':
    iui = InputView()


