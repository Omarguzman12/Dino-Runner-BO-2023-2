from pygame.font import Font
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
FONT_STYLE = "freesansbold.ttf"
balck_color = (0, 0, 0)


def get_message(message, size, width = SCREEN_WIDTH//2, hight = SCREEN_HEIGHT//2):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, balck_color)
    text_rect = text.get_rect()
    text_rect.center = (width, hight)
    return text, text_rect