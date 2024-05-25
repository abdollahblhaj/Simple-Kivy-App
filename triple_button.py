from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDSegmentedControl:
        pos_hint: {"center_x": .5, "center_y": .5}
        MDSegmentedControlItem:
            text: "Male"
        MDSegmentedControlItem:
            text: "Female"
        MDSegmentedControlItem:
            text: "All"
'''
class Exemple(MDApp):
    def build(self):
        return Builder.load_string(KV)
Exemple().run()
