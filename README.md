## 主窗口类型
1. QMainWindow
    - 可以包含菜单栏、工具栏、状态栏和标题栏，是最常见的窗口形式。
2. QWidget
    - 不确定窗口的用途，就用QWidget
3. QDialog
    - 是对话窗口的基类，没有菜单栏、工具栏、状态栏。
## QDesktopWidget
```python
from PyQt5.QtWidgets import QDesktopWidget
screen = QDesktopWidget().screenGeometry()
screen.width()  # 屏幕宽度
screen.height() # 屏幕高度
```