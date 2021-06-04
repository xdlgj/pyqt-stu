"""
屏幕坐标系
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class ScreenGeometry(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle('屏幕坐标系')
        self.resize(400, 300)
        self.move(250, 200)

        btn = QPushButton(self)
        btn.setText('按钮')
        # 绑定事件
        btn.clicked.connect(self.on_click)

    def on_click(self):
        """
        点击事件
        """
        print('x:', self.x())  # 250 窗口x坐标
        print('y:', self.y())  # 200 窗口y坐标
        print('width:', self.width())  # 400 容器宽度
        print('height:', self.height())  # 300 容器高度

        print('geometry().x:', self.geometry().x())  # 250 容器x坐标
        print('geometry().y:', self.geometry().y())  # 222 容器y坐标
        print('geometry().width:', self.geometry().width())  # 400 容器宽度
        print('geometry().height:', self.geometry().height())  # 300 容器高度

        print('frameGeometry().x:', self.frameGeometry().x())  # 250 窗口x坐标
        print('frameGeometry().y:', self.frameGeometry().y())  # 200 窗口y坐标
        print('frameGeometry().width:', self.frameGeometry().width())  # 400 窗口宽度
        print('frameGeometry().height:', self.frameGeometry().height())  # 322 窗口高度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScreenGeometry()
    main.show()
    sys.exit(app.exec_())
