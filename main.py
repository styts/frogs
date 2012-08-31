#!/usr/bin/env python

from dvizshok.app import App
from ingame import InGame


class MyApp(App):
    pass

app = MyApp("Frogs", appstates=[InGame])
app.run()
