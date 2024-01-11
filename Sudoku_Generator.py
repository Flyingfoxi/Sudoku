# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:34:14 2023

Coded by Foxispythonlab
"""

import random


class Sudoku_Generator:
    def __init__(self):
        self.A1 = self.A2 = self.A3 = self.A4 = self.A5 = self.A6 = self.A7 = self.A8 = self.A9 = ' '
        self.B1 = self.B2 = self.B3 = self.B4 = self.B5 = self.B6 = self.B7 = self.B8 = self.B9 = ' '
        self.C1 = self.C2 = self.C3 = self.C4 = self.C5 = self.C6 = self.C7 = self.C8 = self.C9 = ' '

        self.D1 = self.D2 = self.D3 = self.D4 = self.D5 = self.D6 = self.D7 = self.D8 = self.D9 = ' '
        self.E1 = self.E2 = self.E3 = self.E4 = self.E5 = self.E6 = self.E7 = self.E8 = self.E9 = ' '
        self.F1 = self.F2 = self.F3 = self.F4 = self.F5 = self.F6 = self.F7 = self.F8 = self.F9 = ' '

        self.G1 = self.G2 = self.G3 = self.G4 = self.G5 = self.G6 = self.G7 = self.G8 = self.G9 = ' '
        self.H1 = self.H2 = self.H3 = self.H4 = self.H5 = self.H6 = self.H7 = self.H8 = self.H9 = ' '
        self.I1 = self.I2 = self.I3 = self.I4 = self.I5 = self.I6 = self.I7 = self.I8 = self.I9 = ' '

    def __dict__(self):
        return {f"{row}{num}": str(getattr(self, f"{row}{num}")) for row in "ABCDEFGHI" for num in range(1, 10)}

    def generate(self):
        self.__init__()
        for i in range(0, 25):
            self.rows = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9']
            for row in self.rows:

                if row == 'A1':
                    self.row_count = 1
                    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    random.shuffle(nums)
                    self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9 = nums

                elif row == 'I9':
                    self.row_count = 9
                    self.collums = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
                    for cell in self.collums:
                        exec(f"collum = [self.A{cell[1]}, self.B{cell[1]}, self.C{cell[1]},"
                             f" self.D{cell[1]}, self.E{cell[1]}, self.F{cell[1]}, self.G{cell[1]},"
                             f" self.H{cell[1]}, self.I{cell[1]}]")
                        exec(f"self.{cell} = self.generate_collum(collum)")

                else:
                    self.row_count = int(row[1])
                    self.row_name = row[0]
                    exec("self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5,"
                         "self.Cell6, self.Cell7, self.Cell8, self.Cell9 = "
                         f"self.{row[0]}1, self.{row[0]}2, self.{row[0]}3,"
                         f" self.{row[0]}4, self.{row[0]}5, self.{row[0]}6, "
                         f" self.{row[0]}7, self.{row[0]}8, self.{row[0]}9")
                    for _ in range(250):
                        if self.generate_row():
                            break

            dictionary = self.__dict__()
            if not any([(True if field == ' ' else False) for field in dictionary.values()]):
                return dictionary
            else:
                self.__init__()
        raise RuntimeError("Sudoku can't be generated")

    def generate_var(self):
        self.row = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8,
                    self.Cell9]

        self.row_miss = []

        if '1' not in self.row:
            self.row_miss += '1'
        if '2' not in self.row:
            self.row_miss += '2'
        if '3' not in self.row:
            self.row_miss += '3'
        if '4' not in self.row:
            self.row_miss += '4'
        if '5' not in self.row:
            self.row_miss += '5'
        if '6' not in self.row:
            self.row_miss += '6'
        if '7' not in self.row:
            self.row_miss += '7'
        if '8' not in self.row:
            self.row_miss += '8'
        if '9' not in self.row:
            self.row_miss += '9'

        random.shuffle(self.row_miss)

        self.collum9 = (self.A9, self.B9, self.C9, self.D9, self.E9, self.F9, self.G9, self.H9, self.I9)
        self.collum8 = (self.A8, self.B8, self.C8, self.D8, self.E8, self.F8, self.G8, self.H8, self.I8)
        self.collum7 = (self.A7, self.B7, self.C7, self.D7, self.E7, self.F7, self.G7, self.H7, self.I7)
        self.collum6 = (self.A6, self.B6, self.C6, self.D6, self.E6, self.F6, self.G6, self.H6, self.I6)
        self.collum5 = (self.A5, self.B5, self.C5, self.D5, self.E5, self.F5, self.G5, self.H5, self.I5)
        self.collum4 = (self.A4, self.B4, self.C4, self.D4, self.E4, self.F4, self.G4, self.H4, self.I4)
        self.collum3 = (self.A3, self.B3, self.C3, self.D3, self.E3, self.F3, self.G3, self.H3, self.I3)
        self.collum2 = (self.A2, self.B2, self.C2, self.D2, self.E2, self.F2, self.G2, self.H2, self.I2)
        self.collum1 = (self.A1, self.B1, self.C1, self.D1, self.E1, self.F1, self.G1, self.H1, self.I1)

        self.sqare1 = (self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3)
        self.sqare2 = (self.A4, self.A5, self.A5, self.B4, self.B5, self.B6, self.C4, self.C5, self.C6)
        self.sqare3 = (self.A7, self.A8, self.A9, self.B7, self.B8, self.B9, self.C7, self.C8, self.C9)
        self.sqare4 = (self.D1, self.D2, self.D3, self.E1, self.E2, self.E3, self.F1, self.F2, self.F3)
        self.sqare5 = (self.D4, self.D5, self.D6, self.E4, self.E5, self.E6, self.F4, self.F5, self.F6)
        self.sqare6 = (self.D7, self.D8, self.D9, self.E7, self.E8, self.E9, self.F7, self.F8, self.F9)
        self.sqare7 = (self.G1, self.G2, self.G3, self.H1, self.H2, self.H3, self.I1, self.I2, self.I3)
        self.sqare8 = (self.G4, self.G5, self.G6, self.H4, self.H5, self.H6, self.I4, self.I5, self.I6)
        self.sqare9 = (self.G7, self.G8, self.G9, self.H7, self.H8, self.H9, self.I7, self.I8, self.I9)

        if self.row_count in [1, 2, 3]:
            self.sqare_rel1 = self.sqare1
            self.sqare_rel2 = self.sqare2
            self.sqare_rel3 = self.sqare3

        elif self.row_count in [4, 5, 6]:
            self.sqare_rel1 = self.sqare4
            self.sqare_rel2 = self.sqare5
            self.sqare_rel3 = self.sqare6
        else:
            self.sqare_rel1 = self.sqare7
            self.sqare_rel2 = self.sqare8
            self.sqare_rel3 = self.sqare9

    def generate_row(self):
        self.generate_var()
        for self.num in self.row_miss:
            self.generate_var()
            self.insert = []
            self.Cells = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7,
                          self.Cell8, self.Cell9]
            if self.num not in self.row:
                if self.row_count != 1:
                    if self.Cell1 != ' ':
                        if self.Cell2 != ' ':
                            if self.Cell3 != ' ':
                                if self.Cell4 != ' ':
                                    if self.Cell5 != ' ':
                                        if self.Cell6 != ' ':
                                            if self.Cell7 != ' ':
                                                if self.Cell8 != ' ':
                                                    if self.Cell9 != ' ':
                                                        pass

                                                    elif self.num not in self.collum9:
                                                        if self.num not in self.sqare_rel3:
                                                            self.Cell9 = self.num
                                                            self.update()
                                                            return True

                                                        else:
                                                            count = 0
                                                            for i in self.row_miss:
                                                                if i in self.sqare_rel3:
                                                                    count += 1
                                                                    if count >= len(self.row_miss):
                                                                        self.delete_row()
                                                            return False
                                                    else:
                                                        count = 0
                                                        for i in self.row_miss:
                                                            if i in self.collum9:
                                                                count += 1
                                                                if count >= len(self.row_miss):
                                                                    self.delete_row()

                                                elif self.num not in self.collum8:
                                                    if self.num not in self.sqare_rel3:
                                                        self.Cell8 = self.num
                                                        self.update()

                                                    else:
                                                        count = 0
                                                        for i in self.row_miss:
                                                            if i in self.sqare_rel3:
                                                                count += 1
                                                                if count >= len(self.row_miss):
                                                                    self.delete_row()
                                                        return False
                                                else:
                                                    count = 0
                                                    for i in self.row_miss:
                                                        if i in self.collum8:
                                                            count += 1
                                                            if count >= len(self.row_miss):
                                                                self.delete_row()

                                            elif self.num not in self.collum7:
                                                if self.num not in self.sqare_rel3:
                                                    self.Cell7 = self.num
                                                    self.update()

                                                else:
                                                    count = 0
                                                    for i in self.row_miss:
                                                        if i in self.sqare_rel3:
                                                            count += 1
                                                            if count >= len(self.row_miss):
                                                                self.delete_row()

                                            else:
                                                count = 0
                                                for i in self.row_miss:
                                                    if i in self.collum7:
                                                        count += 1
                                                        if count >= len(self.row_miss):
                                                            self.delete_row()

                                        elif self.num not in self.collum6:
                                            if self.num not in self.sqare_rel2:
                                                self.Cell6 = self.num
                                                self.update()

                                            else:
                                                count = 0
                                                for i in self.row_miss:
                                                    if i in self.sqare_rel2:
                                                        count += 1
                                                        if count >= len(self.row_miss):
                                                            self.delete_row()

                                        else:
                                            count = 0
                                            for i in self.row_miss:
                                                if i in self.collum6:
                                                    count += 1
                                                    if count >= len(self.row_miss):
                                                        self.delete_row()

                                    elif self.num not in self.collum5:
                                        if self.num not in self.sqare_rel2:
                                            self.Cell5 = self.num
                                            self.update()

                                        else:
                                            count = 0
                                            for i in self.row_miss:
                                                if i in self.sqare_rel2:
                                                    count += 1
                                                    if count >= len(self.row_miss):
                                                        self.delete_row()

                                    else:
                                        count = 0
                                        for i in self.row_miss:
                                            if i in self.collum5:
                                                count += 1
                                                if count >= len(self.row_miss):
                                                    self.delete_row()

                                elif self.num not in self.collum4:
                                    if self.num not in self.sqare_rel2:
                                        self.Cell4 = self.num
                                        self.update()

                                    else:
                                        count = 0
                                        for i in self.row_miss:
                                            if i in self.sqare_rel2:
                                                count += 1
                                                if count >= len(self.row_miss):
                                                    self.delete_row()

                                else:
                                    count = 0
                                    for i in self.row_miss:
                                        if i in self.collum4:
                                            count += 1
                                            if count >= len(self.row_miss):
                                                self.delete_row()

                            elif self.num not in self.collum3:
                                if self.num not in self.sqare_rel1:
                                    self.Cell3 = self.num
                                    self.update()

                                else:
                                    count = 0
                                    for i in self.row_miss:
                                        if i in self.sqare_rel1:
                                            count += 1
                                            if count >= len(self.row_miss):
                                                self.delete_row()

                            else:
                                count = 0
                                for i in self.row_miss:
                                    if i in self.collum3:
                                        count += 1
                                        if count >= len(self.row_miss):
                                            self.delete_row()

                        elif self.num not in self.collum2:
                            if self.num not in self.sqare_rel1:
                                self.Cell2 = self.num
                                self.update()

                            else:
                                count = 0
                                for i in self.row_miss:
                                    if i in self.collum2:
                                        count += 1
                                        if count >= len(self.row_miss):
                                            self.delete_row()

                        else:
                            count = 0
                            for i in self.row_miss:
                                if i in self.sqare_rel1:
                                    count += 1
                                    if count >= len(self.row_miss):
                                        self.delete_row()

                    elif self.num not in self.collum1:
                        if self.num not in self.sqare_rel1:
                            self.Cell1 = self.num
                            self.update()

                        else:
                            count = 0
                            for i in self.row_miss:
                                if i in self.sqare_rel1:
                                    count += 1
                                    if count >= len(self.row_miss):
                                        self.delete_row()

                    else:
                        count = 0
                        for i in self.row_miss:
                            if i in self.collum1:
                                count += 1
                                if count >= len(self.row_miss):
                                    self.delete_row()

    @staticmethod
    def generate_collum(collum):
        if len(collum) < 10:
            return list(set([str(i) for i in range(1, 10)]) - set(collum))[0]
        else:
            return '10'

    def update(self):
        self.Cells = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8,
                      self.Cell9]
        if self.row_count == 1:
            self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 2:
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 3:
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, self.C9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 4:
            self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8, self.D9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 5:
            self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 6:
            self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 7:
            self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        elif self.row_count == 8:
            self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8, self.H9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9
        else:
            self.I1, self.I2, self.I3, self.I4, self.I5, self.I6, self.I7, self.I8, self.I9 = self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9

    def delete_row(self):
        if self.row_count == 1:
            self.A1 = self.A2 = self.A3 = self.A4 = self.A5 = self.A6 = self.A7 = self.A8 = self.A9 = ' '
        elif self.row_count == 2:
            self.B1 = self.B2 = self.B3 = self.B4 = self.B5 = self.B6 = self.B7 = self.B8 = self.B9 = ' '
        elif self.row_count == 3:
            self.C1 = self.C2 = self.C3 = self.C4 = self.C5 = self.C6 = self.C7 = self.C8 = self.C9 = ' '
        elif self.row_count == 4:
            self.D1 = self.D2 = self.D3 = self.D4 = self.D5 = self.D6 = self.D7 = self.D8 = self.D9 = ' '
        elif self.row_count == 5:
            self.E1 = self.E2 = self.E3 = self.E4 = self.E5 = self.E6 = self.E7 = self.E8 = self.E9 = ' '
        elif self.row_count == 6:
            self.F1 = self.F2 = self.F3 = self.F4 = self.F5 = self.F6 = self.F7 = self.F8 = self.F9 = ' '
        elif self.row_count == 7:
            self.H1 = self.H2 = self.H3 = self.H4 = self.H5 = self.H6 = self.H7 = self.H8 = self.H9 = ' '
        elif self.row_count == 8:
            self.I1 = self.I2 = self.I3 = self.I4 = self.I5 = self.I6 = self.I7 = self.I8 = self.I9 = ' '
        else:
            self.I1 = self.I2 = self.I3 = self.I4 = self.I5 = self.I6 = self.I7 = self.I8 = self.I9 = ' '

        self.Cell1 = self.Cell2 = self.Cell3 = self.Cell4 = self.Cell5 = self.Cell6 = self.Cell7 = self.Cell8 = self.Cell9 = ' '

    def ausgabe(self):
        print('\n\n\n')
        print(' \t   >-- Sudoku  --<\n')
        print(self.A1, ' ', self.A2, ' ', self.A3, ' ¦ ', self.A4, ' ', self.A5, ' ', self.A6, ' ¦ ', self.A7, ' ',
              self.A8, ' ', self.A9)
        print(self.B1, ' ', self.B2, ' ', self.B3, ' ¦ ', self.B4, ' ', self.B5, ' ', self.B6, ' ¦ ', self.B7, ' ',
              self.B8, ' ', self.B9)
        print(self.C1, ' ', self.C2, ' ', self.C3, ' ¦ ', self.C4, ' ', self.C5, ' ', self.C6, ' ¦ ', self.C7, ' ',
              self.C8, ' ', self.C9)
        print('-----------+-------------+-----------')
        print(self.D1, ' ', self.D2, ' ', self.D3, ' ¦ ', self.D4, ' ', self.D5, ' ', self.D6, ' ¦ ', self.D7, ' ',
              self.D8, ' ', self.D9)
        print(self.E1, ' ', self.E2, ' ', self.E3, ' ¦ ', self.E4, ' ', self.E5, ' ', self.E6, ' ¦ ', self.E7, ' ',
              self.E8, ' ', self.E9)
        print(self.F1, ' ', self.F2, ' ', self.F3, ' ¦ ', self.F4, ' ', self.F5, ' ', self.F6, ' ¦ ', self.F7, ' ',
              self.F8, ' ', self.F9)
        print('-----------+-------------+-----------')
        print(self.G1, ' ', self.G2, ' ', self.G3, ' ¦ ', self.G4, ' ', self.G5, ' ', self.G6, ' ¦ ', self.G7, ' ',
              self.G8, ' ', self.G9)
        print(self.H1, ' ', self.H2, ' ', self.H3, ' ¦ ', self.H4, ' ', self.H5, ' ', self.H6, ' ¦ ', self.H7, ' ',
              self.H8, ' ', self.H9)
        print(self.I1, ' ', self.I2, ' ', self.I3, ' ¦ ', self.I4, ' ', self.I5, ' ', self.I6, ' ¦ ', self.I7, ' ',
              self.I8, ' ', self.I9)
        print('\n\n')

    # noinspection PyDefaultArgument
    def play(self, for_gui = True, modus='-M', key = {"easy": 40, "medium": 55, "hard": 70, "master": 100}):

        simple = ['-S', 'Simple']
        einfach = ['-E', 'Easy']
        mittel = ['-M', 'Medium']
        schwer = ['-S', 'Difficult']
        unmoeglich = ['-I', 'Impossible']

        self.generate()

        sudoku = self.__dict__()
        solution = self.__dict__()

        if modus in simple:
            for i in range(1):
                pos = random.choice(tuple(sudoku.keys()))
                sudoku[pos] = ' '

        elif modus in einfach:
            for i in range(key["easy"]):
                pos = random.choice(tuple(sudoku.keys()))
                sudoku[pos] = ' '

        elif modus in mittel:
            for i in range(key["medium"]):
                pos = random.choice(tuple(sudoku.keys()))
                sudoku[pos] = ' '

        elif modus in schwer:
            for i in range(key["hard"]):
                pos = random.choice(tuple(sudoku.keys()))
                sudoku[pos] = ' '

        elif modus in unmoeglich:
            for i in range(key["master"]):
                pos = random.choice(tuple(sudoku.keys()))
                sudoku[pos] = ' '

        else:
            raise KeyError('This Difficulty is not defined')

        if for_gui:
            return sudoku, solution

        else:
            self.ausgabe()


if __name__ == '__main__':
    sudo = Sudoku_Generator()
    sudo.play(False, '-S')

    input('Press return to close: ')
