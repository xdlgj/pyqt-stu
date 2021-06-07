import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class Validator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('校验器')
        form_layout = QFormLayout(self)

        line1 = QLineEdit()
        line2 = QLineEdit()
        line3 = QLineEdit()

        form_layout.addRow('整数：', line1)
        form_layout.addRow('浮点数：', line2)
        form_layout.addRow('正则：', line3)

        # 整数校验器
        int_validator = QIntValidator(self)
        int_validator.setRange(-10, 9)
        line1.setValidator(int_validator)

        double_validator = QDoubleValidator(self)
        double_validator.setRange(-100, 100)  # 此处范围限制存在bug
        double_validator.setNotation(QDoubleValidator.StandardNotation)  # 标准记法
        double_validator.setDecimals(2)  # 保留两位小数
        line2.setValidator(double_validator)

        reg_validator = QRegExpValidator(self)
        reg = QRegExp('[0-9a-zA-Z]+')
        reg_validator.setRegExp(reg)
        line3.setValidator(reg_validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Validator()
    main.show()
    sys.exit(app.exec_())
