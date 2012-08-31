#!/usr/bin/env python

from dvizshok.app import App
from ingame import InGame


class MyApp(App):
    pass

app = MyApp("Frogs", resolution=(800, 480), appstates=[InGame])
app.run()
