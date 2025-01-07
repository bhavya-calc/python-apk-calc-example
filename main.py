import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grid(BoxLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.Ans_screen = TextInput(size_hint=(1, .2), halign="right", text="0", font_size=70)
        self.add_widget(self.Ans_screen)
        self.innergrid = GridLayout()
        self.innergrid.cols = 4
        self.innergrid.rows = 5
        self.innergrid.clearscreen = Button(text="C", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x:self.clearscreen())
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text=u"\u00AB", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.clearscreen())
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="**", size_hint=(.2, .2), background_color=(25/255, 25/255, 25/255, 1), font_size=40,
                                            on_press=lambda x: self.operation(sign="**"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="/", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.operation(sign="/"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="9", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="9"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="8", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="8"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="7", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="7"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="*", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.operation(sign="*"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="6", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="6"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="5", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="5"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="4", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button=4))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="-", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.operation(sign="-"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="3", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="3"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="2", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="2"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="1", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="1"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="+", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.operation(sign="+"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="+/-", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.symbol_change())
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="0", size_hint=(.2, .2), font_size=40,
                                            on_press=lambda x: self.enter_no(button="0"))
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text=".", size_hint=(.2, .2),
                                            on_press=lambda x: self.point())
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.innergrid.clearscreen = Button(text="=", size_hint=(.2, .2), font_size=40, background_color=(25/255, 25/255, 25/255, 1),
                                            on_press=lambda x: self.equal())
        self.innergrid.add_widget(self.innergrid.clearscreen)
        self.add_widget(self.innergrid)


    def clearscreen(self):
        self.Ans_screen.text = "0"

    def enter_no(self,button):
        before_var = self.Ans_screen.text

        if before_var == "0" or before_var == "Can\'t Evaluate":
            self.Ans_screen.text = ""
            self.Ans_screen.text = f"{button}"
        else:
            self.Ans_screen.text = f"{before_var}{button}"

    def operation(self,sign):
        before_var = self.Ans_screen.text
        self.Ans_screen.text = f"{before_var}{sign}"

    def point(self):
        before_var = self.Ans_screen.text
        nos = before_var.split("+")
        if "+" in before_var and "." not in nos[-1]:
            self.Ans_screen.text = f"{before_var}."
        elif "." in before_var:
            pass
        else:
            self.Ans_screen.text = f"{before_var}."

    def back(self):
        before_var = self.Ans_screen.text
        self.Ans_screen.text = f"{before_var[:-1]}"

    def symbol_change(self):
        before_var = self.Ans_screen.text
        if "-" in before_var:
            self.Ans_screen.text = f"{before_var.replace('-',"")}"
        else:
            self.Ans_screen.text = f"-{before_var}"



    def equal(self):
        try:
            before_var = self.Ans_screen.text
            self.Ans_screen.text = f"{eval(before_var)}"
        except:
            self.Ans_screen.text = "Can\'t Evaluate"


class this_is_calcApp(App):
    def build(self):
        return Grid()


if __name__ == '__main__':
    this_is_calcApp().run()