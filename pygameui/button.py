import pygame as pg
from pygameui.events import Events
from pygameui.color import Color
pg.init()

class Button:
    def __init__(self, surf:pg.Surface, rect:pg.Rect, color:tuple[int, int, int]=(0,0,0), img:pg.surface=None, onClick=None, onClickArgs:list[any]=[]):
        self.surf = surf
        self.rect = rect
        self.color = Color.colorRestrain(color)
        self.img = img
        self.onClick = onClick
        self.onClickArgs = onClickArgs

        if self.img is not None:
            if self.rect.width < self.img.get_width():
                self.rect.width = self.img.get_width()
            if self.rect.height < self.img.get_height():
                self.rect.height = self.img.get_height()

    def update(self):
        self.onClickArgs.insert(0, self)

        # draw button to surface
        if self.img is not None:
            self.surf.blit(self.img, [self.rect.x, self.rect.y])
        else:
            pg.draw.rect(self.surf, self.color, self.rect)

        # check for click event
        mouseX, mouseY = pg.mouse.get_pos()
        if pg.MOUSEBUTTONDOWN in Events.allTypes and self.rect.collidepoint(mouseX, mouseY):
            self.onClick(self.onClickArgs)
