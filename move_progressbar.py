from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
KV = '''
MDScreen:
    MDProgressBar:
        orientation: "vertical"
        id: progress
        pos_hint: {"center_y": .6}
        type: "indeterminate"
    MDRaisedButton:
        text: "STOP" if app.state == "start" else "START"
        pos_hint: {"center_x": .5, "center_y": .45}
        on_press: app.state = "stop" if app.state == "start" else "start"
'''
class Test(MDApp):
    state = StringProperty("stop")
    def build(self):
        return Builder.load_string(KV)
    def on_state(self, instance, value):
        {
            "start": self.root.ids.progress.start,
            "stop": self.root.ids.progress.stop,
        }.get(value)()
Test().run()
