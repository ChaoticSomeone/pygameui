import pygameui as pu
import pygame as pg
from sys import exit

win = pg.display.set_mode((400,400))
pg.display.set_caption("PyGameUI")

def clicked(args):
    self = args[0]
    print("Hello, world!")

btn = pu.Button(win, pg.Rect(50,50,120,70), color=(255,0,0), onClick=clicked)
txt = pu.Text(win, [55,60], "Hello", 50, "calibri", autoBg=True, bold=True)

while True:
    pu.Events.getAll()
    btn.update()
    txt.show()
    for ev in pu.Events.all:
        if ev.type == pg.QUIT: exit(0)
    pg.display.update()