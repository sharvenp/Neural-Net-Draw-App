
# Main App

import pygame as pg
from nn import NeuralNet

class NeuralNetApp:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.padding = 30
        self.draw_area_x = self.padding
        self.draw_area_y = self.padding
        self.draw_area_width = self.height - (self.padding * 2)
        self.draw_area_height = self.height - (self.padding * 2)
        
        self.stroke = 9
        
        structure = [(784, '*'), (38, 'sigmoid'), (10, 'sigmoid')]
        self.neural_net = NeuralNet(structure, random_init_bound=0.05)

    def _clear_screen(self, screen):

    	screen.fill(self.BLACK)
    	pg.draw.rect(screen, self.WHITE, (self.draw_area_x, self.draw_area_y, self.draw_area_width, self.draw_area_height), 3)

    def run_app(self):

        pg.init()
        
        screen = pg.display.set_mode((self.width, self.height))    
        pg.display.set_caption('Neural Net App')
        
        font = pg.font.SysFont('Courier', 25)

        self._clear_screen(screen)

        while True:
            
            # Exit Condition
            e = pg.event.poll()
            if e.type == pg.QUIT:
                return

            b1, b2, b3 = pg.mouse.get_pressed()
            mx, my = pg.mouse.get_pos()

            if (self.draw_area_x + self.stroke <= mx <= self.draw_area_x + self.draw_area_width -  self.stroke) and \
               (self.draw_area_y + self.stroke <= my <= self.draw_area_y + self.draw_area_height -  self.stroke):
                if b1: # Left Click
                    pg.draw.circle(screen, self.WHITE, (mx, my), self.stroke)
                elif b3: # Right Click
                    pg.draw.circle(screen, self.BLACK, (mx, my), self.stroke * 4)

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                return
            elif keys[pg.K_c]:
            	self._clear_screen(screen)

            pg.display.update()
            

if __name__ == "__main__":
    nn_app = NeuralNetApp(800, 500)
    nn_app.run_app()
