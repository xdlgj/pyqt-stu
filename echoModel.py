import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class EchoModel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('EchoMode(回显模式)')
        # 1、创建表单布局, 添加参数self等价于self.setLayout(form_layout)
        form_layout = QFormLayout(self)
        # 2、创建QLineEdit
        normal = QLineEdit()
        no_echo = QLineEdit()
        password = QLineEdit()
        password_echo_on_edit = QLineEdit()
        # 3、把QLineEdit添加到布局中
        form_layout.addRow('normal', normal)
        form_layout.addRow('noEcho', no_echo)
        form_layout.addRow('password', password)
        form_layout.addRow('passwordEchoNoEdit', password_echo_on_edit)
        # 4、设置placeholder
        normal.setPlaceholderText('normal')
        no_echo.setPlaceholderText('noEcho')
        password.setPlaceholderText('password')
        password_echo_on_edit.setPlaceholderText('passwordEchoOnEdit')
        # 5、设置回显模式
        normal.setEchoMode(QLineEdit.Normal)
        no_echo.setEchoMode(QLineEdit.NoEcho)
        password.setEchoMode(QLineEdit.Password)
        password_echo_on_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # 5、设置布局
        # self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EchoModel()
    main.show()
    sys.exit(app.exec_())
