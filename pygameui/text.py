import pygame as pg
from pygameui.color import Color
pg.init()

class Text:
    def __init__(self, surf:pg.surface.Surface, pos:list[int, int], text:str, fontSize:int, font:str, fg:list[int,int,int]=[255,255,255], bg:list[int,int,int]=[0,0,0], autoBg=True, bold:bool=False, italic:bool=False):
        self.surf = surf
        self.pos = pos
        self.text = text
        self.fontSize = fontSize
        self.font = font
        self.fg = Color.colorRestrain(fg)
        self.bg = Color.colorRestrain(bg)
        self.autoBg = autoBg
        self.bold = bold
        self.italic = italic

    def show(self):
        if self.autoBg: self.bg = self.surf.get_at(self.pos)
        fontObj = pg.font.SysFont(self.font, self.fontSize, self.bold, self.italic)
        textObj = fontObj.render(self.text, True, self.fg, self.bg)
        self.surf.blit(textObj, self.pos)