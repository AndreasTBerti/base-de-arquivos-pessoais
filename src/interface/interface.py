from PySide6.QtWidgets import QApplication, QWidget
from dataclasses import dataclass

@dataclass
class AppInterface():
    app: QApplication = QApplication([])
    window: QWidget = QWidget()

    def __post_init__(self):
        self.window.setWindowTitle("Gerenciador Pessoal")
        self.window.resize(600, 600)
        self.window.show()

        self.app.exec()


if __name__ == "__main__":
    AppInterface()