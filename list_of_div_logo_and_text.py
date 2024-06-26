from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
w='''
#:import SliverToolbar __main__.SliverToolbar
<CardItem>
    size_hint_y: None
    height: "86dp"
    padding: "4dp"
    radius: 12
    elevation: 4
    FitImage:
        source: "1.jpg"
        radius: root.radius
        size_hint_x: None
        width: root.height
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        spacing: "6dp"
        padding: "12dp", 0, 0, 0
        pos_hint: {"center_y": .5}
        MDLabel:
            text: "abdollah"
            font_style: "H5"
            bold: True
            adaptive_height: True
        MDLabel:
            text: "Devoloper"
            theme_text_color: "Hint"
            adaptive_height: True
MDScreen:
    MDSliverAppbar:
        max_height: "200dp"
        background_color: "2d4a50"
        toolbar_cls: SliverToolbar()
        MDSliverAppbarHeader:
            MDRelativeLayout:
                FitImage:
                    source: "2.jpg"
        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True
'''
class CardItem(MDCard, RoundedRectangularElevationBehavior):
    pass
class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_height = "medium"
        self.headline_text = "persons"
        self.left_action_items = [["arrow-left", lambda x: x]]
        self.right_action_items = [
            ["attachment", lambda x: x],
            ["calendar", lambda x: x],
            ["dots-vertical", lambda x: x],
            ]
class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(w)
    def on_start(self):
        for x in range(10):
            self.root.ids.content.add_widget(CardItem())
Example().run()
