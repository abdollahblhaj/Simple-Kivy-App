from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
kv="""
MDScreen:
    MDBottomNavigation:
        panel_color:"#eeeaea"
        selected_color_background:"#11111f"
        text_color_active:"white"
        MDBottomNavigationItem:
            name: "screen 1"
            text:"Mail"
            icon:"gmail"
            MDLabel:
                text:"screen 1"
                halign:"center"
        MDBottomNavigationItem:
            name: "screen 2"
            text:"linkedin"
            icon:"linkedin"
            MDLabel:
                text:"screen 2"
                halign:"center"


    
"""
class Example(MDApp):
    def build(self):
        return Builder.load_string(kv)
Example().run()