from race.config import WHITE
import pygame
def change (tuple_with_png,frame,timer,speed):
    surf = tuple_with_png[frame]
    if pygame.time.get_ticks() - timer > speed:
        timer= pygame.time.get_ticks()
        frame = (frame+1) % len(tuple_with_png)
        surf = tuple_with_png[frame]
        surf.set_colorkey(WHITE)
    return surf, frame, timer