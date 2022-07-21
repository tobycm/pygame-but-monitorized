from math import cos, sin
from datetime import datetime

from pygame import init as pg_init, display as pg_display, Surface, Color, Rect, event as pg_event, QUIT, draw as pg_draw
from pygame.time import Clock
from pygame.freetype import Font
import pygame_gui

pg_init()

# Set resolution
res = (640, 480)

# Set window title and size
pg_display.set_caption("Yo!")
window_surface = pg_display.set_mode(res)

# Set background
bg = Surface(res)
bg.fill(Color(0, 0, 0))

# Some important stuff I don't know
manager = pygame_gui.UIManager(res)
clock = Clock()

# Some constants and functions
is_running = True
FPS = 60
TL_CRN = (0, 0)
TR_CRN = (res[0], 0)
BL_CRN = (0, res[1])
BR_CRN = (res[0], res[1])
MID = tuple(pos // 2 for pos in res)
default_rect = Rect(
    (0, 0),
    (100, 50)
)

digi_clock_font = Font("assets/fonts/7segmentsfont.ttf", 20)
temp = 0
second = 0
minute = 0
hour = 0

def center_rect(rect : Rect = default_rect):
    rect.x = MID[0] - rect.width // 2
    rect.y = MID[1] - rect.height // 2
    return rect

def degrees_to_pygame(radius : int, angle : int):
    x = round(sin(angle * 3.14 / 180) * radius)
    y = round(cos(angle * 3.14 / 180) * radius)
    return (x + radius, -y + radius)

# Main loop
while is_running:
    # Set framerate
    clock.tick(FPS)
    
    # Process events
    for event in pg_event.get():
        if event.type == QUIT:
            is_running = False

        manager.process_events(event)

    # Draw the background
    window_surface.blit(bg, (0, 0))
    manager.draw_ui(window_surface)
    
    # Draw the circle
    clock_size = 50
    pg_draw.circle(
        window_surface,
        Color(255, 255, 255),
        (
            TL_CRN[0] + clock_size,
            TL_CRN[1] + clock_size
        ),
        clock_size
    )
    
    # Draw seconds
    pg_draw.line(
        window_surface,
        Color(255, 50, 50),
        (clock_size, clock_size),
        degrees_to_pygame(clock_size, round(second * (360 / 60))),
        3
    )
    
    # Draw minutes
    pg_draw.line(
        window_surface,
        Color("#4287f5"),
        (clock_size, clock_size),
        degrees_to_pygame(clock_size, round(minute * (360 / 60))),
        3
    )
    
    # Draw hours
    pg_draw.line(
        window_surface,
        Color(0, 0, 0),
        (clock_size, clock_size),
        degrees_to_pygame(clock_size, round(hour * (360 / 24))),
        3
    )
    
    # Create digital clock as Surface
    digi_clock = digi_clock_font.render(
        f"{hour:02d}:{minute:02d}:{second:02d}",
        Color("#42f5d1")
    )
    # digi_clock is now a tuple of (Surface, Rect)
    
    # Draw digital clock
    window_surface.blit(
        digi_clock[0],
        (
            MID[0] - digi_clock[1].width // 2,
            MID[1] - digi_clock[1].height // 2
        )
    )
        
    # Update time
    temp += 1
    if temp == FPS:
        now = datetime.now()
        now = now.time()
        second = now.second
        minute = now.minute
        hour = now.hour
        temp = 0

    
    pg_display.update()