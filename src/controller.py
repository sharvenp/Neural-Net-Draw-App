
from settings import Settings
import pygame as pg           

# Commands
from draw_command import DrawCommand
from erase_command import EraseCommand

# TkInter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from pymsgbox import *

class Controller:

    def __init__(self, model):
        self.model = model
        self.gui_elements = []

        self.is_dragged = False
        self.command = None

    def add_gui_elements(self, gui_elements):
        self.gui_elements = gui_elements

    def add_command(self, command):
        self.model.add_command(command)

    def predict_button_on_action(self, button):
        print("Predict")

    def load_button_on_action(self, button):
        print("Load")

        root = Tk()
        root.withdraw()		
        root.filename = filedialog.askopenfilename(title = "Load Neural Net Model", defaultextension=".json", filetypes = (("JSON File","*.json"),))
        path = root.filename
        root.destroy()
        self.is_dragged = False
        if path:
            self.model.load(path)
            print("Loaded from", path)
            self._pop_up("Load Successful", "Loaded the Network successfully.")

    def _pop_up(self, title, msg):
        root = Tk()
        root.withdraw()
        messagebox.showinfo(title, msg)

    def _handle_gui_elements(self, e, mouse, keys):

        mouse_buttons = mouse.get_pressed()
        mx, my = mouse.get_pos()

        for element in self.gui_elements:
            if element.name == "button":
                if e.type == pg.MOUSEBUTTONDOWN and mouse_buttons[0]:
                    element.is_clicked(mx, my)

    def _handle_mouse(self, e, mouse):

        mouse_buttons = mouse.get_pressed()
        mx, my = mouse.get_pos()

        if e.type == pg.MOUSEBUTTONDOWN:
            self.is_dragged = True
            if mouse_buttons[0]:
                self.command = DrawCommand()
            elif mouse_buttons[2]:
                self.command = EraseCommand()

            self.add_command(self.command)

        elif e.type == pg.MOUSEMOTION and self.is_dragged:
            
            if (Settings.DRAW_AREA_X + Settings.DRAW_STROKE <= mx <= Settings.DRAW_AREA_X + Settings.DRAW_AREA_WIDTH -  Settings.DRAW_STROKE):
                if (Settings.DRAW_AREA_Y + Settings.DRAW_STROKE <= my <= Settings.DRAW_AREA_Y + Settings.DRAW_AREA_HEIGHT -  Settings.DRAW_STROKE):
                    self.command.add_point(mx, my)

        elif e.type == pg.MOUSEBUTTONUP:
            self.is_dragged = False
            self.command = None
                    

    def _handle_keyboard(self, e, keys):

        if e.type == pg.KEYDOWN:
            if keys[pg.K_ESCAPE]:
                # Exit
                quit(0)

            if keys[pg.K_LCTRL] or keys[pg.K_RCTRL]: # Ctrl modifier
                if keys[pg.K_z]:
                    # Undo
                    self.model.undo()


    def handle(self, e, keys, mouse):

        if e.type == pg.QUIT:
            quit(0)

        self._handle_mouse(e, mouse)
        self._handle_keyboard(e, keys)
        self._handle_gui_elements(e, mouse, keys)
