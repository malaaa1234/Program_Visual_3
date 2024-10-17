from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button1")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()