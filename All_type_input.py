from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDTextField:

        hint_text: "Helper text on focus"
        helper_text: "This will disappear when you click off"
        helper_text_mode: "on_focus"
        helper_text_mode: "persistent"
        helper_text_mode: "on_error"
        pos_hint: {"center_x": .5,"center_y": .5}
        required: True
        max_text_length: 15
        multiline: True
        mode: "rectangle"
        mode: "fill"
      #  mode: "round"
        size_hint: 1, None
        height: "30dp"
        icon_right: "language-python"
        icon_right_color_focus: 0, 1, 0, 1
        icon_right_color_normal: 1, 1, 1, 1
        icon_left_color_normal: 1, 0, 1, 1



'''
class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)
Example().run()