import dialogs


def show_input_dialog():
    return dialogs.form_dialog(fields=[{'type': 'text', 'key': 'account', 'title': 'account'},
                               {'type': 'text', 'key': 'key', 'title': 'secret key'}])

