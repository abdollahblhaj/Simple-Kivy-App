from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
# Your layouts.
Builder.load_string(
'''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"
    IconLeftWidget:
        icon: root.icon
<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Lower the front layer"
    secondary_text: " by 50 %"
    icon: "transfer-down"
    on_press: root.backdrop.open(-Window.height / 2)
    pos_hint: {"top": 1}
    _no_ripple_effect: True
<MyBackdropBackLayer@Image>
    size_hint: .8, .8
    source: "2.png"
    pos_hint: {"center_x": .5, "center_y": .6}
'''
)
# Usage example of MDBackdrop.
Builder.load_string(
'''
<ExampleBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Example Backdrop"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu:"
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
'''
)
class ExampleBackdrop(MDScreen):
    pass
class TestBackdrop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return ExampleBackdrop()
TestBackdrop().run()
