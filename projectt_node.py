from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

class Example(MDApp):

    def login(self,email,password):
        if email=="abdollah" and password=="123":
            return "yes"
        else:
            return "no"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("project.kv")
    
Example().run()
