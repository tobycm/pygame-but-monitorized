from pygame import init as pg_init, display as pg_display, Surface, Color, Rect, event as pg_event, QUIT, draw as pg_draw
from pygame.time import Clock
import pygame_gui

pg_init()

# Set resolution
res = (640, 480)

# Set window title and size
pg_display.set_caption("Yo!")
window_surface = pg_display.set_mode(res)

# Set background
background = Surface(res)
background.fill(Color('#000000'))

# Some important stuff I don't know
manager = pygame_gui.UIManager(res)
clock = Clock()

# Some constants and functions
is_running = True
TL_CRN = (0, 0)
TR_CRN = (res[0], 0)
BL_CRN = (0, res[1])
BR_CRN = (res[0], res[1])
MID = tuple(pos // 2 for pos in res)
rectangle = Rect(
    (0, 0),
    (100, 50)
)

def center_rect(rect : Rect = rectangle):
    rect.x = MID[0] - rect.width // 2
    rect.y = MID[1] - rect.height // 2
    return rect

# Create a button with text
hello_button = pygame_gui.elements.UIButton(
    relative_rect=center_rect(rectangle),
    text='Say Hello',
    manager=manager
)

# Main loop
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pg_event.get():
        if event.type == QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    # Draw the background
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    
    # Draw the circle
    clock_size = 50
    pg_draw.circle(
        window_surface,
        Color('#ffffff'),
        (
            TL_CRN[0] + clock_size,
            TL_CRN[1] + clock_size
        ),
        clock_size
    )

    pg_display.update()