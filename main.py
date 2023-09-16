from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar,MDBottomAppBar


Window.size = (350,580)
Builder.load_file("homescreen.kv")


class HomeScreen(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):

        return HomeScreen()

MyApp().run()
