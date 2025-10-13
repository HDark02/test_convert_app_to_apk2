from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.core.window import Window
# Window.size = (464, 832)

kv="""
MDScreen:
    name: "main"
    MDFloatLayout:
        md_bg_color: "white"
        ProfileCard:
            size_hint_y: .45
            pos_hint: {"top": 1}
            elevation: 6
            md_bg_color: 1, 1, 1, 1
            radius: [0, 0, 20, 20]
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_y": .91}
                theme_text_color: "Custom"
                text_color: "gray"
                font_size: 20
            MDIconButton:
                icon: "dots-vertical"
                pos_hint: {"center_x": .93, "center_y": .91}
                theme_text_color: "Custom"
                text_color: "gray"
                font_size: 20
            MDLabel:
                text: "My Profile"
                pos_hint: {"center_x": .56, "center_y": .82}
                font_size: 25
                theme_text_color: "Primary"
                text_color: "black"
            Image:
                source: "télécharge.jpeg"
                pos_hint: {"center_x": .5, "center_y": .62}
                size_hint: .4, .4
                radius: [20, 20, 20, 20]
            MDLabel:
                text: "Alex Dynamo"
                font_size: 25
                pos_hint: {"center_y": .5}
                halign: "center"
                theme_text_color: "Custom"
                text_color: "black"
            MDLabel:
                text: "School of mobile development"
                font_size: 25
                pos_hint: {"center_y": .44}
                halign: "center"
                theme_text_color: "Custom"
                text_color: "gray"
            MDLabel:
                text: "Lome Togo"
                font_size: 25
                pos_hint: {"center_y": .38}
                halign: "center"
                theme_text_color: "Custom"
                text_color: "gray"
            
            MDGridLayout:
                rows: 2
                cols: 3
                size_hint: .85, .12
                pos_hint: {"center_x": .5, "center_y": .15}
                MDLabel:
                    text: "Photos"
                    font_size: 12
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"
                MDLabel:
                    text: "Followers"
                    font_size: 12
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"
                MDLabel:
                    text: "Likes"
                    font_size: 12
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"
                MDLabel:
                    text: "120"
                    font_size: 18
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"
                MDLabel:
                    text: "3K"
                    font_size: 18
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"
                MDLabel:
                    text: "56M"
                    font_size: 18
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "gray"

"""
class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass
class social(MDApp):

    def build(self):
        # global screen_manager
        # screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_string(kv))
        # return screen_manager
        return Builder.load_string(kv)
    
if __name__ == "__main__":
    social().run()