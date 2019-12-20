
# Main App

import pygame as pg

from model import Model
from view import NeuralNetView
from controller import Controller


if __name__ == "__main__":

    model = Model([(784, '*'), (38, 'sigmoid'), (10, 'sigmoid')])
    view = NeuralNetView()
    controller = Controller(model)

    model.add_observer(view)
    view.attach_controller(controller)

	# Launch Application
    view.launch()