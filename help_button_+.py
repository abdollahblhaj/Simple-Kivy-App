from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView
KV = '''
Screen:
    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos: 100, 100
        on_release: app.tap_target_start()
'''
class TapTargetViewDemo(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="[size=36]Title text[/size]",
            description_text="[color=#ff0000ff]Description text[/color]",
            widget_position="left_bottom",
            outer_circle_color=(1, 1, 0),
            target_circle_color=(1, 0, 0),
            #widget_position="right","top""bottom""left_top""right_top""center"
        )
        return screen
    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
TapTargetViewDemo().run()
