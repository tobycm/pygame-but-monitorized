from datetime import datetime
from os import environ

from pygame import init as pg_init, display as pg_display, Surface, Color, Rect, event as pg_event, QUIT, draw as pg_draw
from pygame.time import Clock
from pygame.freetype import Font

# Set resolution
res = (350, 90)

# init
window_surface = pg_display.set_mode(res)
pg_init()
now = datetime.now()

# Set window title and size
pg_display.set_caption("Yo!")
window_surface = pg_display.set_mode(res)

# Set background
bg = Surface(res)
bg.fill(Color(0, 0, 0))

# Some constants and functions
done = False
clock = Clock()
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

digi_clock_font = Font("assets/fonts/7segmentsfont.ttf", 30)
temp = 0
second = now.second
minute = now.minute
hour = now.hour
day = now.day
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][now.month]
year = now.year

done = False

while not done:
    # Set framerate
    clock.tick(FPS)
    
    # Process events
    for event in pg_event.get():
        if event.type == QUIT:
            done = True
                        
    # Draw the background
    window_surface.blit(bg, (0, 0))
    
    # Create digital clock as Surface
    digi_clock = digi_clock_font.render(
        f"{hour:02d}:{minute:02d}:{second:02d}",
        Color("#42f5d1")
    )
    # digi_clock is now a tuple of (Surface, Rect)
    
    # Create digital date as Surface
    digi_date = digi_clock_font.render(
        f"{month}-{day:02d}-{year}",
        Color("#42f5d1")
    )
    # digi_date is now a tuple of (Surface, Rect)
    
    # Draw digital clock
    window_surface.blit(
        digi_clock[0],
        (
            MID[0] - digi_clock[1].width // 2,
            10
        )
    )
    
    # Draw digital date
    window_surface.blit(
        digi_date[0],
        (
            MID[0] - digi_date[1].width // 2,
            digi_clock[1].height + 15
        )
    )
    
    # Update time
    temp += 1
    if temp == FPS:
        now = datetime.now().time()
        second = now.second
        minute = now.minute
        hour = now.hour
        temp = 0

    
    pg_display.update()