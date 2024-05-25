from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
class Example(MDApp):
    def build(self):
        layout = AnchorLayout()
        data_tables = MDDataTable(
            background_color_cell="#65275d",
            background_color_header="#65275d",
            background_color_selected_cell="e4514f",
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("[color=#52251B]Column 2[/color]", dp(30)),
                ("Column 3", dp(30)),
                ("[size=24][color=#C042B8]Column 4[/color][/size]", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
           (f"{i + 1}",
            "[color=#297B50]1[/color]",
            "[color=#C552A1]2[/color]",
            "[color=#6C9331]3[/color]",
            "4", 
            "5") for i in range(20)
        ],
        )
        layout.add_widget(data_tables)
        return layout
Example().run()