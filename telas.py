from kivy.uix.screenmanager import ScreenManager, Screen
from popups import *
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import ColorProperty
from kivy.app import App
from kivy.uix.label import Label

# Cada página chama a classe Screen contendo as propriedades dela.

# Página principal, onde os carrinhos são selecionados.


class PrincipalPage(Screen):
   pass

# Páginas de seleção de lados. Cada número (SelecLadoXPage) refere-se ao carrinho.


class SelecLado1Page(Screen):
    pass


class SelecLado2Page(Screen):
    pass


class SelecLado3Page(Screen):
    pass


class SelecLado4Page(Screen):
    pass


class SelecLado5Page(Screen):
    pass


# Página de seleção de andares onde cada andar contém seu lado esquerdo e direito e seu número de carrinho.


class SelecAndar1DirPage(Screen):
    pass


class SelecAndar1EsqPage(Screen):
    pass


class SelecAndar2DirPage(Screen):
    pass


class SelecAndar2EsqPage(Screen):
    pass


class SelecAndar3DirPage(Screen):
    pass


class SelecAndar3EsqPage(Screen):
    pass


class SelecAndar4DirPage(Screen):
    pass


class SelecAndar4EsqPage(Screen):
    pass


class SelecAndar5DirPage(Screen):
    pass


class SelecAndar5EsqPage(Screen):
    pass

# Página de seleção das posições, contendo vários métodos para gravação e abertura do pop-up de seleção de endereço.
# PS: São várias páginas, referente a cada andar, totalizando 5 em cada lado, 10 em cada carrinho, 50 no total.


# Cada texto da posição (texto_a, texto_b, ...) é uma propriedade String da biblioteca Kivy (StringProperty).
# Com isso a propriedade text no arquivo .kv pode ser modificada.

# As funções de btn_a até btn_d fazem para abrir o pop-up de seleção de endereço
# As funções de label_a até label_d servem para pegar o endereço específico no pop-up e gravar na página.
# A função botao_ir serve para abrir o pop-up de confirmação e ir para as rotas.

class SelecPosicao1EsqA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1DirA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1EsqA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1DirA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1EsqA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1DirA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1EsqA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1DirA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1EsqA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao1DirA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2EsqA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2DirA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2EsqA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2DirA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2EsqA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2DirA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2EsqA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2DirA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2EsqA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao2DirA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3EsqA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3DirA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3EsqA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3DirA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3EsqA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3DirA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3EsqA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3DirA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3EsqA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao3DirA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4EsqA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4DirA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4EsqA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4DirA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4EsqA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4DirA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4EsqA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4DirA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4EsqA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao4DirA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5EsqA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5DirA1Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5EsqA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5DirA2Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5EsqA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5DirA3Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5EsqA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5DirA4Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5EsqA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()


class SelecPosicao5DirA5Page(Screen):
    texto_a = StringProperty('...')
    texto_b = StringProperty('...')
    texto_c = StringProperty('...')
    texto_d = StringProperty('...')

    # A
    def btn_a(self):
        SelLocalRegiao().open()

    def label_a(self, texto):
        self.texto_a = texto

    # B
    def btn_b(self):
        SelLocalRegiao().open()

    def label_b(self, texto):
        self.texto_b = texto

    # C
    def btn_c(self):
        SelLocalRegiao().open()

    def label_c(self, texto):
        self.texto_c = texto

    # D
    def btn_d(self):
        SelLocalRegiao().open()

    def label_d(self, texto):
        self.texto_d = texto

    def botao_ir(self):
        popup = Confirmar()
        popup.open()

# Página de escolha das rotas

# A função voltar_botao vai abrir um pop-up para confirmação para voltar sendo assim resetando os dados para padrão.


class EscolhaRotaPage(Screen):
    def voltar_botao(self):
        popup = Voltar()
        popup.open()

# Página de escolha das paradas em cada rota, conténdo métodos para separação de setores especificos

# Cada parada deixará os checks padrão em todos os carrinhos
# E após isso foi separado em uma lista (setores) especificando cada setor naquela parada

# A função parada_sel receberá qual parada está, referência do botão selecionado na rota.

# Se a parada é igual, os setores serão alterados e com esses setores pegarão os endereços que foram apontados nas
# páginas de seleção e colocar o check verde em sua posição específica.
# Utilizei as estruturas de repetição para percorrer em cada página de resultado e chamando o método mudar_cor().

class Rota01Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R01 C81MS090', 'R01 C81PA070', 'R01 C81MS070']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P02':
            setores = ['R01 C81MS060', 'R01 C81PA110', 'R01 C81MS050', 'R01 C81PA020']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P03':
            setores = ['R01 C81MS040', 'R01 C81MS030']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P04':
            setores = ['R01 C81MS020', 'R01 C81PA120']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P05':
            setores = ['R01 C81MS010', 'R01 C81PA010', 'R01 C81PA130']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')


class Rota0302Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R03 C81FL120', 'R03 C81FL110', 'R03 C81FL210',
                       'R03 C81FL220', 'R03 C81PA050']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P02':
            setores = ['R03 C81FL260', 'R03 C81PA030', 'R03 C81FL250',
                       'R03 C81FL240', 'R03 C81PA080']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P03':
            setores = ['R03 C81FL230', 'R03 C81PA090']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P04':
            setores = ['R03 C81FL310', 'R02 C81FL310', 'R03 C81PA060',
                       'R03 C81PA040', 'R03 C81FL320', 'R02 C81FL320']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P05':
            setores = ['R02 C81FL320', 'R03 C81PA100', 'R02 C81FL310']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')


class Rota04Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R04 C81FL120', 'R04 C81FL110', 'R04 C81PA030',
                       'R04 C82PA110']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P02':
            setores = ['R04 C82PA070', 'R04 C81PA090']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P03':
            setores = ['R04 C81PA060', 'R04 C82PA040']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P04':
            setores = ['R04 C81FL330', 'R04 C81PA100', 'R04 C81PA040']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P05':
            setores = ['R04 C82PA120', 'R04 C82PA100', 'R04 C82FL240',
                       'R04 C82FL230', 'R04 C82FL220']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')


class Rota05Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R05 C82PA120', 'R05 C82PA100', 'R05 C82FL240',
                       'R05 C82FL230', 'R05 C82FL220', 'R05 C82FL210', 'R05 C82MS080']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P02':
            setores = ['R05 C82MS050', 'R05 C82PA130']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P03':
            setores = ['R05 C82PA050', 'R05 C82MS040']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P04':
            setores = ['R05 C82MS030', 'R05 C82MS020', 'R05 C82PA080', 'R05 C82MS010']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P05':
            setores = ['R05 C82MS005', 'R05 C82PA010', 'R05 C82PA060', 'R05 C82PA020']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')


class Rota0607Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R06 C82MS005', 'R06 C82PA010', 'R06 C82PA030',
                       'R06 C82PA090', 'OUT G08', 'OUT PINTURA']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
        elif parada.split(' ')[1] == 'P02':
            setores = ['R06 C82MS010', 'R06 C82FL110']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
        elif parada.split(' ')[1] == 'P03':
            setores = ['R06 C82MS030', 'R06 C82MS040', 'R06 C82FL130',
                       'R07 C82FL110', 'R07 C82FL130']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
        elif parada.split(' ')[1] == 'P04':
            setores = ['R06 C82MS050', 'R06 C82FL120']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
        elif parada.split(' ')[1] == 'P05':
            setores = ['R06 C82MS080', 'R06 C82MS090']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)

        app.root.ids['rescarrinhopage'].mudar_label(parada)
        app.mudar_tela('rescarrinhopage')


class Rota08Page(Screen):
    def parada_sel(self, parada):
        app = App.get_running_app()
        for c in range(1, 6):
            app.root.ids[f'resladodir{c}page'].cor_padrao()
            app.root.ids[f'resladoesq{c}page'].cor_padrao()
            app.root.ids[f'resseleclado{c}page'].padrao()
        app.root.ids[f'rescarrinhopage'].padrao()
        if parada.split(' ')[1] == 'P01':
            setores = ['R08 SO5700', 'R08 SO5800', 'R08 SO7200', 'R08 SO5900',
                       'R08 SO5100', 'R08 SO5500', 'R08 SO1900', 'R08 SO7100', 'R08 SO0900']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P02':
            setores = ['R08 SO7500', 'R08 SO7000', 'R08 SO5300', 'R08 SO5600',
                       'R08 SO7300', 'R08 SO5400', 'R08 SO5000', 'R08 SO6000', 'R08 SO1200']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P03':
            setores = ['R08 SO1500', 'R08 SO1400', 'R08 SO1000', 'R08 SO16A0',
                       'R08 SO1600']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P04':
            setores = ['R08 SO0600', 'R08 SO01D0', 'R08 SO17A0']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P05':
            setores = ['R08 SO1800', 'R08 SO1300', 'R08 SO02A0', 'R08 SO0200',
                       'R08 SO0100', 'R08 SO01A0', 'R08 SO01E0']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')
        elif parada.split(' ')[1] == 'P06':
            setores = ['R08 SO0800', 'R08 SO0500', 'R08 SO0700']
            for c in range(1, 6):
                app.root.ids[f'resladodir{c}page'].mudar_cor(setores)
                app.root.ids[f'resladoesq{c}page'].mudar_cor(setores)
            app.root.ids['rescarrinhopage'].mudar_label(parada)
            app.mudar_tela('rescarrinhopage')


# Página de resultado de carrinhos

# Contém seus checks referenciando a qual carrinho está apontado (check_1, check_2)

# A função padrao() definirá os checks como padrão. Utilizado nas escolhas da parada, para resetar os checks padrão.

# A funçao check_padrão() tem o mesmo significado da função acima, pois ela serve para caso 2 ou mais carrinhos
# estiverem disponíveis, caso o usuário voltar de um carrinho que já tirou todas as embalagens disponíveis, e ir para o
# próximo carrinho, o carrinho anterior se tornará com check padrão, tornando mais dinâmico.

# A função check_carrinho() receberá qual carrinho está com disponibilidade e tornará o check em positivo.

# A função voltar_rota() serve para o usuário voltar em sua rota específica, a variável label_parada terá referência
# de qual rota e parada está, com a rota definida ele voltará para a mesma rota em que estava.

# A função mudar_label() receberá a parada_sel da escolha das paradas em cada rota, com isso ela definirá
# qual referência está e alterando a variável label_parada. Também fará um particionamento da string com método split()
# para definir a varíável rota.

# A função sel_carrinho() receberá o carrinho com o botão pressionado e mudará para o página do carrinho selecionado
# e alterando também a propriedade da label_parada.

class ResCarrinhoPage(Screen):
    label_parada = StringProperty('')
    check_1 = StringProperty('icones/error.png')
    check_2 = StringProperty('icones/error.png')
    check_3 = StringProperty('icones/error.png')
    check_4 = StringProperty('icones/error.png')
    check_5 = StringProperty('icones/error.png')
    rota = ''

    def padrao(self):
        self.check_1 = 'icones/error.png'
        self.check_2 = 'icones/error.png'
        self.check_3 = 'icones/error.png'
        self.check_4 = 'icones/error.png'
        self.check_5 = 'icones/error.png'

    def check_padrao(self, carrinho):
        if carrinho == '1':
            self.check_1 = 'icones/error.png'
        elif carrinho == '2':
            self.check_2 = 'icones/error.png'
        elif carrinho == '3':
            self.check_3 = 'icones/error.png'
        elif carrinho == '4':
            self.check_4 = 'icones/error.png'
        elif carrinho == '5':
            self.check_5 = 'icones/error.png'

    def check_carrinho(self, carrinho):
        if carrinho == '1':
            self.check_1 = 'icones/check.png'
        elif carrinho == '2':
            self.check_2 = 'icones/check.png'
        elif carrinho == '3':
            self.check_3 = 'icones/check.png'
        elif carrinho == '4':
            self.check_4 = 'icones/check.png'
        elif carrinho == '5':
            self.check_5 = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        if self.rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif self.rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{self.rota[2]}page')
        self.check_1 = 'icones/error.png'
        self.check_2 = 'icones/error.png'
        self.check_3 = 'icones/error.png'
        self.check_4 = 'icones/error.png'
        self.check_5 = 'icones/error.png'

    def mudar_label(self, parada_sel):
        self.rota = parada_sel.split(' ')[0]
        self.label_parada = f'LOCAL: {parada_sel}'

    def sel_carrinho(self, carrinho):
        app = App.get_running_app()
        app.mudar_tela(f'resseleclado{carrinho}page')
        app.root.ids[f'resseleclado{carrinho}page'].label_local(self.label_parada)
        app.root.ids[f'resladoesq{carrinho}page'].label_local(self.label_parada)
        app.root.ids[f'resladodir{carrinho}page'].label_local(self.label_parada)

# Página de seleção de lados disponíveis

# Terá dois checks, especificando os lados. (check_dir, check_esq)

# O método padrao() definirá os checks em padrão

# O método check_padrao() recebe qual lado foi selecionado, assim o usuário terminado de fazer pagamento em um lado
# voltando para a seleção de lados, o lado em que ele estava tornará padrão.

# O método check_lado() receberá qual lado tem disponibilidade e tornará o check positivo.

# O método voltar_rota() servirá para voltar a rota específica, mesmo método da classe ResCarrinhoPage() e
# tornará padrão os checks de lado.

# O método voltar_carrinho() voltará para seleção de carrinhos disponíveis e tornando padrão
# os checks de lado e do carrinho que estava

# O método label_local() é a referência da rota e parada em que está.


class ResSelecLado1Page(Screen):
    label_parada = StringProperty('')
    check_dir = StringProperty('icones/error.png')
    check_esq = StringProperty('icones/error.png')

    def padrao(self):
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def check_padrao(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/error.png'
        if lado == 'esq':
            self.check_esq = 'icones/error.png'

    def check_lado(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/check.png'
        elif lado == 'esq':
            self.check_esq = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def voltar_carrinho(self):
        app = App.get_running_app()
        page_carrinho = app.root.ids['rescarrinhopage']
        page_carrinho.check_1 = 'icones/error.png'
        app.mudar_tela('rescarrinhopage')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def label_local(self, parada):
        self.label_parada = parada


class ResSelecLado2Page(Screen):
    label_parada = StringProperty('')
    check_dir = StringProperty('icones/error.png')
    check_esq = StringProperty('icones/error.png')

    def padrao(self):
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def check_padrao(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/error.png'
        if lado == 'esq':
            self.check_esq = 'icones/error.png'

    def check_lado(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/check.png'
        elif lado == 'esq':
            self.check_esq = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def voltar_carrinho(self):
        app = App.get_running_app()
        page_carrinho = app.root.ids['rescarrinhopage']
        page_carrinho.check_2 = 'icones/error.png'
        app.mudar_tela('rescarrinhopage')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def label_local(self, parada):
        self.label_parada = parada


class ResSelecLado3Page(Screen):
    label_parada = StringProperty('')
    check_dir = StringProperty('icones/error.png')
    check_esq = StringProperty('icones/error.png')

    def padrao(self):
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def check_padrao(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/error.png'
        if lado == 'esq':
            self.check_esq = 'icones/error.png'

    def check_lado(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/check.png'
        elif lado == 'esq':
            self.check_esq = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def voltar_carrinho(self):
        app = App.get_running_app()
        page_carrinho = app.root.ids['rescarrinhopage']
        page_carrinho.check_3 = 'icones/error.png'
        app.mudar_tela('rescarrinhopage')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def label_local(self, parada):
        self.label_parada = parada


class ResSelecLado4Page(Screen):
    label_parada = StringProperty('')
    check_dir = StringProperty('icones/error.png')
    check_esq = StringProperty('icones/error.png')

    def padrao(self):
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def check_padrao(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/error.png'
        if lado == 'esq':
            self.check_esq = 'icones/error.png'

    def check_lado(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/check.png'
        elif lado == 'esq':
            self.check_esq = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def voltar_carrinho(self):
        app = App.get_running_app()
        page_carrinho = app.root.ids['rescarrinhopage']
        page_carrinho.check_4 = 'icones/error.png'
        app.mudar_tela('rescarrinhopage')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def label_local(self, parada):
        self.label_parada = parada


class ResSelecLado5Page(Screen):
    label_parada = StringProperty('')
    check_dir = StringProperty('icones/error.png')
    check_esq = StringProperty('icones/error.png')

    def padrao(self):
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def check_padrao(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/error.png'
        if lado == 'esq':
            self.check_esq = 'icones/error.png'

    def check_lado(self, lado):
        if lado == 'dir':
            self.check_dir = 'icones/check.png'
        elif lado == 'esq':
            self.check_esq = 'icones/check.png'

    def voltar_rota(self):
        app = App.get_running_app()
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def voltar_carrinho(self):
        app = App.get_running_app()
        page_carrinho = app.root.ids['rescarrinhopage']
        page_carrinho.check_5 = 'icones/error.png'
        app.mudar_tela('rescarrinhopage')
        self.check_dir = 'icones/error.png'
        self.check_esq = 'icones/error.png'

    def label_local(self, parada):
        self.label_parada = parada


# Página de resultado dos carrinhos.

# Cada posição do carrinho contém um botão com sua propriedade de cor, padrão em vermelho.

# O método cor_padrão() definirá todas as posições de cor padrão.

# O método mudar_cor() é o método que utilizará para mudar as cores das posições.
# Primeiro o método percorre em uma estrutura de repetição de cada andar, sendo de 1 a 5, e definirá a variável page,
# sendo selecposicao1dirA{andar}, após isso, cada andar tem sua posição (A, B, C, D), como já foram definidos acima,
# como texto_a, texto_b, texto_c e texto_d.
# Sendo assim, ele validará se o endereço nesse texto é o mesmo que contém na lista de setores, pois o método
# vai receber a lista de setores onde o método será chamado lá na seleção de paradas das rotas. E com isso ele tornará
# o check na cor verde, tornando disponível, também mudará o lado em que está selecionado e também o carrinho.

# O método voltar_rota() é o mesmo segmento utilizado antes, porém tornando os checks das posições padrão

# O método voltar_res_carrinho() serve para voltar ao carrinho e tornando os checks padrão.

# O método check_posição() é o comando de cada botão das posições, abrindo um pop-up especificando qual é o endereço.

# O método label_local() é a referência da rota e parada em qual está.

class ResLadoDir1Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        app = App.get_running_app()
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao1dirA{andar}']
            check_carrinho = app.root.ids['rescarrinhopage']
            check_lado = app.root.ids[f'resseleclado1page']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('dir')


    def voltar_rota(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado1page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('1')
        check_lado.check_padrao('dir')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado1page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('1')
        check_lado.check_padrao('dir')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado1page']
        app.mudar_tela('resseleclado1page')
        self.cor_padrao()
        check_lado.check_padrao('dir')


    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao1dir{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoEsq1Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado1page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao1esqA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('1')
                            check_lado.check_lado('esq')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado1page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('1')
        check_lado.check_padrao('esq')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado1page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('1')
        check_lado.check_padrao('esq')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado1page']
        app.mudar_tela('resseleclado1page')
        self.cor_padrao()
        check_lado.check_padrao('esq')


    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao1esq{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()


    def label_local(self, parada):
        self.label_parada = parada


class ResLadoDir2Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao2dirA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('dir')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('2')
        check_lado.check_padrao('dir')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('2')
        check_lado.check_padrao('dir')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado2page']
        app.mudar_tela('resseleclado2page')
        self.cor_padrao()
        check_lado.check_padrao('dir')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao2dir{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()


    def label_local(self, parada):
        self.label_parada = parada


class ResLadoEsq2Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao2esqA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('2')
                            check_lado.check_lado('esq')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('2')
        check_lado.check_padrao('esq')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado2page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('2')
        check_lado.check_padrao('esq')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado2page']
        app.mudar_tela('resseleclado2page')
        self.cor_padrao()
        check_lado.check_padrao('esq')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao2esq{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoDir3Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao3dirA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('dir')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('3')
        check_lado.check_padrao('dir')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('3')
        check_lado.check_padrao('dir')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado3page']
        app.mudar_tela('resseleclado3page')
        self.cor_padrao()
        check_lado.check_padrao('dir')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao3dir{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoEsq3Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao3esqA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('3')
                            check_lado.check_lado('esq')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('3')
        check_lado.check_padrao('esq')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado3page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('3')
        check_lado.check_padrao('esq')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado3page']
        app.mudar_tela('resseleclado3page')
        self.cor_padrao()
        check_lado.check_padrao('esq')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao3esq{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoDir4Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao4dirA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('dir')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('4')
        check_lado.check_padrao('dir')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('4')
        check_lado.check_padrao('dir')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado4page']
        app.mudar_tela('resseleclado4page')
        self.cor_padrao()
        check_lado.check_padrao('dir')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao4dir{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoEsq4Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao4esqA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('4')
                            check_lado.check_lado('esq')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('4')
        check_lado.check_padrao('esq')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado4page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('4')
        check_lado.check_padrao('esq')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado4page']
        app.mudar_tela('resseleclado4page')
        self.cor_padrao()
        check_lado.check_padrao('esq')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao4esq{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoDir5Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao5dirA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('dir')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('5')
        check_lado.check_padrao('dir')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('5')
        check_lado.check_padrao('dir')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado5page']
        app.mudar_tela('resseleclado5page')
        self.cor_padrao()
        check_lado.check_padrao('dir')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao5dir{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada


class ResLadoEsq5Page(Screen):
    cor_vermelha = (0.99, 0.29, 0.28, 0.93)
    label_parada = StringProperty('')
    cor_a_5 = ColorProperty(cor_vermelha)
    cor_b_5 = ColorProperty(cor_vermelha)
    cor_c_5 = ColorProperty(cor_vermelha)
    cor_d_5 = ColorProperty(cor_vermelha)
    cor_a_4 = ColorProperty(cor_vermelha)
    cor_b_4 = ColorProperty(cor_vermelha)
    cor_c_4 = ColorProperty(cor_vermelha)
    cor_d_4 = ColorProperty(cor_vermelha)
    cor_a_3 = ColorProperty(cor_vermelha)
    cor_b_3 = ColorProperty(cor_vermelha)
    cor_c_3 = ColorProperty(cor_vermelha)
    cor_d_3 = ColorProperty(cor_vermelha)
    cor_a_2 = ColorProperty(cor_vermelha)
    cor_b_2 = ColorProperty(cor_vermelha)
    cor_c_2 = ColorProperty(cor_vermelha)
    cor_d_2 = ColorProperty(cor_vermelha)
    cor_a_1 = ColorProperty(cor_vermelha)
    cor_b_1 = ColorProperty(cor_vermelha)
    cor_c_1 = ColorProperty(cor_vermelha)
    cor_d_1 = ColorProperty(cor_vermelha)

    def cor_padrao(self):
        self.cor_a_5 = self.cor_vermelha
        self.cor_b_5 = self.cor_vermelha
        self.cor_c_5 = self.cor_vermelha
        self.cor_d_5 = self.cor_vermelha
        self.cor_a_4 = self.cor_vermelha
        self.cor_b_4 = self.cor_vermelha
        self.cor_c_4 = self.cor_vermelha
        self.cor_d_4 = self.cor_vermelha
        self.cor_a_3 = self.cor_vermelha
        self.cor_b_3 = self.cor_vermelha
        self.cor_c_3 = self.cor_vermelha
        self.cor_d_3 = self.cor_vermelha
        self.cor_a_2 = self.cor_vermelha
        self.cor_b_2 = self.cor_vermelha
        self.cor_c_2 = self.cor_vermelha
        self.cor_d_2 = self.cor_vermelha
        self.cor_a_1 = self.cor_vermelha
        self.cor_b_1 = self.cor_vermelha
        self.cor_c_1 = self.cor_vermelha
        self.cor_d_1 = self.cor_vermelha

    def mudar_cor(self, setores):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        cor_verde = (0.08, 0.99, 0.32, 0.93)
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        for andar in range(1, 6):
            page = app.root.ids[f'selecposicao5esqA{andar}']
            if andar == 1:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_1 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
            elif andar == 2:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_2 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
            elif andar == 3:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_3 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
            elif andar == 4:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_4 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
            elif andar == 5:
                for pos in range(1, 5):
                    if pos == 1:
                        if page.texto_a in setores:
                            self.cor_a_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 2:
                        if page.texto_b in setores:
                            self.cor_b_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 3:
                        if page.texto_c in setores:
                            self.cor_c_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')
                    elif pos == 4:
                        if page.texto_d in setores:
                            self.cor_d_5 = cor_verde
                            check_carrinho.check_carrinho('5')
                            check_lado.check_lado('esq')

    def voltar_rota(self):
        cor_vermelha = (0.99, 0.29, 0.28, 0.93)
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        rota = app.root.ids['rescarrinhopage'].rota
        if rota[2] == '3':
            app.mudar_tela(f'rota0302page')
        elif rota[2] == '6':
            app.mudar_tela(f'rota0607page')
        else:
            app.mudar_tela(f'rota0{rota[2]}page')
        self.cor_padrao()
        check_carrinho.check_padrao('5')
        check_lado.check_padrao('esq')

    def voltar_res_carrinho(self):
        app = App.get_running_app()
        check_carrinho = app.root.ids['rescarrinhopage']
        check_lado = app.root.ids[f'resseleclado5page']
        app.mudar_tela('rescarrinhopage')
        self.cor_padrao()
        check_carrinho.check_padrao('5')
        check_lado.check_padrao('esq')

    def voltar_lado(self):
        app = App.get_running_app()
        check_lado = app.root.ids[f'resseleclado5page']
        app.mudar_tela('resseleclado5page')
        self.cor_padrao()
        check_lado.check_padrao('esq')

    def check_posicao(self, andar, posicao):
        app = App.get_running_app()
        popup = ResCheck()
        page = app.root.ids[f'selecposicao5esq{andar}']
        if posicao == 'a':
            texto = page.texto_a
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'b':
            texto = page.texto_b
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'c':
            texto = page.texto_c
            popup.mudar_texto(texto)
            popup.open()
        elif posicao == 'd':
            texto = page.texto_d
            popup.mudar_texto(texto)
            popup.open()

    def label_local(self, parada):
        self.label_parada = parada

