
from observable import Observable
from observer import Observer
from nn import NeuralNet

class Model(Observable, Observer):

    def __init__(self, structure):

        Observable.__init__(self)

        self.neural_net = NeuralNet(structure, random_init_bound=0.05)
        self.commands = []

    def load(self, path):
        pass

    def update(self, command):
        self.notify_observers()

    def add_command(self, command):
        self.commands.append(command)
        command.add_observer(self)
        self.notify_observers()

    def undo(self):
        if self.commands:
            self.commands.pop()
            self.notify_observers()

    def clear(self):
        self.commands.clear()
        self.notify_observers()
