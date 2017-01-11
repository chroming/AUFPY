# coding: utf-8
"""
生成界面元素的函数
Pythonista 的 ui 类无法继承，只能写成函数形式
"""
import ui


def Nlabel(view):
    label = ui.Label()
    label.border_color = 'black'
    label.border_width = 2

    label.width = view.width * 2
    label.height = view.height * 0.5

    return label
