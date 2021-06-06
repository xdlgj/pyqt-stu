"""
设置伙伴关系
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout


class LabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('label伙伴关系')

        name_label = QLabel('&Name')  # 通过alt + N 可以将输入光标定位到输入框
        name_line_edit = QLineEdit()
        # 设置伙伴关系
        name_label.setBuddy(name_line_edit)

        password_label = QLabel('&Password')
        password_line_edit = QLineEdit()
        password_label.setBuddy(password_line_edit)

        btn_ok = QPushButton('确定')
        btn_cancel = QPushButton('取消')

        # 设置布局
        main_layout = QGridLayout(self)
        main_layout.addWidget(name_label, 0, 0)
        main_layout.addWidget(name_line_edit, 0, 1, 1, 2)
        main_layout.addWidget(password_label, 1, 0)
        main_layout.addWidget(password_line_edit, 1, 1, 1, 2)
        main_layout.addWidget(btn_ok, 2, 1)
        main_layout.addWidget(btn_cancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LabelBuddy()
    dialog.show()
    sys.exit(app.exec_())
