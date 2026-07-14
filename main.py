import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.backend.controller import AppController
def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    controller = AppController(main_window)
    controller.run()
    sys.exit(app.exec())
if __name__ == "__main__": main()
