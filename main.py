#!/usr/bin/env python

from dvizshok.app import App
from ingame import InGame


class MyApp(App):
    def init(self):
        self.resman.load_font("default", 20)
        self.font = self.resman.get_font("default_20")

#res = (480, 320)
res = (800, 480)
#res = (800, 600)
#res = (1024, 768)
app = MyApp("Frogs", resolution=res, appstates=[InGame], fps=100)
app.run()
