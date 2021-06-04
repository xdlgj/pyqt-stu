import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class LabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLabel控件')
        self.setGeometry(300, 300, 400, 300)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=red>这是一个文本标签。</font>")
        label1.setAutoFillBackground(True)  # 填充背景颜色
        palette = QPalette()  # 调色板
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)

        label2.setText("<a href='#'>欢迎使用python GUI</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./img/qt.ico'))
        # True用浏览器打开网页，False调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://www.baidu.com'>百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('百度')
        # 设置垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.hovered)
        label4.linkActivated.connect(self.activated)
        self.setLayout(vbox)

    @staticmethod
    def hovered():
        print('hovered')

    @staticmethod
    def activated():
        print('activated')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LabelDemo()
    main.show()
    sys.exit(app.exec_())
