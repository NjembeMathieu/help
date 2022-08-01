from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton


class ScreenUI(Screen):

    def __init__(self):
        super().__init__()
        mdflat_button = MDFlatButton(
            text="button",
            pos_hint={"center_x":0.5,"center_y":0.5}
        )
        self.add_widget(mdflat_button)