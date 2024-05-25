from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDSmartTile:
        radius: 24
        box_radius: [0, 0, 24, 24]
        box_color: 0, 0, 1, .2
        source: "1.jpg"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "320dp", "320dp"
        MDIconButton:
            icon: "heart-outline"
            theme_icon_color: "Custom"
            icon_color: 1, 0, 0, 1
            pos_hint: {"center_y": .5}
            on_release:
                self.icon = "heart" \
                if self.icon == "heart-outline" else \
                "heart-outline"
        MDLabel:
            text: "follow"
            bold: True
            color: 1, 0, 0, 1

'''
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
MyApp().run()