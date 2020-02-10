from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen 
import praw

reddit = None

class StartUpWindow(Screen):

    username = ObjectProperty(None)
    password = ObjectProperty(None)
    userLabel = ObjectProperty(None)
    passLabel = ObjectProperty(None) 
    layout = ObjectProperty(None)
    loginButton = ObjectProperty(None)

    def login(self, username,password):
        try:
            global reddit
            reddit = praw.Reddit(user_agent="joe",
                                client_id='msA8YHPtMopEFg',
                                client_secret='iiqKiuOkS4bicJwyBiTq_hQ5lwQ',
                                password=password,#to be changed
                                username=username)#to be changed
            return True
        except:
            return False
    def resetTextFields(self):
        self.username.text = ""
        self.password.text = ""
        print("ey")
    def resetLoginWidgets(self):#Adds the original main screen widgets back
        pass
    def goToPost(self,button):
        self.parent.current = "post"#trying to do the same as inside the kv file
    def loginSuccess(self):
        self.layout.remove_widget(self.userLabel)
        self.layout.remove_widget(self.passLabel)
        self.layout.remove_widget(self.username)
        self.layout.remove_widget(self.password)
        self.layout.remove_widget(self.loginButton)
        self.layout.add_widget(Label(size_hint=(0.25, 0.05),
                                    color=(0,0,0,1),
                                    pos_hint={"x": 0.25, "y": 0.4},
                                    text="Subreddit Name: "))
        self.layout.add_widget(TextInput(pos_hint ={"x": 0.50, "y": 0.4},
                                        size_hint= (0.2, 0.05),
                                        multiline = False))#TextInput
        confirm = Button(background_normal='',
                                        background_color = (1, .25, 0, 1),
                                        text="Confirm",
                                        pos_hint ={"x": 0.40, "y": 0.2},
                                        size_hint = (0.2,0.1))
        confirm.bind(on_press=self.goToPost)
        self.layout.add_widget(confirm)#Confirm Button
        
        

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