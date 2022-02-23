from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
import telas
from telas import *
from botoes import *
from popups import *
from kivy.metrics import dp, sp
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()


GUI = Builder.load_file("main.kv")

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_tela_pos = ''
        self.text_pos = ''

    def build(self):
        return GUI

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    def id_tela(self, id_tela, text):
        self.id_tela_pos = id_tela
        self.text_pos = text


MainApp().run()
