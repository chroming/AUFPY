# coding: utf-8
"""
生成界面元素的函数
Pythonista 的 ui 类无法继承，只能写成函数形式
"""
import ui


def ntextfield(view):
    textfield = ui.TextField()

    textfield.width = view.width * 0.8
    textfield.height = view.height * 0.05

    return textfield


def nlabel(view):
    label = ui.Label()

    label.width = view.width * 0.3
    label.height = view.height * 0.05

    label.text_color = 'black'

    return label


def nbutton(view):
    button = ui.Button()

    button.border_color = 'black'
    button.border_width = 2

    button.width = view.width * 0.2
    button.height = view.height * 0.05

    button.tint_color = 'black'

    return button


def center_and_size(view, subview, subview_name, center_json, size_json, hei=0, wid=0):
    subview.center = (view.width * (center_json[subview_name][0] + wid), view.height * (center_json[subview_name][1] + hei))
    subview.width *= size_json[subview_name][0]
    subview.height *= size_json[subview_name][1]
    return subview