from turtle import width
import pygame
import os    
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

WIDTH, HEIGHT = 1080, 720

class AdaLovelace(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        #button
        self.button = Button (text = "Ada Lovelace General Info")
        self.button.bind(on_press = self.ada)

        self.button2 = Button (text = "Psychology")
        self.button2.bind(on_press = self.psychology)

        self.button3 = Button (text = "How the field would be lacking")
        self.button3.bind(on_press = self.lacking)

        self.button4 = Button (text = "Significance")
        self.button4.bind(on_press = self.sig)

        self.button5 = Button (text = "Why unique")
        self.button5.bind(on_press = self.unique)

        self.button6 = Button (text = "Group Reactions")
        self.button6.bind(on_press =self.reactions)

        self.button7 = Button (text = "Sources")
        self.button7.bind(on_press =self.sources)

        self.window.add_widget(self.button)
        self.window.add_widget(self.button2)
        self.window.add_widget(self.button3)
        self.window.add_widget(self.button4)
        self.window.add_widget(self.button5)
        self.window.add_widget(self.button6)
        self.window.add_widget(self.button7)
        

        return self.window
    def pop_ada(self):
        pop = Popup(title = "ada", content = Image(source =os.path.join("Assets", "AdaSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_psychology(self):
        pop = Popup(title = "Psychology", content = Image(source =os.path.join("Assets", "PsychologySlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_lacking(self):
        pop = Popup(title = "lacking", content = Image(source =os.path.join("Assets", "LackingSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_sig(self):
        pop = Popup(title = "significance", content = Image(source =os.path.join("Assets", "SignificanceSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_unique(self):
        pop = Popup(title = "unique", content = Image(source =os.path.join("Assets", "UniqueSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_reaction(self):
        pop = Popup(title = "reactions", content = Image(source =os.path.join("Assets", "ReactionSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()
    def pop_sources(self):
        pop = Popup(title = "sources", content = Image(source =os.path.join("Assets", "SourcesSlide.png")),size_hint = (None,None), size =(1280,720))
        pop.open()

    def ada(self,instance):
        self.pop_ada()
    def psychology(self,instance):
        self.pop_psychology()
    def lacking(self,instance):
        self.pop_lacking()
    def sig(self,instance):
        self.pop_sig()
    def unique(self,instance):
        self.pop_unique()
    def reactions(self,instance):
        self.pop_reaction()
    def sources(self,instance):
        self.pop_sources()

if __name__ == "__main__":
    AdaLovelace().run()