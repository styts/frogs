#!/usr/bin/env python

from dvizshok.app import App
from ingame import InGame


class MyApp(App):
    pass

#res = (480, 320)
res = (800, 600)
#res = (1024, 768)
app = MyApp("Frogs", resolution=res, appstates=[InGame])
app.run()
