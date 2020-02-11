from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
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

    StageTwoWidgetList = ListProperty([])

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
    def loginButtonTrigger(self, button):
        self.parent.transition.direction = "left" 
        if self.login(self.username.text,self.password.text):
            self.loginSuccess()
        else:
            print("FAILED")
        self.resetTextFields()

    def resetLoginWidgets(self):#Adds the original main screen widgets back as well as removing others
        self.layout.clear_widgets(self.StageTwoWidgetList)

        self.userLabel = Label(
            id = 'userLabel',
            size_hint = (0.25, 0.05),
            color = (0,0,0,1),
            pos_hint = {"x": 0.25, "y": 0.5},
            text= "Username: ")
        self.layout.add_widget(self.userLabel)

        self.username = TextInput(
            id='username',
            pos_hint = {"x": 0.50, "y": 0.5},
            size_hint= (0.2, 0.05),
            multiline =False)
        self.layout.add_widget(self.username)

        self.passLabel = Label(
            id='passLabel',
            size_hint= (0.25, 0.05),
            color= (0,0,0,1),
            pos_hint = {"x": 0.25, "y": 0.4},
            text = "Password: ")
        self.layout.add_widget(self.passLabel)

        self.password = TextInput(
            id='password',
            pos_hint={"x": 0.50, "y": 0.4},
            size_hint= (0.2, 0.05),
            multiline=False)
        self.layout.add_widget(self.password)
        self.loginButton = Button(
            background_normal= '',
            background_color= (1, .25, 0, 1),
            id= 'login',
            text="Login",
            pos_hint= {"x": 0.40, "y": 0.2},
            size_hint= (0.2,0.1))
                
        self.loginButton.bind(on_press=self.loginButtonTrigger)
        self.layout.add_widget(self.loginButton)
            
    def goToPost(self,button):
        self.parent.current = "post"

    def loginSuccess(self):
        self.layout.remove_widget(self.userLabel)
        self.layout.remove_widget(self.passLabel)
        self.layout.remove_widget(self.username)
        self.layout.remove_widget(self.password)
        self.layout.remove_widget(self.loginButton)
        subredditLabel = Label(size_hint=(0.25, 0.05),
                                    color=(0,0,0,1),
                                    pos_hint={"x": 0.25, "y": 0.4},
                                    text="Subreddit Name: ")
        self.StageTwoWidgetList.append(subredditLabel)
        self.layout.add_widget(subredditLabel)
        subredditInput = TextInput(pos_hint ={"x": 0.50, "y": 0.4},
                                        size_hint= (0.2, 0.05),
                                        multiline = False)
        self.StageTwoWidgetList.append(subredditInput)
        self.layout.add_widget(subredditInput)#TextInput
        confirm = Button(background_normal='',
                                        background_color = (1, .25, 0, 1),
                                        text="Confirm",
                                        pos_hint ={"x": 0.40, "y": 0.2},
                                        size_hint = (0.2,0.1))
        self.StageTwoWidgetList.append(confirm)
        confirm.bind(on_press=self.goToPost)
        self.layout.add_widget(confirm)#Confirm Button
        
        

class PostWindow(Screen):
    pass

class AnalyticWindow(Screen):
    pass

class WindowManager(ScreenManager):
    startWindow = ObjectProperty(None)

kv = Builder.load_file("GUI.kv")

class GUIApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    GUIApp().run()