import pygame as pg

class Events:
    all = []
    allTypes = []

    @staticmethod
    def getAll():
        Events.all = pg.event.get()
        Events.allTypes = []
        for ev in Events.all:
            Events.allTypes.append(ev.type)