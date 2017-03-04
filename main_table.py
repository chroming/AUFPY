# coding: utf-8
from generate_code import *
from conn_sqlite import ConnSqlite
import ui
import dialogs
import notification


def _show_all_texts(code_texts, all_accounts):
    len_c = len(code_texts)
    codes_accounts = [(code_texts[x], all_accounts[x]) for x in range(len_c)]
    main_ui.data_source = ui.ListDataSource(['%s -- %s' % (x, y) for x, y in codes_accounts])
    main_ui.present()
    auto_reload()


def reload_all_texts(code_texts, all_accounts):
    len_c = len(code_texts)
    codes_accounts = [(code_texts[x], all_accounts[x]) for x in range(len_c)]
    main_ui.data_source = ui.ListDataSource(['%s -- %s' % (x, y) for x, y in codes_accounts])
    main_ui.reload()


def _get_all_codes():
    global countdown
    """
    根据名称 list 获取 code_texts 列表并调用 _show_all_texts
    :param name_texts: 名称 list
    :return: None
    """
    code_texts = []
    for c in name_texts:
        code_text, countdown = get_code(conn.select_code(c)[0])
        code_texts.append(code_text)
    _show_all_texts(code_texts, name_texts)


def get_all_accounts():
    global name_texts
    """
    从sqlite 中获取所有名称 并调用get_texts
    :return: None
    """
    names = conn.select_all()
    name_texts = [name[0] for name in names]
    _get_all_codes()


def add_button_tapped(sender):
    get_input_dict = show_input_dialog()
    _save_to_db(get_input_dict) if get_input_dict else None


def show_input_dialog():
    return dialogs.form_dialog(fields=[{'type': 'text', 'key': 'account', 'title': 'account'},
                               {'type': 'text', 'key': 'key', 'title': 'secret key'}])


def _save_to_db(new_dict):
    conn = ConnSqlite()
    account = new_dict['account']
    key = new_dict['key']
    if account and key:
        conn.insert_value(account, key)
        notification.schedule('Add success!', 1)
    conn.close_conn()


def auto_reload():
    global countdown
    while main_ui.on_screen:
        countdown -= 1
        if countdown == 0:
            _get_all_codes()
            break
        else:
            time_button_item.title = '%s' % str(countdown)
            main_ui.reload()
            time.sleep(1)

countdown = '*'
main_ui = ui.TableView()
main_ui.name = 'AUFPY'
add_button_item = ui.ButtonItem()
add_button_item.title = 'ADD'
add_button_item.action = add_button_tapped
time_button_item = ui.ButtonItem()
time_button_item.title = '%s' % countdown
main_ui.right_button_items = [add_button_item, time_button_item]

conn = ConnSqlite()
get_all_accounts()