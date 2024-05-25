from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
KV = '''
<Item>
    ImageLeftWidget:
        source: root.source

MDFloatLayout:
    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_simple_dialog()
'''
class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()
class Example(MDApp):
    dialog = None
    def build(self):
        return Builder.load_string(KV)
    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    Item(text="user01@gmail.com", source="1.jpg"),
                    Item(text="user02@gmail.com", source="1.jpg"),
                    Item(text="Add account", source="1.jpg"),
                ],
            )
        self.dialog.open()
Example().run()
