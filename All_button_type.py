from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet

KV = '''
MDScreen:
    #md_bg_color: "#f7f2fa"
    MDIconButton:
        icon: "language-python"
        icon: "android"
        #md_bg_color: app.theme_cls.primary_color
        icon_color: app.theme_cls.primary_color
        icon: "1.jpg"
        icon_size: "64sp"
        pos_hint: {"center_x": 0.8, "center_y": 0.6}
    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
    MDFlatButton:
        text: "[color=#00ffcc]MDFLATBUTTON[/color]"
        theme_text_color: "Custom"
        font_size: "18sp"
        #font_name: "path/to/font"  #load file for font
        text_color: 0, 0, 1, 1
        line_color: 0, 0, 1, 1
        pos_hint:{"center_x": .8, "center_y": .1}
    MDRectangleFlatIconButton:
        icon: "android"
        text: "hello"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 1, 0, 1, 1
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
        pos_hint:{"center_x": .5, "center_y": .1}
    MDRectangleFlatIconButton
        text:"hi!"
        icon:"language-python"
        line_color:(0, 0, 0, 0)
        pos_hint:{"center_x": .1, "center_y": .1}
        icon: "language-python"
    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"
        text_color: 0, 1, 0, 1
        pos_hint:{"center_x": .9, "center_y": .9}
    MDFillRoundFlatButton
        text: "MDROUNDFLATBUTTON"
        text_color: 1, 0, 0, 1
        pos_hint:{"center_x": .1, "center_y": .9}
    MDTextButton:
        text: "MDTEXTBUTTON"
        custom_color: 0, 1, 1, 1
        pos_hint:{"center_x": .1, "center_y": .6}
    MDFloatingActionButtonSpeedDial:
        data: app.data1   #go to json data in class 
        bg_hint_color: app.theme_cls.primary_light
        root_button_anim: True
    MDRaisedButton:
        text: "Open list bottom sheet"
        on_release:  app.show_example_grid_bottom_sheet()
        pos_hint: {"center_x": .5, "center_y": .5}
    MDSwitch:
        widget_style: "ios"
        pos_hint: {"center_x": .4, "center_y": .4}
'''
class Example(MDApp):
    data1 = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
        }
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)
    def on_start(self):
        data = {
            "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
            "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
            "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type=type_button,
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    icon_color=data[type_button]["text_color"],
                    )
            )
    def callback_for_menu_items(self, *args):
        toast(args[0])
    def show_example_grid_bottom_sheet(self):
        data1 = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
            }

        bottom_sheet_menu = MDGridBottomSheet()
        for item in data1.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x,
                y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

Example().run()
