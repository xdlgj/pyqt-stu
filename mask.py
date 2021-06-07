import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout


class Mask(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Mask')
        form_layout = QFormLayout(self)

        ip = QLineEdit()
        mac = QLineEdit()
        date = QLineEdit()
        lic = QLineEdit()
        # 掩码由掩码字符与分隔符字符串组成，后面可以跟一个分号和空白字符，空白字符在编辑后会从文本删除的
        ip.setInputMask('999.999.999.999;_')
        mac.setInputMask('>HH:HH:HH:HH:HH:HH;_')
        date.setInputMask('0000-00-00')
        lic.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')
        form_layout.addRow('ip', ip)
        form_layout.addRow('mac', mac)
        form_layout.addRow('date', date)
        form_layout.addRow('license', lic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Mask()
    main.show()
    sys.exit(app.exec_())
