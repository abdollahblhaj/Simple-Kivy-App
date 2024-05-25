from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
class ClickableTextFieldRound(MDRelativeLayout):
    pass
class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("kv.kv")
Example().run()

