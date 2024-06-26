from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    # Will always be at the bottom of the screen.
    MDBottomAppBar:
        MDTopAppBar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "end"
            icon_color: 0, 1, 0, 1
'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
Test().run()