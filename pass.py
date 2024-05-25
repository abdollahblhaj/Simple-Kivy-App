from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
class ClickableTextFieldRound(MDRelativeLayout):
    pass
class Example(MDApp):

    def build(self):
        return Builder.load_string("""
<ClickableTextFieldRound>:

    MDTextField:
        id: text_field
        text: "root.text"
        password: True
        icon_left: "key-variant"
        pos_hint: {"center_y": .5}
    MDIconButton:
        icon: "reload"
        pos_hint: {"center_y": .6}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "reload-alert" if self.icon == "reload" else "reload"
            text_field.text = "False" if text_field.text is "True" else "True"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True
MDScreen:
    ClickableTextFieldRound:
        size_hint_x: None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .5}

""")

Example().run()