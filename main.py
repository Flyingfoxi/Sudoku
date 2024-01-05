# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:34:14 2023

Coded by Foxispythonlab
"""

############################ --- Importe --- ##################################

import os, json
from Sudoku_Generator import Sudoku_Generator
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QSpacerItem,
    QLabel,
    QLineEdit,
    QGridLayout,
    QMainWindow,
    QPushButton
)

from PyQt6.QtCore import (
    Qt,
    QMargins,
)

from PyQt6.QtGui import (
    QPainter,
    QPen,
    QAction,
    QFont
)


######################### --- Inizializing --- ################################


class Sudoku_Widget(QWidget):
    def __init__(self, sudoku: dict, solution: dict, parent: QWidget = None):
        super().__init__(parent)
        self.parent = parent

        self.setWindowTitle('Sudoku - Visualizer')
        self.setGeometry(0, 0, 800, 500)

        self.size = abs((650 * 350) / 10000)

        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 75, 75, 75))

        nums = [0, 1, 2, 4, 5, 6, 8, 9, 10]
        letters = [i for i in 'ABCDEFGHI']
        self.translation_to_letters = {int(nums[i]): letters[i] for i in range(len(nums))}

        sudoku_display = {}
        modr = -2

        for rowblock in ['ABC', 'DEF', 'GHI']:
            modr += 1
            for row in [i for i in rowblock]:
                modc = -2
                for collumblock in ['123', '456', '789']:
                    modc += 1
                    for collum in [i for i in collumblock]:
                        if not sudoku[f"{row}{collum}"] in [str(num) for num in range(1, 10)]:
                            # noinspection PyTypedDict
                            sudoku_display[f"{row}{collum}"] = QLineEdit()
                            sudoku_display[f"{row}{collum}"].setText(
                                (sudoku[f"{row}{collum}"] if sudoku[f"{row}{collum}"] != ' ' else ''))
                            sudoku_display[f"{row}{collum}"].textChanged.connect(self.check)

                        else:
                            sudoku_display[f"{row}{collum}"] = QLabel(sudoku[f"{row}{collum}"])
                        layout.addWidget(sudoku_display[f"{row}{collum}"], ord(row.lower()) - (96 - modr),
                                         int(collum) + modc,
                                         Qt.AlignmentFlag.AlignCenter)

        layout.addItem(QSpacerItem(25, 10), 0, 3)
        layout.addItem(QSpacerItem(25, 10), 0, 7)
        layout.addItem(QSpacerItem(10, 25), 3, 0)
        layout.addItem(QSpacerItem(10, 25), 7, 0)

        self.trys = 5
        self.sudoku_display = sudoku_display.copy()
        self.sudoku_to_solve = sudoku
        self.sudoku_solution = solution

        self.setLayout(layout)

    def check(self):
        self.resizeEvent([])
        nums = [str(i) for i in range(1, 10)]
        for key in self.sudoku_display.keys():
            field = self.sudoku_display[key]
            if isinstance(field, QLineEdit):
                if True:
                    if field.text() in nums:
                        pos = self.layout().getItemPosition(self.layout().indexOf(field))

                        num: str = field.text()
                        row = self.translation_to_letters[pos[0]]
                        collum = (pos[1] + 1 if pos[1] < 3 else pos[1] if pos[1] < 7 else pos[1] - 1)

                        if self.sudoku_solution[f"{row}{collum}"] == num:
                            field.hide()
                            self.sudoku_display[key] = QLabel(num)

                            self.getsize()
                            self.sudoku_display[key].setFont(self.create_font('Times', int(5 + (self.size + 1.25))))
                            # noinspection PyArgumentList
                            self.layout().addWidget(self.sudoku_display[key],
                                                    pos[0], pos[1], 1, 1, Qt.AlignmentFlag.AlignCenter)
                        else:
                            self.trys -= 1
                            print('You used all trys up' if self.trys <= 0
                                  else f"Wrong, your used a try, you have {self.trys} left")

                    else:
                        field.setText('')
        if not any([(True if isinstance(field, QLabel) else False) for field in self.sudoku_display.values()]):
            self.parent.completed()

    def paintEvent(self, event):
        pen = QPainter()
        pen.begin(self)

        pen_style = QPen()
        pen_style.setWidth(int(self.size / 5 + 1))
        pen.setPen(pen_style)

        w = self.geometry().width()
        h = self.geometry().height()

        pen.drawLine(int(w / 3) + 20, 75, int(w / 3) + 20, h - 75)
        pen.drawLine(int(w / 3) * 2 - 20, 75, int(w / 3) * 2 - 20, h - 75)
        pen.drawLine(75, int(h / 3) + 20, w - 75, int(h / 3) + 20)
        pen.drawLine(75, int(h / 3) * 2 - 20, w - 75, int(h / 3) * 2 - 20)

        pen.end()

    def getsize(self):
        w = self.geometry().width()
        h = self.geometry().height()

        self.size = abs(int((w - 150 * h - 150) / 10000))
        return w, h

    def resizeEvent(self, event):
        w, h = self.getsize()

        for field in self.sudoku_display.values():
            field.setFont(self.create_font('Times', int(self.size * 1.25 + 5)))
            field.setFixedSize(int((w - 150) / 12), int((h - 150) / 15))
            field.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def create_font(self, style: str, size=10):
        font = QFont(style)
        font.setPointSize(int(size))
        return font


class Sudoku_HomeScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 50, 50, 50))

        titel = QLabel('Sudoku')
        titel.setFont(self.create_font('Times', 48))

        bu_create = QPushButton('Create Sudoku')
        bu_create.clicked.connect(self.create_medium)
        bu_create.setFont(self.create_font('Times', 14))

        bu_load = QPushButton('Load latest Sudoku')
        bu_load.clicked.connect(self.load_sudoku)
        bu_load.setFont(self.create_font('Times', 14))

        bu_statistics = QPushButton('Show Statistics')
        bu_statistics.setFont(self.create_font('Times', 14))

        layout.addWidget(titel, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_create, 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_load, 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_statistics, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.active_widget = QWidget()
        self.active_widget.setLayout(layout)
        self.setCentralWidget(self.active_widget)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sudoku - v1.0 Alpha')
        self.setGeometry(0, 0, 800, 500)

        self.generator = Sudoku_Generator()
        self.statistics = Sudoku_Statistics()

        self._init_menubar()
        self.home()

    def _init_menubar(self):
        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_sudoku = menu.addMenu('Sudoku')
        menu_sudoku_create = menu_sudoku.addMenu('Create')
        menu_statistics = menu.addMenu('Statistics')

        save = QAction('Save', self)
        save.triggered.connect(self.save_sudoku)
        save.setStatusTip('This Saves your current Sudoku to finish it later')

        load = QAction('Load', self)
        load.triggered.connect(self.load_sudoku)
        load.setStatusTip('This loads already saved Sudoku, to finish them')

        create_easy = QAction('Easy', self)
        create_medium = QAction('Medium', self)
        create_hard = QAction('Hard', self)

        create_easy.triggered.connect(self.create_easy)
        create_medium.triggered.connect(self.create_medium)
        create_hard.triggered.connect(self.create_hard)

        account_login = QAction('Login', self)
        account_login.setStatusTip('Login or Create a Account for free to save your statistics')

        account_logout = QAction('Logout', self)

        home = QAction('Home', self)
        home.setStatusTip('Returns to the starting Padge')
        home.triggered.connect(self.home)

        statistics_show = QAction('Show Statistics', self)
        statistics_show.setStatusTip('Let your take a look over your Statistics')

        menu_sudoku_create.addActions((create_easy, create_medium, create_hard))
        menu_file.addActions((account_login, account_logout, home))
        menu_sudoku.addSeparator()
        menu_sudoku.addActions((save, load))
        menu_statistics.addAction(statistics_show)

    def save_sudoku(self):
        if isinstance(self.active_widget, Sudoku_Widget):
            with open('Latest_Sudoku.json', 'w') as f:
                values = [dict(), self.active_widget.sudoku_solution]
                for field in self.active_widget.sudoku_display.keys():
                    values[0][field] = self.active_widget.sudoku_display[field].text()
                json.dump(values, f, indent = 1)

    def load_sudoku(self):
        try:
            with open('Latest_Sudoku.json', 'r') as f:
                sudoku, solution = json.load(f)
                self.active_widget = Sudoku_Widget(sudoku, solution)
                self.setCentralWidget(self.active_widget)
        except FileNotFoundError:
            return 'E1'

    def home(self):
        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 50, 50, 50))

        titel = QLabel('Sudoku')
        titel.setFont(self.create_font('Times', 48))

        bu_create = QPushButton('Create Sudoku')
        bu_create.clicked.connect(self.create_medium)
        bu_create.setFont(self.create_font('Times', 14))

        bu_load = QPushButton('Load latest Sudoku')
        bu_load.clicked.connect(self.load_sudoku)
        bu_load.setFont(self.create_font('Times', 14))

        bu_statistics = QPushButton('Show Statistics')
        bu_statistics.setFont(self.create_font('Times', 14))

        layout.addWidget(titel, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_create, 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_load, 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_statistics, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.active_widget = QWidget()
        self.active_widget.setLayout(layout)
        self.setCentralWidget(self.active_widget)

    def completed(self, difficulty):
        if not isinstance(self.active_widget, Sudoku_Widget):
            return

        difficulty_index = ("easy" if difficulty == '-E' else "medium" if difficulty == '-M' else "hard")
        self.statistics.add_statistics(difficulty_index)
        self.home()

    def update_statistics(self):
        self.statistics.add_statistics("easy")

    def create_easy(self):
        sudoku, solution = self.generator.play(True, '-E')
        self.active_widget = Sudoku_Widget(sudoku, solution, self)
        self.setCentralWidget(self.active_widget)
        self.difficulty = 'easy'

    def create_medium(self):
        sudoku, solution = self.generator.play(True, '-M')
        self.active_widget = Sudoku_Widget(sudoku, solution, self)
        self.setCentralWidget(self.active_widget)
        self.difficulty = 'medium'

    def create_hard(self):
        sudoku, solution = self.generator.play(True, '-S')
        self.active_widget = Sudoku_Widget(sudoku, solution, self)
        self.setCentralWidget(self.active_widget)
        self.difficulty = 'hard'

    def create_font(self, style: str = 'Times', size=10):
        font = QFont(style)
        font.setPointSize(int(size))
        return font


class Sudoku_Statistics:
    def __init__(self):
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                self.config = json.load(f)
                self.dir = ""
        else:
            path_to_user = os.path.expanduser('~')
            path_to_dir = "Appdata\\Local\\Programms\\Sudoku"
            self.dir = os.path.join(path_to_user, path_to_dir)
            if os.path.exists(os.path.join(self.dir, "config.json")):
                with open(os.path.join(self.dir, "config.json")) as f:
                    self.config = json.load(f)
            else:
                raise RuntimeError("Can't find config file")

        self.st_path = self.config['paths']['statistics']

    def get_statistics(self, typ: str):
        try:
            with open(os.path.join(self.dir + self.st_path), 'r') as f:
                self.statistics = json.load(f)
                return self.statistics[typ]
        except FileNotFoundError:
            raise 'E2'

    def add_statistics(self, typ: str, value: int = 1):
        if typ in ["easy", "medium", "hard"]:
            self.add_statistics("games_finished", value)
        self.get_statistics("games_finished")
        with open(os.path.join(self.dir, self.st_path), 'w') as f:
            self.statistics[typ] += value
            json.dump(self.statistics, f, indent = 1)
        print(self.statistics)


######################### --- Main Programm --- ###############################


if __name__ == '__main__':

    app = QApplication([])
    mainwin = Window()
    mainwin.show()
    app.exec()

else:
    print('loaded Sudoku module form Foxispythonlab')
