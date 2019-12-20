
from gui_element import GUI_Element
from settings import Settings

class Label(GUI_Element):

    def __init__(self, text, x, y):

        GUI_Element.__init__(self, "label")

        self.text = text

        self.x = x
        self.y = y