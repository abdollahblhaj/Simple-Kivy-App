from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: "10dp"
    MDProgressBar:
        value: 60
        color: app.theme_cls.accent_color
'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
Test().run()