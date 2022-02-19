from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string('''
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Hello world'
    BoxLayout:
        text_input: text_input
        orientation: 'vertical'
        TextInput:
            id: text_input
        Button:
            text: 'dismiss'    
            on_press: root.dismiss()
''')

class CustomPopup(Popup):
    pass

class TestApp(App):
    popup_text = StringProperty()

    def build(self):
        l = BoxLayout()
        l.add_widget(Button(
            text='show_popup', on_press=self.show_popup
        ))
        l.add_widget(Button(
            text='print popup text', on_press=self.print_popup_text
        ))
        return l

    def show_popup(self, *args):
        p = CustomPopup()
        p.content.text_input.bind(text=self.setter('popup_text'))
        p.open()

    def print_popup_text(self, *args):
        print(self.popup_text)

if __name__ == '__main__':
    TestApp().run()