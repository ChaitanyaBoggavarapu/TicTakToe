# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:07:29 2021

@author: abhil
"""
import Display_tic_tac_toe
class Tic_tak_toe:
    
    def __init__(self,grid):
        
        self.grid = grid
        self.row = None
        self.col = None
        self.symbol=None
    
    ###Place marker method 
    def place_marker(self,previous_place_holder = None):
    
        ##Displaying Table
        Display_tic_tac_toe.print_table(grid)
    
        ###Get Input From the User
        
   
        self.symbol = (input("Enter Symbol")).upper()
        try:
            self.row = int(input("Enter Row number ranging from 0 to 2"))
            self.col = int(input("Enter col number ranging from 0 to 2"))
            
        except:
            print("Please enter Intezer values")
            self.place_marker(previous_place_holder = None)
            
        
        while self.check_valid_input():
        ##Checking Whether Previous Symbol and current Symbol are same also current position is empty
            if(self.check_grid() and self.check_symbol(previous_place_holder)):        
                previous_place_holder = self.symbol
            else:
                print("This Column is filled or it is not your turn")
                return self.place_marker(previous_place_holder)
        
            self.grid[self.row][self.col] = self.symbol
            #Display_tic_tac_toe.l[self.row][self.col] = self.symbol
            
            

            if(self.check_finish()):
                Display_tic_tac_toe.print_table(grid)
                return self.symbol
            
            if(self.full_grid()):
                return "Game Over NoBody wins"
        
            return self.place_marker(previous_place_holder)     
                
    
        print("Please make Sure row and col values between 0 and 2 and Int also symbol only takes X and O")
        return self.place_marker(previous_place_holder)
     
    
    
    ##Checking Grid availability             
    def check_grid(self):
        if not self.grid[self.row][self.col]:
            return True
        return False
    
    ###Checking Previous and Current Symbol
    def check_symbol(self,previous_place_holder):
        if previous_place_holder != self.symbol:
            return True
        return False
    
        
    def check_finish(self):
    
    ##Checking Row and column wise
        for i in range(3):
            if((self.grid[i][0]  == self.grid[i][1] == self.grid[i][2] == 'X' or self.grid[i][0]  == self.grid[i][1] == self.grid[i][2] == 'O' ) or (self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == 'X' or self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == 'O') ):
                return True
            
        if self.grid[1][1]:
            if(self.grid[1][1] == self.grid[0][0] == self.grid[2][2] == 'X'  or self.grid[1][1] == self.grid[0][0] == self.grid[2][2] == 'O'):
                return True
            elif (self.grid[1][1] == self.grid[0][2] == self.grid[2][0] == 'X'  or self.grid[1][1] == self.grid[0][2] == self.grid[2][0] == 'O'):
                return True
        return False
        
    def full_grid(self):
    ##Check If full grid is filled
        for i in self.grid:
            for j in i:
                if not j:
                    return False 
        return True
    
    def check_valid_input(self):
        if((self.row <=2 and self.row >=0) and (self.col <=2 and self.col >=0) and (self.symbol == 'X' or self.symbol == 'O')):
            return True
        return False
    
    
if __name__=="__main__":
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    print("Game Completed, Winner is "+Tic_tak_toe(grid).place_marker())
    
    
        
        
        
        