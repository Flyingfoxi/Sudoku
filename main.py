# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:34:14 2023

Coded by Foxispythonlab
"""

############################ --- Imports --- ##################################

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
    QPushButton,
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
    def __init__(self, config: dict, sudoku: dict, solution: dict, parent: QMainWindow = None, difficulty = "medium"):
        super().__init__(parent)
        self.parent = parent

        self.setWindowTitle('Sudoku - Visualizer')
        self.setGeometry(0, 0, 800, 800)

        self.size = abs((800 * 800) / 10000)

        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 75, 75, 75))

        nums = [0, 1, 2, 4, 5, 6, 8, 9, 10]
        letters = [i for i in 'ABCDEFGHI']
        self.translation_to_letters = {int(nums[i]): letters[i] for i in range(len(nums))}
        self.auto_commit = (config["auto-commit"] == "True")
        self.config = config

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
                            if self.auto_commit:
                                sudoku_display[f"{row}{collum}"].textChanged.connect(self.check)
                        else:
                            sudoku_display[f"{row}{collum}"] = QLabel(sudoku[f"{row}{collum}"])
                            sudoku_display[f"{row}{collum}"].setStyleSheet("color: #000000 ; font-weight: bold ")
                        layout.addWidget(sudoku_display[f"{row}{collum}"], ord(row.lower()) - (96 - modr),
                                         int(collum) + modc,
                                         Qt.AlignmentFlag.AlignCenter)
                        
        if not self.auto_commit:
            self.commit = QPushButton("Prüfen")
            self.commit.clicked.connect(self.check)
            layout.addWidget(self.commit, 12, 1, 1, 10, Qt.AlignmentFlag.AlignCenter)

        layout.addItem(QSpacerItem(25, 10), 0, 3)
        layout.addItem(QSpacerItem(25, 10), 0, 7)
        layout.addItem(QSpacerItem(10, 25), 3, 0)
        layout.addItem(QSpacerItem(10, 25), 7, 0)

        self.trys = config["trys"][difficulty]
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
                if '-' not in field.text():
                    if field.text() in nums:
                        pos = self.layout().getItemPosition(self.layout().indexOf(field))

                        num: str = field.text()
                        row = self.translation_to_letters[pos[0]]
                        collum = (pos[1] + 1 if pos[1] < 3 else pos[1] if pos[1] < 7 else pos[1] - 1)

                        if self.sudoku_solution[f"{row}{collum}"] == num:
                            field.hide()
                            self.sudoku_display[key] = QLabel(num)

                            self.getsize()
                            self.sudoku_display[key].setFont(self.create_font(int(5 + (self.size + 1.25))))
                            # noinspection PyArgumentList
                            self.layout().addWidget(self.sudoku_display[key],
                                                    pos[0], pos[1], 1, 1, Qt.AlignmentFlag.AlignCenter)
                        else:
                            self.trys -= 1
                            field.setText('')
                            print('Trys left: ', self.trys)
                            if self.trys == 0:
                                [obj.setReadOnly(True) for obj in self.sudoku_display.values() if isinstance(obj, QLineEdit)]
                                self.parent.failed()

                    else:
                        field.setText('')

        if not any([(False if isinstance(field, QLabel) else True) for field in self.sudoku_display.values()]):
            [obj.setEnabled(False) for obj in self.sudoku_display if isinstance(obj, QLineEdit)]
            self.parent.completed()

    def paintEvent(self, event):
        pen = QPainter()
        pen.begin(self)

        pen_style = QPen()
        pen_style.setWidth(int(self.size / 5 + 1))
        pen.setPen(pen_style)

        pen_fine = QPen()
        pen_fine.setWidth(1)

        w = self.geometry().width()
        h = self.geometry().height()

        if self.auto_commit:
            pen.drawLine(int(w / 3) + 20, 75, int(w / 3) + 20, h - 75)
            pen.drawLine(int(w / 3) * 2 - 20, 75, int(w / 3) * 2 - 20, h - 75)
            pen.drawLine(75, int(h / 3) + 20, w - 75, int(h / 3) + 20)
            pen.drawLine(75, int(h / 3) * 2 - 20, w - 75, int(h / 3) * 2 - 20)
        else:
            pen.drawLine(int(w / 3) + 20, 75, int(w / 3) + 20, h - 125)
            pen.drawLine(int(w / 3) * 2 - 20, 75, int(w / 3) * 2 - 20, h - 125)
            pen.drawLine(75, int(h / 3), w - 75, int(h / 3))
            pen.drawLine(75, int(h / 3) * 2 - 50, w - 75, int(h / 3) * 2 - 50)
            pen.end()

    def getsize(self):
        w = self.geometry().width()
        h = self.geometry().height()

        self.size = abs(int((w - 150 * h - 150) / 10000))
        return w, h

    def resizeEvent(self, event):
        w, h = self.getsize()

        for field in self.sudoku_display.values():
            field.setFont(self.create_font(int(self.size * 1.25 + 5)))
            field.setFixedSize(int((w - 150) / 12), int((h - 150) / 15))
            field.setAlignment(Qt.AlignmentFlag.AlignCenter)
           
    def create_font(self, size=10):
        font = QFont(self.config["font_type"])
        font.setPointSize(int(size))
        return font


class Sudoku_HomeScreen(QWidget):
    def __init__(self, parent: QMainWindow, standart_difficulty, font_type):
        super().__init__(parent)
        self.parent = parent
        self.font_type = font_type

        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 50, 50, 50))

        self.i = {}

        self.titel = QLabel('Sudoku')

        self.i['bu_create'] = QPushButton('Create Sudoku')
        self.i['bu_create'].clicked.connect(getattr(self.parent, f"create_{standart_difficulty}"))

        self.i['bu_load'] = QPushButton('Load latest Sudoku')
        self.i['bu_load'].clicked.connect(self.parent.load_sudoku)

        self.i['bu_statistics'] = QPushButton('Show Statistics')
        self.i['bu_statistics'].clicked.connect(self.parent.show_statistics)

        layout.addWidget(self.titel, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.i['bu_create'], 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.i['bu_load'], 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.i['bu_statistics'], 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.resizeEvent(1)

    def resizeEvent(self, event):
        w = self.geometry().width()
        h = self.geometry().height()
        size = abs(int((w - 150 * h - 150) / 10000))

        font1 = self.create_font(int(5 + size * 2))
        font2 = self.create_font(int(20 + size * 10))

        [self.i[pos].setFont(font1) for pos in self.i.keys()]
        self.titel.setFont(font2)

    def create_font(self, size=10):
        font = QFont(self.font_type)
        font.setPointSize(int(size))
        return font


class Sudoku_StatisticsView(QWidget):
    def __init__(self, statistics: dict, parent: QMainWindow, font_type):
        super().__init__(parent)
        self.parent = parent
        self.font_type = font_type

        layout = QGridLayout()
        layout.setContentsMargins(QMargins(100, 50, 100, 50))

        self.titel = QLabel("Statistics")
        layout.addWidget(self.titel, 0, 0, 1, 7, Qt.AlignmentFlag.AlignCenter)

        content = dict(); row = 2
        for stat in ["easy", "medium", "hard", "master", "total"]:
            content[stat+'l'] = QLabel(stat)
            content[stat+'n'] = QLabel(str(statistics[stat]))
            layout.addWidget(content[stat+'l'], row, 1, 1, 1)
            layout.addWidget(content[stat+'n'], row, 5, 1, 1, Qt.AlignmentFlag.AlignCenter)
            row += 1
        self.content = content

        self.setLayout(layout)

    def resizeEvent(self, event):
        w = self.geometry().width()
        h = self.geometry().height()
        size = abs(int((w - 150 * h - 150) / 10000))

        font1 = self.create_font(int(5 + size * 2))
        font2 = self.create_font(int(10 + size * 10))

        [self.content[pos].setFont(font1) for pos in self.content.keys()]
        self.titel.setFont(font2)

    def create_font(self, size=14):
        font = QFont(self.font_type)
        font.setPointSize(int(size))
        return font
    

class Sudoku_SettingsView(QWidget):
    def __init__(self, parent = None):
        super().__init__(self, parent)
    

class Sudoku_Messager(QWidget):
    def __init__(self, parent, titel_message, message, font_type):
        super().__init__()

        self.setWindowTitle('Sudoku - v1.0 Alpha')
        self.setGeometry(100, 100, 400, 250)
        self.show()

        self.parent = parent
        self.font_type = font_type

        layout = QGridLayout()

        titel = QLabel("Sudoku")
        titel.setFont(self.create_font())
        layout.addWidget(titel, 0, 0, Qt.AlignmentFlag.AlignCenter)

        main_message = QLabel(titel_message)
        main_message.setFont(self.create_font(size=24, bold = True))
        layout.addWidget(main_message, 1, 0, Qt.AlignmentFlag.AlignCenter)

        message = QLabel(message)
        message.setWordWrap(True)
        message.setFont(self.create_font(10))
        layout.addWidget(message, 2, 0, Qt.AlignmentFlag.AlignCenter)

        close = QPushButton("close")
        close.clicked.connect(self.close)
        layout.addWidget(close, 3, 0, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def close(self):
        self.destroy()

    def create_font(self, size=14, bold = False):
        font = QFont(self.font_type)
        font.setPointSize(int(size))
        font.setBold(bold)
        return font


class Sudoku_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sudoku - v1.0 Alpha')
        self.setGeometry(0, 0, 1100, 800)

        self.generator = Sudoku_Generator()
        self.setup = Sudoku_Settings()
        self.mws = self.setup.setup_mainwin()
        self.wis = self.setup.setup_widget()
        self.statistics = Sudoku_Statistics(self.setup.config, self.setup.dir)
        
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
        create_master = QAction('Master Mode', self)

        create_easy.triggered.connect(self.create_easy)
        create_medium.triggered.connect(self.create_medium)
        create_hard.triggered.connect(self.create_hard)
        create_master.triggered.connect(self.create_master)

        account_login = QAction('Login', self)
        account_login.setStatusTip('Login or Create a Account for free to save your statistics')

        account_logout = QAction('Logout', self)

        home = QAction('Home', self)
        home.setStatusTip('Returns to the starting Padge')
        home.triggered.connect(self.home)

        statistics_show = QAction('Show Statistics', self)
        statistics_show.setStatusTip('Let your take a look over your Statistics')
        statistics_show.triggered.connect(self.show_statistics)

        menu_sudoku_create.addActions((create_easy, create_medium, create_hard, create_master))
        menu_file.addActions((account_login, account_logout, home))
        menu_sudoku.addSeparator()
        menu_sudoku.addActions((save, load))
        menu_statistics.addAction(statistics_show)

    def failed(self):
        self.message = Sudoku_Messager(self, "Try Again",
                                       "You used to many false trys", self.mws["font_type"])

    def home(self):
        self.active_widget = Sudoku_HomeScreen(self, self.mws["standart_difficulty"], self.mws["font_type"])
        self.setCentralWidget(self.active_widget)

    def save_sudoku(self):
        if isinstance(self.active_widget, Sudoku_Widget):
            with open('Latest_Sudoku.json', 'w') as f:
                values = [dict(), self.active_widget.sudoku_solution, self.difficulty]
                for field in self.active_widget.sudoku_display.keys():
                    values[0][field] = self.active_widget.sudoku_display[field].text()
                json.dump(values, f, indent = 1)

    def load_sudoku(self):
        try:
            with open('Latest_Sudoku.json', 'r') as f:
                sudoku, solution, self.difficulty = json.load(f)
                self.active_widget = Sudoku_Widget(self.wis, sudoku, solution, self, self.difficulty)
                self.setCentralWidget(self.active_widget)
        except FileNotFoundError:
            return 'E1'

    def completed(self):
        if not isinstance(self.active_widget, Sudoku_Widget):
            return
        self.statistics.add_statistics(self.difficulty)
        self.message = Sudoku_Messager(self, "Gratulations", "You sucessfully completet the Sudoku.",
                                       self.mws["font_type"])

    def show_statistics(self):
        stats = {index: self.statistics.get_statistics(index) for index in ["easy", "medium", "hard", "master", "total"]}
        self.active_widget = Sudoku_StatisticsView(stats, self, self.mws["font_type"])
        self.setCentralWidget(self.active_widget)

    def create_easy(self):
        # Reset to -E for normal games, -S is for developing reasons (very easy)
        self.difficulty = 'easy'
        sudoku, solution = self.generator.play(True, '-E')
        self.active_widget = Sudoku_Widget(self.wis, sudoku, solution, self, self.difficulty)
        self.setCentralWidget(self.active_widget)

    def create_medium(self):
        self.difficulty = 'medium'
        sudoku, solution = self.generator.play(True, '-M')
        self.active_widget = Sudoku_Widget(self.wis, sudoku, solution, self, self.difficulty)
        self.setCentralWidget(self.active_widget)
        
    def create_hard(self):
        self.difficulty = 'hard'
        sudoku, solution = self.generator.play(True, '-S')
        self.active_widget = Sudoku_Widget(self.wis, sudoku, solution, self, self.difficulty)
        self.setCentralWidget(self.active_widget)
        
    def create_master(self):
        self.difficulty = 'master'
        sudoku, solution = self.generator.play(True, '-I')
        self.active_widget = Sudoku_Widget(self.wis, sudoku, solution, self, self.difficulty)
        self.setCentralWidget(self.active_widget)
        

class Sudoku_Statistics:
    def __init__(self, config: dict, sdir):
        self.st_path = config["paths"]["statistics"]
        self.dir = sdir

    def get_statistics(self, typ: str):
        try:
            with open(os.path.join(self.dir + self.st_path), 'r') as f:
                self.statistics = json.load(f)
                return self.statistics[typ]
        except FileNotFoundError:
            raise 'E2'

    def add_statistics(self, typ: str, value: int = 1):
        if typ in ["easy", "medium", "hard", "master"]:
            self.add_statistics("total", value)
        self.get_statistics("total")
        with open(os.path.join(self.dir, self.st_path), 'w') as f:
            self.statistics[typ] += value
            json.dump(self.statistics, f, indent = 1)


class Sudoku_Settings:
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
    
    def setup_mainwin(self):
        return self.config["setup"]["window"]
    
    def setup_widget(self):
        return self.config["setup"]["widget"]
    
    def setup_generator(self):
        return self.config["setup"]["generator"]


######################### --- Main Programm --- ###############################


if __name__ == '__main__':

    app = QApplication([])
    mainwin = Sudoku_Window()
    mainwin.show()
    app.exec()

else:
    print('loaded Sudoku module form Foxispythonlab')
