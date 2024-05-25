from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDIconButton:
        icon: "1.jpg"
        pos_hint: {"center_x": .5, "center_y": .5}
        icon_size: "64sp"


'''
class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)
Example().run()
