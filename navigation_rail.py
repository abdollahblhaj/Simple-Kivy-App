from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
class ExtendedButton(RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)
    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"
    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4
    
class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("test.kv")
    def switch_screen(self, instance_navigation_rail, instance_navigation_rail_item):
        self.root.ids.screen_manager.current = (
        instance_navigation_rail_item.icon.split("-")[1].lower()
    )
    def on_start(self):
        '''Creates application screens.'''
        navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()
        for widget in navigation_rail_items:
            name_screen = widget.icon.split("-")[1].lower()
            screen = MDScreen(
                name=name_screen,
                md_bg_color="#edd769",
                radius=[18, 0, 0, 0],
            )
            box = MDBoxLayout(padding="12dp")
            label = MDLabel(
                text=name_screen.capitalize(),
                font_style="H1",
                halign="right",
                adaptive_height=True,
                shorten=True,
            )
            box.add_widget(label)
            screen.add_widget(box)
            self.root.ids.screen_manager.add_widget(screen)
Example().run()