from PySide6.QtWidgets import QMessageBox, QFileDialog, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.GUI.welcome_ui import Ui_MainWindow
from src.backend.data_manager import DataManager
from src.backend.config import GAConfig
from src.backend.math_functions import Polynom, StepFunc
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

        self.current_generation = 0
        self.current_individual = 0

        self.function_figure = None
        self.function_canvas = None
        self.error_figure = None
        self.error_canvas = None

        self.init_plots()
        self.connect_signals()

    def init_plots(self):
        self.function_figure = Figure()
        self.function_canvas = FigureCanvas(self.function_figure)
        self.function_canvas.setParent(self.ui.functionPlotContainer)

        layout = QVBoxLayout(self.ui.functionPlotContainer)
        layout.addWidget(self.function_canvas)

        self.error_figure = Figure()
        self.error_canvas = FigureCanvas(self.error_figure)
        self.error_canvas.setParent(self.ui.errorPlotContainer)

        layout2 = QVBoxLayout(self.ui.errorPlotContainer)
        layout2.addWidget(self.error_canvas)

    def connect_signals(self):
        self.ui.startButton.clicked.connect(self.on_manual_input)   # Главная страница
        self.ui.loadButton.clicked.connect(self.on_load_file)
        self.ui.randomButton.clicked.connect(self.on_random_generate)
        self.ui.aboutButton.clicked.connect(self.on_about)

        self.ui.backButton_1.clicked.connect(self.on_back_to_menu)   # Ввода данных
        self.ui.nextButton_1.clicked.connect(self.submit_entered_data)

        self.ui.backButton_2.clicked.connect(self.on_back_to_menu)   # О программе

        self.ui.backButton_4.clicked.connect(self.on_back_to_input)   # Параметры алгоритма
        self.ui.nextButton_3.clicked.connect(self.submit_algorithm_params)

        self.ui.backButton_3.clicked.connect(self.on_back_to_params)   # Выполнение алгоритма
        self.ui.backButton_5.clicked.connect(self.on_prev_generation)
        self.ui.nextButton_4.clicked.connect(self.on_next_generation)
        self.ui.inEndButton.clicked.connect(self.on_go_to_end)
        self.ui.lineEdit.returnPressed.connect(self.on_go_to_generation)
        self.ui.lineEdit_2.returnPressed.connect(self.on_go_to_individual)

    def on_manual_input(self):
        self.ui.stackedWidget.setCurrentIndex(2)

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

                    self.ui.sizePopulSpinBox.setValue(config.population_size)   # Поля параметров алгоритма
                    self.ui.numPopulSpinBox.setValue(config.generations)
                    self.ui.mutationsDoubleSpinBox.setValue(config.mutation_chance)
                    self.ui.crossoverDoubleSpinBox.setValue(config.crossover_chance)

                print(f"Загружена задача: {task_data}")
                print(f"Параметры ГА: {self.ga_config}")

                self.ui.stackedWidget.setCurrentIndex(3)

            except Exception as e:
                QMessageBox.critical(self.window, "Ошибка", f"Не удалось загрузить файл:\n{str(e)}")

    def on_random_generate(self):
        self.current_task = self.data_manager.generate_random_task()
        print(f"Сгенерирована случайная задача: {self.current_task}")

        coefs = self.current_task['polynom']   # Поля ввода
        self.ui.degSpinBox.setValue(len(coefs) - 1)
        self.ui.coefLineEdit.setText(' '.join(map(str, coefs)))
        self.ui.beginnigIntSpinBox.setValue(int(self.current_task['interval'][0]))
        self.ui.endIntSpinBox.setValue(int(self.current_task['interval'][1]))
        self.ui.stepsSpinBox.setValue(self.current_task['steps'])

        self.ui.stackedWidget.setCurrentIndex(3)

    def on_about(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_back_to_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_back_to_input(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_back_to_params(self):
        self.ui.stackedWidget.setCurrentIndex(3)

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
            print("Данные задачи приняты")
            self.ui.stackedWidget.setCurrentIndex(3)

        except ValueError:
            QMessageBox.critical(self.window, "Ошибка", "Коэффициенты должны быть числами, "
                                                        "разделенными пробелами")

    def submit_algorithm_params(self):
        self.ga_config.population_size = self.ui.sizePopulSpinBox.value()
        self.ga_config.generations = self.ui.numPopulSpinBox.value()
        self.ga_config.mutation_chance = self.ui.mutationsDoubleSpinBox.value()
        self.ga_config.crossover_chance = self.ui.crossoverDoubleSpinBox.value()

        self.ga_config.validate()

        print(f"Параметры алгоритма: {self.ga_config}")

        self.run_algorithm()

    def run_algorithm(self):
        if not self.current_task:
            QMessageBox.warning(self.window, "Ошибка", "Сначала задайте параметры задачи")
            return

        polynom = Polynom(self.current_task['polynom'])
        l, r = self.current_task['interval']
        steps = self.current_task['steps']

        self.ga = GeneticAlgorithm(polynom, l, r, steps, self.ga_config)
        self.ga.init_population()
        self.current_generation = 0
        self.current_individual = 0

        self.ui.stackedWidget.setCurrentIndex(4)
        self.update_display()

    def on_next_generation(self):
        if not self.ga: return
        finish_flag = False
        if self.current_generation < self.ga.curr_generation:
            self.current_generation += 1
            self.current_individual = 0
            self.update_display()
            if self.current_generation == self.ga_config.generations: finish_flag = True
        elif self.ga.curr_generation < self.ga_config.generations:
            self.ga.generation_step()
            self.current_generation += 1
            self.current_individual = 0
            self.update_display()
            if self.current_generation == self.ga_config.generations: finish_flag = True

        if finish_flag: self.show_best_solution()

    def on_prev_generation(self):
        if self.ga and self.current_generation > 0:
            self.current_generation -= 1
            self.current_individual = 0
            self.update_display()

    def on_go_to_end(self):
        if not self.ga: return
        if self.current_generation == self.ga_config.generations: return
        while self.ga.curr_generation < self.ga_config.generations: self.ga.generation_step()
        self.current_generation = self.ga.curr_generation
        self.current_individual = 0
        self.update_display()
        self.show_best_solution()

    def on_go_to_generation(self):  # К конкретному поколению
        if not self.ga: return
        try:
            gen_num = int(self.ui.lineEdit.text())
            if 0 <= gen_num <= self.ga_config.generations:
                while self.ga.curr_generation < gen_num: self.ga.generation_step()
                self.current_generation = gen_num
                self.current_individual = 0
                self.update_display()
                self.ui.lineEdit.clear()
                if self.current_generation == self.ga_config.generations: self.show_best_solution()
            else:
                QMessageBox.warning(self.window, "Ошибка",
                                    f"Введите номер поколения от 0 до {self.ga_config.generations}")
        except ValueError:
            QMessageBox.warning(self.window, "Ошибка", "Введите число")

    def on_go_to_individual(self):  # К конкретному индивиду
        if self.ga:
            try:
                ind_num = int(self.ui.lineEdit_2.text())
                if 0 <= ind_num < self.ga_config.population_size:
                    self.current_individual = ind_num
                    self.update_display()
                    self.ui.lineEdit_2.clear()
                else:
                    QMessageBox.warning(self.window, "Ошибка",
                                        f"Введите номер индивида от 0 до {self.ga_config.population_size - 1}")
            except ValueError:
                QMessageBox.warning(self.window, "Ошибка", "Введите число")

    def update_display(self):
        if not self.ga: return
        state = self.ga.history[self.current_generation]
        self.ui.generationNum.setText(str(self.current_generation))
        self.ui.bestMistake.setText(f"{state['best_fitness']:.4f}")
        self.update_function_plot(state)
        self.update_error_plot()

    def update_function_plot(self, state):
        self.function_figure.clear()
        ax = self.function_figure.add_subplot()

        polynom = self.ga.polynom
        l, r = self.ga.l, self.ga.r

        x_vals = []
        y_poly = []
        y_step = []
        if self.current_individual < len(state['population']):
            heights = state['population'][self.current_individual]
            step_func = StepFunc(heights, l, r)
            dots = 1000
            step = (r - l) / dots
            for i in range(dots + 1):
                x = l + i * step
                x_vals.append(x)
                y_poly.append(polynom.value_at_point(x))
                y_step.append(step_func.value_at_point(x))

            ax.plot(x_vals, y_poly, label = 'f(x)', color = 'blue')
            ax.plot(x_vals, y_step, label = 'g(x)', color = 'red')

        ax.set_title(f'Поколение {self.current_generation}, Индивид {self.current_individual}')
        ax.legend(loc='lower right')
        ax.grid()

        self.function_canvas.draw()

    def update_error_plot(self):
        self.error_figure.clear()
        ax = self.error_figure.add_subplot()

        max_fitnesses = [state['best_fitness'] for state in self.ga.history]
        avg_fitnesses = [state['avg_fitness'] for state in self.ga.history]
        generations = range(len(max_fitnesses))

        ax.plot(generations, max_fitnesses, label = 'Max', color = 'green')
        ax.plot(generations, avg_fitnesses, label = 'Avg', color = 'purple')

        ax.set_ylabel('Приспособленность')
        ax.set_title('Изменение приспособленности')
        ax.legend(loc='lower right')
        ax.grid()

        self.error_canvas.draw()

    def show_best_solution(self):
        state = self.ga.history[-1]
        best_fitness = state['best_fitness']
        best_genotype = state['best_genotype']
        best_index = state['population'].index(best_genotype)
        if self.current_individual != best_index:
            self.current_individual = best_index
            self.update_display()

        message = ("Работа алгоритма завершена.\n"
                   f"Номер лучшего индивида: {best_index}\n"
                   f"Лучшая приспособленность: {round(best_fitness, 4)}\n")

        message_box = QMessageBox(self.window)
        message_box.setWindowTitle("Лучшее приближение")
        message_box.setText(message)
        message_box.exec()

    def run(self):
        self.window.show()