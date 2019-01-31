import pygame
import os
from time import sleep
from math import pi
from random import choice 


    
class PlayClass():
    def __init__(self):
        self.fon = pygame.image.load("1/fon0.jpg")
        self.shar = pygame.image.load("1/shar1.png")
        self.shar = self.shar.convert_alpha()
        self.x, self.y = 500, 500
        self.key_down,self.key_up = False, False
    def key_button_control(self):
        if self.key_up:
            self.y -= 1
        if self.key_down:
            self.y += 1

    def set_view(self, left, top, cell_size):
        pass
        
    def get_click(self, mouse_pos):
        try:
            cell = self.get_cell(mouse_pos)
            self.on_click(self, cell)
        except Exception as e:
            print(e)
        
    def get_cell(self, cort):
        x, y = pygame.mouse.get_pos()
        x, y = (x - self.left)//self.cell_size, (y - self.top)//self.cell_size
        # print(x, y)
        if (x >= 0 and x <= self.width) and (y >= 0 and y <= self.height):
            return (x, y,)
    
    def on_click(self, obg, cell):
        if cell:
            x, y = cell
            r, g, b = self.board[y][x]
                    
 
    def render(self):
        try:
            self.key_button_control()
            screen.blit(self.fon, (0, 0))
            screen.blit(self.shar, (self.x, self.y))
            '''
            for i in range(self.width):
                for j in range(self.height):
                    self.board2[j][i] = [(i * self.cell_size + self.left),
                                         (j * self.cell_size + self.top),
                                         self.cell_size,self.cell_size][::]
                                         '''
        except Exception as e:
            print(e)


pygame.init()
screen = pygame.display.set_mode((1000,800))
osn_play = PlayClass()
running = True     
while running:   
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False 
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_DOWN:
                osn_play.key_down = True
            if i.key == pygame.K_UP:
                osn_play.key_up = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_DOWN:
                osn_play.key_down = False
            if i.key == pygame.K_UP:
                osn_play.key_up = False           
    if i.type == pygame.MOUSEBUTTONDOWN:
        osn_play.get_click(i.pos)  
        sleep(0.7)
    screen.fill((0, 0, 0))
    osn_play.render()
    pygame.display.flip()
pygame.quit()