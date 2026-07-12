from PySide6.QtWidgets import QMessageBox, QFileDialog
from src.GUI.welcome_ui import Ui_MainWindow
from src.backend.data_manager import DataManager
from src.backend.config import GAConfig
from src.backend.math_functions import Polynom
from src.backend.genetic_algorithm import GeneticAlgorithm

class AppController:
    def __init__(self, window):
        self.window = window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.data_manager = DataManager()
        self.ga_config = GAConfig()
        self.ga = None
        self.current_task = None

        self.connect_signals()

    def connect_signals(self):
        self.ui.startButton.clicked.connect(self.on_manual_input)
        self.ui.loadButton.clicked.connect(self.on_load_file)
        self.ui.randomButton.clicked.connect(self.on_random_generate)
        self.ui.aboutButton.clicked.connect(self.on_about)

        self.ui.backButton_1.clicked.connect(self.on_back_to_menu)
        self.ui.nextButton_1.clicked.connect(self.submit_entered_data)

    def on_manual_input(self):
        self.ui.stackedWidget.setCurrentIndex(1)

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

    def on_back_to_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def submit_entered_data(self):
        deg = self.ui.degSpinBox.value()
        coefs_str = self.ui.coefLineEdit.text().strip()
        l = self.ui.beginnigIntSpinBox.value()
        r = self.ui.endIntSpinBox.value()
        steps = self.ui.stepsSpinBox.value()

        if not coefs_str:
            QMessageBox.warning(self.window, "Ошибка", "Введите коэффициенты полинома")
            return

        try:
            coefs = [float(x) for x in coefs_str.split()]
            if len(coefs) != deg + 1:
                QMessageBox.warning(self.window, "Ошибка", f"Для степени {deg} необходимо "
                                                           f"ввести {deg + 1} коэффициентов")
                return

            for coef in coefs:
                if not (-5 <= coef <= 5):
                    QMessageBox.warning(self.window, "Ошибка", f"Коэффициент {coef} выходит за пределы "
                                                               f"[-5; 5]")
                    return

            if l >= r:
                QMessageBox.warning(self.window, "Ошибка", "Начало интервала не может быть больше конца")
                return

            self.current_task = {
                'polynom': coefs,
                'interval': [l, r],
                'steps': steps
            }
            print("OK")
            self.algorithm()

        except ValueError:
            QMessageBox.critical(self.window, "Ошибка", "Коэффициенты должны быть числами, "
                                                        "разделенными пробелами")

    def algorithm(self):
        pass

    def on_about(self):
        QMessageBox.about(self.window,"О программе",
        "Приближение полиномиальной функции ступенчатой функцией с использованием генетического алгоритма.\n\n"
            "Разработано в рамках учебной практики СПбГЭТУ ЛЭТИ.\n\n"
            "Авторы: Шувалов Алексей, Трушкин Александр, Гавриш Матвей"
        )

    def run(self):
        self.window.show()