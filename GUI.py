from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 


class StartUpWindow(Screen):
    pass

class PostWindow(Screen):
    pass

class AnalyticWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("GUI.kv")

class GUIApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    GUIApp().run()