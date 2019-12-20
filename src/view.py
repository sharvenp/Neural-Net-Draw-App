
from observer import Observer
from settings import Settings
from button import Button
from label import Label

import pygame as pg

class NeuralNetView(Observer):

    def __init__(self):
        
        pg.init()
        
        self.screen = pg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))    
        pg.display.set_caption('Neural Net App by Sharven')

    def attach_controller(self, controller):
        self.controller = controller
    
    def _add_gui_elements(self):

        self.gui_elements = []

        x = Settings.DRAW_AREA_X + Settings.DRAW_AREA_WIDTH + Settings.BUTTON_PADDING
        y = Settings.DRAW_AREA_Y + Settings.BUTTON_PADDING
        width = (Settings.WIDTH - Settings.BUTTON_PADDING) - x
        height = 50
        
        predict_label = Label("Prediction: ", x, y + (height + Settings.BUTTON_PADDING)*4)

        self.gui_elements.append(predict_label)

        predict_button = Button("Predict", x, y, width, height)
        predict_button.set_on_action(self.controller.predict_button_on_action)
        predict_button.set_associated_elements((self.screen, predict_label))

        self.gui_elements.append(predict_button)

        load_button = Button("Load Net", x, y + height + Settings.BUTTON_PADDING, width, height)
        load_button.set_on_action(self.controller.load_button_on_action)

        self.gui_elements.append(load_button)

    def _render_screen(self, model=None):

        self.screen.fill(Settings.BACKGROUND_COLOR)

        # Execute all drawing commands
        if model:
            for command in model.commands:
                command.execute(self.screen)

        # Render all gui elements
        for element in self.gui_elements:
            if element.name == "button":
                # Render Button
                x, y, width, height = element.x, element.y, element.width, element.height
                pg.draw.rect(self.screen, Settings.BUTTON_COLOR, (x, y, width, height))

                font = pg.font.SysFont(Settings.DEFAULT_FONT[0], Settings.DEFAULT_FONT[1])
                button_text = font.render(element.text, True, Settings.BUTTON_TEXT_COLOR)
                self.screen.blit(button_text, button_text.get_rect(center=(x + width//2, y + height//2)))

            elif element.name == "label":
                # Render Label
                x, y, text = element.x, element.y, element.text
                font = pg.font.SysFont(Settings.DEFAULT_FONT[0], Settings.DEFAULT_FONT[1])
                label_text = font.render(text, True, Settings.BUTTON_TEXT_COLOR)
                self.screen.blit(label_text, (x, y))

        pg.draw.rect(self.screen, Settings.DRAW_COLOR, \
                    (Settings.DRAW_AREA_X, Settings.DRAW_AREA_Y, Settings.DRAW_AREA_WIDTH, Settings.DRAW_AREA_HEIGHT), \
                    Settings.BOX_EDGE_THICKNESS)


        pg.display.update()

    def update(self, model):
        self._render_screen(model)

    def launch(self):

        self._add_gui_elements()
        self._render_screen()        

        self.controller.add_gui_elements(self.gui_elements)

        while True:
            e = pg.event.poll()
            keys = pg.key.get_pressed()
            mouse = pg.mouse
            self.controller.handle(e, keys, mouse)
            