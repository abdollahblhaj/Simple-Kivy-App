from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDChip:
        text: "account"
        icon_right: "close-circle-outline"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.on_release_chip(self)
        icon_left: "1.jpg"
        line_color: app.theme_cls.disabled_hint_text_color
        md_bg_color: 1, 0, 0, .5

'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def on_release_chip(self,instance_check):
        a=instance_check
        print("instance_check")
Test().run()