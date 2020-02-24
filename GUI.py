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
from post import Post

import praw

reddit = None

"""
-Add option to have a tray application/do the waiting in the background or send it to a server to post it
-Maybe intergrate with amazon lambda
"""

class StartUpWindow(Screen):

    username = ObjectProperty(None)
    password = ObjectProperty(None)
    userLabel = ObjectProperty(None)
    passLabel = ObjectProperty(None) 
    layout = ObjectProperty(None)
    loginButton = ObjectProperty(None)

    

    StageTwoWidgetList = ListProperty([])

    def login(self, username,password):#Doesn't really work
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
    post_type = StringProperty(defaultvalue='txt')

    text_post_widget = ObjectProperty(None)
    img_post_widget = ObjectProperty(None)
    vid_post_widget = ObjectProperty(None)
    post_container = ObjectProperty(None)
    title = ObjectProperty(None)

    def change_post_type(self, post_type=None):
        if post_type == None:
            post_type = self.post_type

        if post_type == 'img':
            self.add_img_widget()
        elif post_type == 'vid':
            self.add_vid_widget()
        else:
            self.add_txt_widget()   
        
    def focus_main_widget(self):
        post_type = self.post_type

        if post_type =='vid':
            self.vid_post_widget.opacity = 1
            self.vid_post_widget.disabled = False
            self.img_post_widget.opacity = 0
            self.img_post_widget.disabled = True
            self.text_post_widget.opacity = 0
            self.text_post_widget.disabled = True
        elif post_type =='img':
            self.img_post_widget.opacity = 1
            self.img_post_widget.disabled = False
            self.text_post_widget.opacity = 0
            self.text_post_widget.disabled = True
            self.vid_post_widget.opacity = 0
            self.vid_post_widget.disabled = True
        else:#assume post type is txt
            self.text_post_widget.opacity = 1
            self.text_post_widget.disabled = False
            self.img_post_widget.opacity = 0
            self.img_post_widget.disabled = True
            self.vid_post_widget.opacity = 0
            self.vid_post_widget.disabled = True

    def construct_JSON(self):
        if self.post_type == "img":
            post = Post(self.title.text,self.post_type,txt=None,filePath=self.img_post_widget.source)
        elif self.post_type == "vid":
            post = Post(self.title.text,self.post_type,txt=None,filePath=self.vid_post_widget.source)
        else:
            post = Post(self.title.text,self.post_type,txt=self.text_post_widget.text)
        print(post.to_JSON())
        #construct a post obj then make the JSON then print it for now

class AnalyticWindow(Screen):
    pass

class WindowManager(ScreenManager):
    start_window = ObjectProperty(None)
    post_window = ObjectProperty(None)
    analyse_window = ObjectProperty(None)

#kv = Builder.load_file("GUI.kv") #maybe this is the problem?? getting different behaviour doing this in build

class GUIApp(App):
    def build(self):
        #start = StartUpWindow()
        Window.bind(on_dropfile=self._on_file_drop)
        return WindowManager()
    def _on_file_drop(self, widget, file_path):
        if self.root.current == "post":
            post_type = self.root.post_window.post_type
            print(post_type)
            temp = str(file_path).replace("\'","")
            self.file_path = temp[1:len(temp)]
            if post_type == 'vid':
                self.root.get_screen('post').ids.vid_post.source = self.file_path
                print("SOURCE: ",self.root.get_screen('post').ids.vid_post.source)
                self.root.get_screen('post').ids.vid_post.state = 'play'
                print("WIDGET ",self.root.post_window.vid_post_widget,"\n STATE: ",self.root.post_window.vid_post_widget.state)    
                
            elif post_type == 'img':
                print(self.file_path)
                print("IMAGE: ",self.root.post_window.img_post_widget)
                self.root.post_window.img_post_widget.source = self.file_path

if __name__ == '__main__':
    GUIApp().run()