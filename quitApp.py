"""
退出应用程序
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class QuitApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('退出应用程序')
        self.resize(400, 300)
        # 设置主窗口的标题
        self.setWindowTitle('窗口居中')
        # 设置窗口的尺寸, 不包括title的高度
        self.resize(400, 300)

        # 添加button
        self.button_quit = QPushButton('退出')
        # 将信号与槽进行关联
        self.button_quit.clicked.connect(self.on_click_button)
        # 设置布局
        layout = QHBoxLayout()
        layout.addWidget(self.button_quit)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_click_button(self):
        """
        处理按钮单击事件
        """
        sender = self.sender()
        print(sender.text())  # 退出
        application = QApplication.instance()
        # 退出应用程序
        application.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('img/qt.ico'))
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())
