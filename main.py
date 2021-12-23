from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols=1

        self.new_layout = GridLayout()
        self.new_layout.cols = 2

        self.add_widget(self.new_layout)

        self.new_layout.add_widget(Label(text='Name', font_size=32))
        self.name = TextInput(multiline=False, font_size=32)
        self.new_layout.add_widget(self.name)

        self.new_layout.add_widget(Label(text='Family', font_size=32))
        self.family = TextInput(multiline=False, font_size=32)
        self.new_layout.add_widget(self.family)

        self.new_layout.add_widget(Label(text='Class', font_size=32))
        self.Class = TextInput(multiline=False, font_size=32)
        self.new_layout.add_widget(self.Class)

        self.submit=Button(text="Submit", font_size=32)
        self.submit.bind(on_release=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        family = self.family.text
        Class = self.Class.text

        if name and family and Class:
            self.add_widget(Label(text=f"Hello {name} {family} , your Class is {Class}"))

            self.name.text=""
            self.family.text=""
            self.Class.text=""


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()