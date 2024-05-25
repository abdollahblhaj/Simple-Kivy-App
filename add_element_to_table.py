from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
class Example(MDApp):
    data_tables = None
    def build(self):
        layout = MDFloatLayout() # root layout
        # button div
        button_box = MDBoxLayout(pos_hint={"center_x": 0.5},adaptive_size=True,padding="24dp",spacing="24dp",)
        #button 1 add row
        btn1=MDRaisedButton(text="Add row",on_release=self.on_button_press)
        #button 2 Remove row
        btn2=MDRaisedButton(text="Remove row",on_release=self.on_button_press)
        #add this button to button div
        button_box.add_widget(btn1)
        button_box.add_widget(btn2)
        # Create a table.
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},#table position
            size_hint=(0.9, 0.6),#size table 
            use_pagination=False,
            column_data=[("No.", dp(30)),("Column 1", dp(40)),("Column 2", dp(40)),("Column 3", dp(40)),],#colom of table
            row_data=[("1", "1", "2", "3"),("10", "51", "2", "3")],#data in table
        )
        # Adding a table and buttons to the toot layout.
        layout.add_widget(self.data_tables)#add table to layout
        layout.add_widget(button_box)#add button div to layout
        return layout
    def on_button_press(self, instance_button: MDRaisedButton) -> None:
        try:
            {
                "Add row": self.add_row,
                "Remove row": self.remove_row,
            }[instance_button.text]()
        except KeyError:
            pass

    def add_row(self) -> None:
        try:
            last_num_row = int(self.data_tables.row_data[-1][0])
            self.data_tables.add_row(("1", "1", "2", "3"))# function for add element to this table
        except:
            self.data_tables.add_row(("1", "1", "2", "3"))# function for add element to this table

    def remove_row(self) -> None:
        if len(self.data_tables.row_data) > 0:
            self.data_tables.remove_row(self.data_tables.row_data[-1])#function for remove element from the table
Example().run()
