import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口的尺寸, 不包括title的高度
        self.resize(400, 300)
        # 设置状态栏,并展示只存在5秒的消息
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息。', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('img/qt.ico'))
    main = MainWin()
    main.show()

    sys.exit(app.exec_())
