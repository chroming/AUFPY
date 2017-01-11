# coding: utf-8
from ui_class import *
from generate_code import *
from conn_sqlite import ConnSqlite

view = ui.View()
view.name = 'AUFPY'
view.background_color = 'white'

code_label = Nlabel(view)
code_label.center = (view.width*1.2, view.height*0.9)
name_label = Nlabel(view)
name_label.width *= 0.5
name_label.height *= 0.5
name_label.center = (view.width*0.7, view.height*1.3)
view.add_subview(name_label)
view.add_subview(code_label)

view.present('123')
c = ConnSqlite()

name_label.text = 'test'
secret_code = c.select_code('test')[0]

code_label.text, _ = get_code(secret_code)
