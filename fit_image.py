from kivy.lang import Builder
from kivymd.app import MDApp
KV="""
MDBoxLayout:
   
    height: "700dp"
    orientation: 'vertical'
    FitImage:
        size_hint_y: 1
        source: '1.jpg'
        radius: 36, 36, 0, 0
    FitImage:
        size_hint_y: 1
        source: '2.jpg'
        radius: 36, 36, 0, 0
"""
class Main(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)
Main().run()