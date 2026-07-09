import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from welcome_ui import Ui_MainWindow
from data_manager import DataManager
from config import GAConfig
from math_functions import Polynom
from genetic_algorithm import GeneticAlgorithm


class AppController:
    def __init__(self):
        self.data_manager = DataManager()
        self.ga_config = GAConfig()
        self.ga = None
        self.current_task = None

        # Инициализация GUI
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.connect_signals()

    def connect_signals(self):
        self.ui.startButton.clicked.connect(self.on_manual_input)
        self.ui.loadButton.clicked.connect(self.on_load_file)
        self.ui.randomButton.clicked.connect(self.on_random_generate)
        self.ui.aboutButton.clicked.connect(self.on_about)

    def on_manual_input(self):
        print("Открыть окно ручного ввода")

    def on_load_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.window,
            "Выберите файл с параметрами",
            "",
            "JSON файлы (*.json);;Все файлы (*)"
        )

        if filename:
            try:
                task_data, config = self.data_manager.load_from_file(filename)
                self.current_task = task_data

                if config:
                    self.ga_config = config

                print(f"Загружена задача: {task_data}")
                print(f"Параметры ГА: {self.ga_config}")

            except Exception as e:
                QMessageBox.critical(self.window, "Ошибка", f"Не удалось загрузить файл:\n{str(e)}")

    def on_random_generate(self):
        self.current_task = self.data_manager.generate_random_task()

        print(f"Сгенерирована случайная задача: {self.current_task}")

    def on_about(self):
        QMessageBox.about(
            self.window,
            "О программе",
            "Приближение полиномиальной функции ступенчатой функцией\n"
            "с использованием генетического алгоритма.\n\n"
            "Разработано в рамках учебной практики СПбГЭТУ ЛЭТИ"
        )

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    controller = AppController()
    controller.run()