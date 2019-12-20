
class Settings:
    """
    Holds all the settings used by the application.
    """
    # Colors
    DRAW_COLOR = (255, 255, 255) # Has to be white
    BACKGROUND_COLOR = (0, 0, 0)
    BUTTON_COLOR = (60, 33, 64)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    
    # Application Window Dimensions
    WIDTH = 800
    HEIGHT = 500
    PADDING = 30

    # Drawing Box parameters
    BOX_EDGE_THICKNESS = 3
    DRAW_AREA_X = PADDING
    DRAW_AREA_Y = PADDING
    DRAW_AREA_WIDTH = HEIGHT - (PADDING * 2)
    DRAW_AREA_HEIGHT = HEIGHT - (PADDING * 2)

    # Fonts
    DEFAULT_FONT = ("Consolas", 25)

    # Drawing parameters
    DRAW_STROKE = 12
    ERASE_STROKE = 36

    # Button parameters
    BUTTON_PADDING = 20