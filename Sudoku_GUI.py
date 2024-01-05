# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:34:14 2023

Coded by Foxispythonlab
"""


############################ --- Importe --- ##################################

import random, os, pickle
from PyQt6.QtWidgets import (
    QApplication,
    QWidget, 
    QSpacerItem,
    QLabel, 
    QLineEdit, 
    QGridLayout,
    QVBoxLayout,
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

class Sudoku_Generator:
    def __init__(self, typ: str = 'generate'):
        random.seed()
        if typ == 'generate':
            self.A1 = self.A2 = self.A3 = self.A4 = self.A5 = self.A6 = self.A7 = self.A8 = self.A9 = ' '
            self.B1 = self.B2 = self.B3 = self.B4 = self.B5 = self.B6 = self.B7 = self.B8 = self.B9 = ' '
            self.C1 = self.C2 = self.C3 = self.C4 = self.C5 = self.C6 = self.C7 = self.C8 = self.C9 = ' '
            
            self.D1 = self.D2 = self.D3 = self.D4 = self.D5 = self.D6 = self.D7 = self.D8 = self.D9 = ' '
            self.E1 = self.E2 = self.E3 = self.E4 = self.E5 = self.E6 = self.E7 = self.E8 = self.E9 = ' '
            self.F1 = self.F2 = self.F3 = self.F4 = self.F5 = self.F6 = self.F7 = self.F8 = self.F9 = ' '
            
            self.G1 = self.G2 = self.G3 = self.G4 = self.G5 = self.G6 = self.G7 = self.G8 = self.G9 = ' '
            self.H1 = self.H2 = self.H3 = self.H4 = self.H5 = self.H6 = self.H7 = self.H8 = self.H9 = ' '
            self.I1 = self.I2 = self.I3 = self.I4 = self.I5 = self.I6 = self.I7 = self.I8 = self.I9 = ' '
            
        self.collum9 = [self.A9, self.B9, self.C9, self.D9, self.E9, self.F9, self.G9, self.H9, self.I9]
        self.collum8 = [self.A8, self.B8, self.C8, self.D8, self.E8, self.F8, self.G8, self.H8, self.I8]
        self.collum7 = [self.A7, self.B7, self.C7, self.D7, self.E7, self.F7, self.G7, self.H7, self.I7]
        self.collum6 = [self.A6, self.B6, self.C6, self.D6, self.E6, self.F6, self.G6, self.H6, self.I6]
        self.collum5 = [self.A5, self.B5, self.C5, self.D5, self.E5, self.F5, self.G5, self.H5, self.I5]
        self.collum4 = [self.A4, self.B4, self.C4, self.D4, self.E4, self.F4, self.G4, self.H4, self.I4]
        self.collum3 = [self.A3, self.B3, self.C3, self.D3, self.E3, self.F3, self.G3, self.H3, self.I3]
        self.collum2 = [self.A2, self.B2, self.C2, self.D2, self.E2, self.F2, self.G2, self.H2, self.I2]
        self.collum1 = [self.A1, self.B1, self.C1, self.D1, self.E1, self.F1, self.G1, self.H1, self.I1]
        
        self.sqare1 = [self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3]
        self.sqare2 = [self.A4, self.A5, self.A5, self.B4, self.B5, self.B6, self.C4, self.C5, self.C6]
        self.sqare3 = [self.A7, self.A8, self.A9, self.B7, self.B8, self.B9, self.C7, self.C8, self.C9]
        self.sqare4 = [self.D1, self.D2, self.D3, self.E1, self.E2, self.E3, self.F1, self.F2, self.F3]
        self.sqare5 = [self.D4, self.D5, self.D6, self.E4, self.E5, self.E6, self.F4, self.F5, self.F6]
        self.sqare6 = [self.D7, self.D8, self.D9, self.E7, self.E8, self.E9, self.F7, self.F8, self.F9]
        self.sqare7 = [self.G1, self.G2, self.G3, self.H1, self.H2, self.H3, self.I1, self.I2, self.I3]
        self.sqare8 = [self.G4, self.G5, self.G6, self.H4, self.H5, self.H6, self.I4, self.I5, self.I6]
        self.sqare9 = [self.G7, self.G8, self.G9, self.H7, self.H8, self.H9, self.I7, self.I8, self.I9]
        
        self.row1 = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9]
        self.row2 = [self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9]
        self.row3 = [self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, self.C9]
        self.row4 = [self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8, self.D9]
        self.row5 = [self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9]
        self.row6 = [self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9]
        self.row7 = [self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9]
        self.row8 = [self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8, self.H9]
        self.row9 = [self.I1, self.I2, self.I3, self.I4, self.I5, self.I6, self.I7, self.I8, self.I9]
        
        self.sudoku = {
                'A1' : self.A1, 'A2' : self.A2, 'A3' : self.A3, 'A4' : self.A4, 'A5' : self.A5, 'A6' : self.A6, 'A7' : self.A7, 'A8' : self.A8, 'A9' : self.A9, 
                'B1' : self.B1, 'B2' : self.B2, 'B3' : self.B3, 'B4' : self.B4, 'B5' : self.B5, 'B6' : self.B6, 'B7' : self.B7, 'B8' : self.B8, 'B9' : self.B9, 
                'C1' : self.C1, 'C2' : self.C2, 'C3' : self.C3, 'C4' : self.C4, 'C5' : self.C5, 'C6' : self.C6, 'C7' : self.C7, 'C8' : self.C8, 'C9' : self.C9, 
                'D1' : self.D1, 'D2' : self.D2, 'D3' : self.D3, 'D4' : self.D4, 'D5' : self.D5, 'D6' : self.D6, 'D7' : self.D7, 'D8' : self.D8, 'D9' : self.D9, 
                'E1' : self.E1, 'E2' : self.E2, 'E3' : self.E3, 'E4' : self.E4, 'E5' : self.E5, 'E6' : self.E6, 'E7' : self.E7, 'E8' : self.E8, 'E9' : self.E9, 
                'F1' : self.F1, 'F2' : self.F2, 'F3' : self.F3, 'F4' : self.F4, 'F5' : self.F5, 'F6' : self.F6, 'F7' : self.F7, 'F8' : self.F8, 'F9' : self.F9, 
                'G1' : self.G1, 'G2' : self.G2, 'G3' : self.G3, 'G4' : self.G4, 'G5' : self.G5, 'G6' : self.G6, 'G7' : self.G7, 'G8' : self.G8, 'G9' : self.G9, 
                'H1' : self.H1, 'H2' : self.H2, 'H3' : self.H3, 'H4' : self.H4, 'H5' : self.H5, 'H6' : self.H6, 'H7' : self.H7, 'H8' : self.H8, 'H9' : self.H9, 
                'I1' : self.I1, 'I2' : self.I2, 'I3' : self.I3, 'I4' : self.I4, 'I5' : self.I5, 'I6' : self.I6, 'I7' : self.I7, 'I8' : self.I8, 'I9' : self.I9}
    
        
    def generate(self):
        for _ in range(0, 50):
            self.rows = ['row1', 'row2', 'row3', 'row4', 'row5', 'row5','row6', 'row7', 'row8', 'row9']
            for row in self.rows:
                self.Cell1 = self.Cell2 = self.Cell3 = self.Cell4 = self.Cell5 = self.Cell6 = self.Cell7 = self.Cell8 = self.Cell9 = ' '
                if row == 'row1':
                    self.row_count = 1
                    self.nums = ['1', '2','3', '4', '5', '6', '7', '8', '9']
                    random.shuffle(self.nums)
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.nums
                    
                    self.update()
                    
                
                elif row == 'row2':
                    self.row_count = 2
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9
                    for i in range(0, 20):
                        if self.generate_row():
                            break
                
                elif row == 'row3':
                    self.row_count = 3
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, self.C9
                    for i in range(0, 50):
                        if self.generate_row():
                            break
                        
                elif row == 'row4':
                    self.row_count = 4
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8, self.D9
                    for i in range(0, 50):
                        if self.generate_row():
                            break
                            
                elif row == 'row5':
                    self.row_count = 5
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9
                    for i in range(0, 50):
                        if self.generate_row():
                            break
            
                elif row == 'row6':
                    self.row_count = 6
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9
                    for i in range(0, 100):
                        if self.generate_row():
                            break
                        
                elif row == 'row7':
                    self.row_count = 7
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9
                    for i in range(0, 100):
                        if self.generate_row():
                            break
                        
                elif row == 'row8':
                    self.row_count = 8
                    self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9 = self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8, self.H9
                    for i in range(0, 150):
                        if self.generate_row():
                            break
                else:
                    self.row_count = 9
                    self.collums = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
                    for self.cell_count in self.collums:
                        if self.cell_count == 'I1':
                            self.collum = [self.A1, self.B1, self.C1, self.D1, self.E1, self.F1, self.G1, self.H1, self.I1]
                            self.generate_collum()
                            self.I1 = self.Cell
                        elif self.cell_count == 'I2':
                            self.collum = [self.A2, self.B2, self.C2, self.D2, self.E2, self.F2, self.G2, self.H2, self.I2]
                            self.generate_collum()
                            self.I2 = self.Cell
                        elif self.cell_count == 'I3':
                            self.collum = [self.A3, self.B3, self.C3, self.D3, self.E3, self.F3, self.G3, self.H3, self.I3]
                            self.generate_collum()
                            self.I3 = self.Cell
                        elif self.cell_count == 'I4':
                            self.collum = [self.A4, self.B4, self.C4, self.D4, self.E4, self.F4, self.G4, self.H4, self.I4]
                            self.generate_collum()
                            self.I4 = self.Cell
                        elif self.cell_count == 'I5':
                            self.collum = [self.A5, self.B5, self.C5, self.D5, self.E5, self.F5, self.G5, self.H5, self.I5]
                            self.generate_collum()
                            self.I5 = self.Cell
                        elif self.cell_count == 'I6':
                            self.collum = [self.A6, self.B6, self.C6, self.D6, self.E6, self.F6, self.G6, self.H6, self.I6]
                            self.generate_collum()
                            self.I6 = self.Cell
                        elif self.cell_count == 'I7':
                            self.collum = [self.A7, self.B7, self.C7, self.D7, self.E7, self.F7, self.G7, self.H7, self.I7]
                            self.generate_collum()
                            self.I7 = self.Cell
                        elif self.cell_count == 'I8':
                            self.collum = [self.A8, self.B8, self.C8, self.D8, self.E8, self.F8, self.G8, self.H8, self.I8]
                            self.generate_collum()
                            self.I8 = self.Cell
                        elif self.cell_count == 'I9':
                            self.collum = [self.A9, self.B9, self.C9, self.D9, self.E9, self.F9, self.G9, self.H9, self.I9]
                            self.generate_collum()
                            self.I9 = self.Cell
            
      
            if self.checker('gen'):
                return True, self.sudoku

         
    def checker(self, com):
        if com == 'gen':
            self.generate_var('check')
            
        check = True
        for pos in tuple(self.sudoku.keys()):
            if self.sudoku[pos] == ' ':
                check = False
                break
        
        if check:
            #Returns the Sudoku
            return True, self.sudoku
        
        else:
            if com == 'gen':
                
                self.__init__('regenerate')
                         
                    
    def generate_var(self, gen = True):
        self.__init__('var')
        
        if gen:
            self.row = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9]
            
            row_miss = []
                
            if '1' not in self.row:
                row_miss += '1'
            if '2' not in self.row:
                row_miss += '2'
            if '3' not in self.row:
                row_miss += '3'
            if '4' not in self.row:
                row_miss += '4'
            if '5' not in self.row:
                row_miss += '5'
            if '6' not in self.row:
                row_miss += '6'
            if '7' not in self.row:
                row_miss += '7'
            if '8' not in self.row:
                row_miss += '8'
            if '9' not in self.row:
                row_miss += '9'
                
            random.shuffle(row_miss)
            
            if self.row_count in [1, 2, 3]:
                sqare_rel1 = self.sqare1
                sqare_rel2 = self.sqare2
                sqare_rel3 = self.sqare3
                
            elif self.row_count in [4, 5, 6]:
                sqare_rel1 = self.sqare4
                sqare_rel2 = self.sqare5
                sqare_rel3 = self.sqare6
            else:
                sqare_rel1 = self.sqare7
                sqare_rel2 = self.sqare8
                sqare_rel3 = self.sqare9
            return row_miss, sqare_rel1, sqare_rel2, sqare_rel3
        else:
            self.row = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9]
            
            
    def generate_row(self):
        row_miss, sqare_rel1, sqare_rel2, sqare_rel3 = self.generate_var()
                
        for num in row_miss:
                    self.Cells = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9]
                    if num not in self.row:
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
                                                                raise RuntimeError("Sudoku can't be generated")
                                                            
                                                            elif num not in self.collum9:
                                                                if num not in sqare_rel3:
                                                                    self.Cell9 = num
                                                                    self.update()
                                                                    return True
                                                                    
                                                                else:
                                                                    count = 0
                                                                    for i in row_miss:
                                                                        if i in sqare_rel3:
                                                                            count +=1
                                                                            if count >= len(row_miss):
                                                                                self.delete_row()
                                                                    return False
                                                            else:
                                                                count = 0
                                                                for i in row_miss:
                                                                    if i in self.collum9:
                                                                        count +=1
                                                                        if count >= len(row_miss):
                                                                            self.delete_row()
                                                     
                                                    
                                                        elif num not in self.collum8:
                                                            if num not in sqare_rel3:
                                                                self.Cell8 = num
                                                                self.update()
                                                                
                                                            else:
                                                                count = 0
                                                                for i in row_miss:
                                                                    if i in sqare_rel3:
                                                                        count +=1
                                                                        if count >= len(row_miss):
                                                                            self.delete_row()
                                                                return False
                                                        else:
                                                            count = 0
                                                            for i in row_miss:
                                                                if i in self.collum8:
                                                                    count +=1
                                                                    if count >= len(row_miss):
                                                                        self.delete_row()
                                                            
                                                            
                                                            
                                                    elif num not in self.collum7:
                                                        if num not in sqare_rel3:
                                                            self.Cell7 = num
                                                            self.update()
                                                            
                                                        else:
                                                            count = 0
                                                            for i in row_miss:
                                                                if i in sqare_rel3:
                                                                    count +=1
                                                                    if count >= len(row_miss):
                                                                        self.delete_row()
                                              
                                                    else:
                                                        count = 0
                                                        for i in row_miss:
                                                            if i in self.collum7:
                                                                count +=1
                                                                if count >= len(row_miss):
                                                                    self.delete_row()
                                                  
                                                        
                                                elif num not in self.collum6:
                                                    if num not in sqare_rel2:
                                                        self.Cell6 = num
                                                        self.update()
                                                        
                                                    else:
                                                        count = 0
                                                        for i in row_miss:
                                                            if i in sqare_rel2:
                                                                count +=1
                                                                if count >= len(row_miss):
                                                                    self.delete_row()
                                                 
                                                else:
                                                    count = 0
                                                    for i in row_miss:
                                                        if i in self.collum6:
                                                            count +=1
                                                            if count >= len(row_miss):
                                                                self.delete_row()
                                                            
                                                            
                              
                                            elif num not in self.collum5:
                                                if num not in sqare_rel2:
                                                    self.Cell5 = num
                                                    self.update()
                                                    
                                                else:
                                                    count = 0
                                                    for i in row_miss:
                                                        if i in sqare_rel2:
                                                            count +=1
                                                            if count >= len(row_miss):
                                                                self.delete_row()
                                            
                                            else:
                                                count = 0
                                                for i in row_miss:
                                                    if i in self.collum5:
                                                        count +=1
                                                        if count >= len(row_miss):
                                                            self.delete_row()
                                                    
                                                    
                                        elif num not in self.collum4:
                                            if num not in sqare_rel2:
                                                self.Cell4 = num
                                                self.update()
                                                
                                            else:
                                                count = 0
                                                for i in row_miss:
                                                    if i in sqare_rel2:
                                                        count +=1
                                                        if count >= len(row_miss):
                                                            self.delete_row()
                                    
                                        else:
                                            count = 0
                                            for i in row_miss:
                                                if i in self.collum4:
                                                    count +=1
                                                    if count >= len(row_miss):
                                                        self.delete_row()
                            
                
                                    elif num not in self.collum3:
                                        if num not in sqare_rel1:
                                            self.Cell3 = num
                                            self.update()
                                            
                                        else:
                                            count = 0
                                            for i in row_miss:
                                                if i in sqare_rel1:
                                                    count +=1
                                                    if count >= len(row_miss):
                                                        self.delete_row()
                                    
                                    else:
                                        count = 0
                                        for i in row_miss:
                                            if i in self.collum3:
                                                count +=1
                                                if count >= len(row_miss):
                                                    self.delete_row()
                                
                                            
                                elif num not in self.collum2:
                                    if num not in sqare_rel1:
                                        self.Cell2 = num
                                        self.update()
                                    
                                    else:
                                        count = 0
                                        for i in row_miss:
                                            if i in self.collum2:
                                                count +=1
                                                if count >= len(row_miss):
                                                    self.delete_row()
                                    
                                else:
                                    count = 0
                                    for i in row_miss:
                                        if i in sqare_rel1:
                                            count +=1
                                            if count >= len(row_miss):
                                                self.delete_row()
                                    
                                        
                            elif num not in self.collum1:
                                if num not in sqare_rel1:
                                    self.Cell1 = num
                                    self.update()
                                
                                else:
                                    count = 0
                                    for i in row_miss:
                                        if i in sqare_rel1:
                                            count +=1
                                            if count >= len(row_miss):
                                                self.delete_row()
                                
                            else:
                                count = 0
                                for i in row_miss:
                                    if i in self.collum1:
                                        count +=1
                                        if count >= len(row_miss):
                                            self.delete_row()
                            
                        
    def generate_collum(self):
        self.generate_var(False)
        if '1' not in self.collum:
            self.Cell = '1'
        elif '2' not in self.collum:
            self.Cell = '2'
        elif '3' not in self.collum:
            self.Cell = '3'
        elif '4' not in self.collum:
            self.Cell = '4'
        elif '5' not in self.collum:
            self.Cell = '5'
        elif '6' not in self.collum:
            self.Cell = '6'
        elif '7' not in self.collum:
            self.Cell = '7'
        elif '8' not in self.collum:
            self.Cell = '8'
        else:
            self.Cell = '9'
    
    
    def update(self):
        self.Cells = [self.Cell1, self.Cell2, self.Cell3, self.Cell4, self.Cell5, self.Cell6, self.Cell7, self.Cell8, self.Cell9]
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
        print(('\n\n\n'*50))
        os.system('cls')
        print('\n\n\n\t\t\t>-- Sudoku  --<\n')
        print("\t    1 - 2 - 3  -  4 - 5 - 6  -  7 - 8 - 9")
        print('\t    -------------------------------------')
        count1 = count2 = -1
        for row in range(1, 10):
            nr = str('A' if row == 1 else 'B' if row ==2 else 'C' if row == 3
                  else 'D' if row == 4 else 'E' if row == 5 else 'F' if row == 6
                  else 'G' if row == 7 else 'H' if row == 8 else 'I')
            
            count1 += 1; count2 = -1
            if count1 >= 3:
                print('\t    -----------+-------------+-----------'); count1 = 0 
            print(f"\t{nr} -", end = '')
            for cell in tuple(self.sudoku.keys())[row*9-9:row*9]:
                count2 += 1
                if count2 >= 3:
                    print('| ', end = ''); count2 = 0 
                print(f" {self.sudoku[cell]} ", end = ' ')
            print()
            
            
    def play(self, for_gui : True, modus = '-M'):
        while True:
            einfach = ['-E', 'Easy']
            mittel = ['-M', 'Medium']
            schwer = ['-S', 'Difficult']
            unmöglich = ['-U', 'Impossible']
            
            if not self.generate():
               self.__init__()
               continue
            
            self.sudoku_solved = dict(self.sudoku)
            
            if modus in einfach:
                for i in range(40):
                    pos = random.choice(tuple(self.sudoku.keys()))
                    self.sudoku[pos] = ' '
                    
            elif modus in mittel:
                for i in range(55):
                    pos = random.choice(tuple(self.sudoku.keys()))
                    self.sudoku[pos] = ' '
                    
            elif modus in schwer:
                for i in range(70):
                    pos = random.choice(tuple(self.sudoku.keys()))
                    self.sudoku[pos] = ' '
                    
            elif modus in unmöglich:
                for i in range(100):
                    pos = random.choice(tuple(self.sudoku.keys()))
                    self.sudoku[pos] = ' '
                    
            else:
                raise KeyError('This Difficulty is not defined')
                    
            if for_gui:
                return self.sudoku, self.sudoku_solved
            
            else:
                self.ausgabe()
            
                
class Sudoku_Widget(QWidget):
    def __init__(self, sudoku: dict, solution : dict):
        super().__init__()
        
        self.setWindowTitle('Sudoku - Visualizer')
        self.setGeometry(0, 0, 800, 500)
        
        
        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 75, 75, 75))
        
        nums = [0, 1, 2, 4, 5, 6, 8, 9, 10]
        letters = [i for i in 'ABCDEFGHI']
        self.translation_to_letters = {}
        for i in range(len(nums)):
            self.translation_to_letters[int(nums[i])] = letters[i]
        
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
                            sudoku_display[f"{row}{collum}"] = QLineEdit()
                            sudoku_display[f"{row}{collum}"].setText((sudoku[f"{row}{collum}"] if sudoku[f"{row}{collum}"] != ' ' else ''))
                            sudoku_display[f"{row}{collum}"].textChanged.connect(self.check)
                        else:   
                            sudoku_display[f"{row}{collum}"] = QLabel(sudoku[f"{row}{collum}"])
                        #sudoku_display[f"{row}{collum}"].setFixedSize(w, h)
                            
                        layout.addWidget(sudoku_display[f"{row}{collum}"], ord(row.lower()) - (96 - modr) , int(collum) + modc,
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
            if type(field) == QLineEdit:
                if '-' not in field.text():
                    if field.text() in nums:
                        pos = self.layout().getItemPosition(self.layout().indexOf(field))
                        
                        num = field.text()
                        row = self.translation_to_letters[pos[0]]
                        collum = (pos[1] + 1 if pos[1] < 3 else pos[1]  if pos[1] < 7 else pos[1] -1)
                
                        if self.sudoku_solution[f"{row}{collum}"] == num:
                            field.hide()
                            self.sudoku_display[key] = QLabel(num)
                            self.layout().addWidget(self.sudoku_display[key],
                                    pos[0], pos[1], 1, 1, Qt.AlignmentFlag.AlignCenter)
                        else:
                            self.trys -= 1
                            print('You used all trys up' if self.trys <= 0
                                  else f"Wrong, your used a try, you have {self.trys} left")
                            
                    
                    else:
                        field.setText('')
        
        full = True
        for field in self.sudoku_display.values():
            if type(field) == QLineEdit:
                full = False
        if full:
            print('Sudoku Solved')
        
        
    def paintEvent(self, event):
        pen = QPainter()
        pen.begin(self)
        
        pen_style = QPen()
        pen_style.setWidth(int(self.size / 5 + 1))
        pen.setPen(pen_style)
        
        w = self.geometry().width()
        h = self.geometry().height()
        
        pen.drawLine(int(w/3) + 20, 75, int(w/3) + 20, h-75)
        pen.drawLine(int(w/3) * 2 - 20, 75, int(w/3) * 2 - 20, h-75)
        pen.drawLine(75, int(h/3) + 20, w-75, int(h/3) + 20)
        pen.drawLine(75, int(h/3) * 2 - 20, w-75, int(h/3) * 2 - 20)
        
        pen.end()
        
        
    def resizeEvent(self, event):
        w = self.geometry().width()
        h = self.geometry().height()
        
        self.size = abs(int((w-150 * h-150) / 10000))

        for field in self.sudoku_display.values():
            field.setFont(self.font('Times', self.size + 5))
            
    def font(self, style: str, size = 10):
        font = QFont(style)
        font.setPointSize(int(size))
        return font


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Sudoku - v1.0 Alpha')
        self.setGeometry(0, 0, 800, 500)
        
        self.generator = Sudoku_Generator()
        
        self.init_menubar()
        self.home()
        
        
        
    def init_menubar(self):
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
        if type(self.active_widget) == Sudoku_Widget:
            with open('Latest_Sudoku.sdu', 'wb') as f:
                values = [dict(), self.active_widget.sudoku_solution]
                for field in self.active_widget.sudoku_display.keys():
                    values[0][field] = self.active_widget.sudoku_display[field].text()
                pickle.dump(values, f)
        
    def load_sudoku(self):
        try:
            with open('Latest_Sudoku.sdu', 'rb') as f:
                sudoku, solution = pickle.load(f)
                self.active_widget = Sudoku_Widget(sudoku, solution)
                self.setCentralWidget(self.active_widget)
        except:
            return 'E1'
        
    def home(self):
        layout = QGridLayout()
        layout.setContentsMargins(QMargins(75, 50, 50, 50))
        
        titel = QLabel('Sudoku')
        titel.setFont(self.font('Times', 48))
        
        bu_create = QPushButton('Create Sudoku')
        bu_create.clicked.connect(self.create_medium)
        bu_create.setFont(self.font('Times', 14))
        
        bu_load = QPushButton('Load latest Sudoku')
        bu_load.clicked.connect(self.load_sudoku)
        bu_load.setFont(self.font('Times', 14))
        
        bu_statistics = QPushButton('Show Statistics')
        bu_statistics.setFont(self.font('Times', 14))
        
        layout.addWidget(titel, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_create, 1, 0,  Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_load, 1, 1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bu_statistics, 1, 2, Qt.AlignmentFlag.AlignCenter)
        
        self.active_widget = QWidget()
        self.active_widget.setLayout(layout)
        self.setCentralWidget(self.active_widget)
        
        
    def create_easy(self, difficulty):
        sudoku, solution = self.generator.play(True, '-E')
        sudoku_window = Sudoku_Widget(sudoku, solution)
        self.active_widget = sudoku_window
        self.setCentralWidget(sudoku_window)
        
    def create_medium(self):
        sudoku, solution = self.generator.play(True, '-M')
        sudoku_window = Sudoku_Widget(sudoku, solution)
        self.active_widget = sudoku_window
        self.setCentralWidget(sudoku_window)
        
    def create_hard(self):
        sudoku, solution = self.generator.play(True, '-S')
        sudoku_window = Sudoku_Widget(sudoku, solution)
        self.active_widget = sudoku_window
        self.setCentralWidget(sudoku_window)
      
    def font(self, style: str = 'Times', size = 10):
        font = QFont(style)
        font.setPointSize(int(size))
        return font
        

######################### --- Main Programm --- ###############################

if __name__ == '__main__': 
    
    app = QApplication([])
    mainwin = Window()
    mainwin.show()
    app.exec()

else:
    print('loaded Sudoku module form Foxispythonlab')
