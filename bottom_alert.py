from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "MDTopAppBar"
        left_action_items: [["menu", "This is the navigation"]]
        right_action_items:[["dots-vertical", lambda x: app.callback(x), "this is the More Actions"]]
    MDLabel:
        text: "Content"
        halign: "center"
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def callback(self, button):
        Snackbar(text="Hello World").open()
Test().run()
