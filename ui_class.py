# coding: utf-8
"""
生成界面元素的函数
Pythonista 的 ui 类无法继承，只能写成函数形式
"""
import ui


def ntextfield(view):
    textfield = ui.TextField()

    # textfield.border_color = 'black'
    # textfield.border_width = 2

    textfield.width = view.width * 0.8
    textfield.height = view.height * 0.05

    return textfield


def nlabel(view):
    label = ui.Label()

    label.width = view.width * 0.3
    label.height = view.height * 0.05

    return label


def nbutton(view):
    button = ui.Button()

    button.border_color = 'black'
    button.border_width = 2

    button.width = view.width * 0.2
    button.height = view.height * 0.05

    return button
