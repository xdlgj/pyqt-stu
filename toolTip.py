"""
显示提示信息
"""
import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget, QPushButton
from PyQt5.QtGui import QFont


class ToolTip(QWidget):
    def __init__(self):
        super(ToolTip, self).__init__()
        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('Arial', 12))
        self.setToolTip('今天是<b>周一</b>')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('设置控件提示')

        btn = QPushButton(self)
        btn.setText('按钮')
        btn.setToolTip('这是一个按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolTip()
    main.show()
    sys.exit(app.exec_())