"""
窗口居中显示
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口的标题
        self.setWindowTitle('窗口居中')
        # 设置窗口的尺寸, 不包括title的高度
        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        left = int((screen.width() - size.width()) / 2)
        top = int((screen.height() - size.height()) / 2)
        self.move(left, top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('img/qt.ico'))
    main = CenterForm()
    main.center()
    main.show()
    sys.exit(app.exec_())
