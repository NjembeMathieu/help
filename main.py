from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (360, 540)


class MDLive(App, MDApp):

    CLASSES = {
        "ScreenUI": "liveapp.Screen_ui"
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def build_app(self, *args):
        print("Inside Build App Auto Reload 2")
        return Factory.ScreenUI()


MDLive().run()