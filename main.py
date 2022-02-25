from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
import telas
from telas import *
from popups import *
from kivy.metrics import dp, sp
import os
import certifi

# Permissão para geração do aplicativo
os.environ["SSL_CERT_FILE"] = certifi.where()

# Leitura dos arquivos.kv
GUI = Builder.load_file("main.kv")


# Classe do aplicativo principal
class MainApp(App):
    # Método incializador onde apenas terá 2 variáveis para especificar qual tela e texto de referência.
    # Além também de chamar os atributos principais com super()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_tela_pos = ''
        self.text_pos = ''

    # Método de construção com os arquivos .kv que retornará a parte de design.
    def build(self):
        return GUI

    # Método principal para mudança de telas
    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    # Método para buscar o id da tela e o texto de referência e mudar as variáveis da classe principal.
    def id_tela(self, id_tela, text):
        self.id_tela_pos = id_tela
        self.text_pos = text

# Função principal para executar
MainApp().run()
