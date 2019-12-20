
from gui_element import GUI_Element
from settings import Settings

class Button(GUI_Element):

    def __init__(self, text, x, y, width, height):

        GUI_Element.__init__(self, "button")

        self.text = text

        self.associated_elements = ()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.on_action = self._default_on_action

    def set_associated_elements(self, associated_elements):
        self.associated_elements = associated_elements

    def set_on_action(self, action):
        self.on_action = action

    def is_clicked(self, x, y):
        
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                self.on_action(self)

    def _default_on_action(self):
        pass
