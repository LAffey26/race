from race.config import WHITE
import pygame
def changing_animation_frames (list_with_frames,frame,timer,speed):
    surf = list_with_frames[frame]
    if pygame.time.get_ticks() - timer > speed:
        timer= pygame.time.get_ticks()
        frame = (frame+1) % len(list_with_frames)
        surf = list_with_frames[frame]
        surf.set_colorkey(WHITE)
    return surf, frame, timer