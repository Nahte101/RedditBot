from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.video import Video
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
        self.parent.current_window = 'post'

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
    post_type = StringProperty()

    text_post_widget = ObjectProperty(None)
    img_post_widget = ObjectProperty(None)
    vid_post_widget = ObjectProperty(None)
    post_container = ObjectProperty(None)

#schedule this to do when button to change posttype is clicked
    def change_post_type(self, post_type=None):
        if post_type == None:
            post_type = self.post_type

        if post_type == 'img':
            self.add_img_widget()
        elif post_type == 'vid':
            self.add_vid_widget()
        else:
            self.add_txt_widget()   
        
    def remove_main_post_widget(self):
        self.post_container.clear_widgets()

    def add_vid_widget(self):
        vid = Video(id='vid_post',pos_hint={"top":0.99,"x":0.001},
                size_hint=[0.999,0.96])
        self.post_container.add_widget(vid)
    def add_img_widget(self):
        img = Image(id='img_post',pos_hint={"top":0.99,"x":0.001},
                size_hint=[0.999,0.96])
        self.post_container.add_widget(img)
    def add_txt_widget(self):
        txt = TextInput(id='paraText',text="Text underneath title",pos_hint={"top":0.99,"x":0.001},
                size_hint=[0.999,0.96])
        self.post_container.add_widget(txt)


class AnalyticWindow(Screen):
    pass

class WindowManager(ScreenManager):
    start_window = ObjectProperty(None)
    post_window = ObjectProperty(None)
    analyse_window = ObjectProperty(None)

kv = Builder.load_file("GUI.kv")

class GUIApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return kv
    def _on_file_drop(self, widget, file_path):
        if self.root.current == "post":
            post_type = self.root.post_window.post_type
            print(post_type)
            temp = str(file_path).replace("\'","")
            self.file_path = temp[1:len(temp)]
            if post_type == 'vid':    
                print(self.file_path)
                self.root.post_window.child.
            elif post_type == 'img':
                print(self.file_path)
                self.root.post_window.
            return

if __name__ == '__main__':
    GUIApp().run()