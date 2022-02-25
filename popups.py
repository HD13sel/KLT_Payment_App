from kivy.factory import Factory
from telas import *
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.app import App


# Pop-up Confirmar

# Confirmação após o botão 'PRONTO'
# Faz confirmação mudando a tela com o método principal mudar_tela()
class Confirmar(Popup):
    pass


# Pop-up Voltar

# Voltar da página escolha das rotas

# O método voltar_botão(), fazerá que todas as posições em cada carrinho serão resetados para padrão
class Voltar(Popup):
    txt = '...'

    def voltar_botao(self):
        app = App.get_running_app()
        for c in range(1, 6):
            for a in range(1, 6):
                for pos in range(1, 5):
                    if pos == 1:
                        app.root.ids[f'selecposicao{c}dirA{a}'].texto_a = self.txt
                        app.root.ids[f'selecposicao{c}esqA{a}'].texto_a = self.txt
                    if pos == 2:
                        app.root.ids[f'selecposicao{c}dirA{a}'].texto_b = self.txt
                        app.root.ids[f'selecposicao{c}esqA{a}'].texto_b = self.txt
                    if pos == 3:
                        app.root.ids[f'selecposicao{c}dirA{a}'].texto_c = self.txt
                        app.root.ids[f'selecposicao{c}esqA{a}'].texto_c = self.txt
                    if pos == 4:
                        app.root.ids[f'selecposicao{c}dirA{a}'].texto_d = self.txt
                        app.root.ids[f'selecposicao{c}esqA{a}'].texto_d = self.txt
        app.mudar_tela('principalpage')


# Pop-up LocalRegiao

# Aparecerá após selecionar a posição, com ele vai definir qual endereço está nessa posição (C81, C82, SOLDA, OUTROS)
# E cada botão é um método de referência a região, abrindo outro pop-up, pois cada classe chama a classe Popup.

# O método apagar serve para tornar aquela posição com o texto padrão.
class SelLocalRegiao(Popup):
    def c81(self):
        SelLocalRotasC81().open()

    def c82(self):
        SelLocalRotasC82().open()

    def solda(self):
        SelLocalRotasSolda().open()

    def outros(self):
        SelLocalRotasOutros().open()

    def apagar(self):
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'...'
        destino.open()


# Pop-up C81

# Cada rota do setor abrirá o pop-up próprio.
# O método voltar_'setor'() voltará no pop-up anterior em que estava.
class SelLocalRotasC81(Popup):
    def c81_r01(self):
        SelLocalRotasC81R01().open()

    def c81_r02(self):
        SelLocalRotasC81R02().open()

    def c81_r03(self):
        SelLocalRotasC81R03().open()

    def c81_r04(self):
        SelLocalRotasC81R04().open()

    def voltar_c81(self):
        SelLocalRegiao().open()


# Pop-up C82
class SelLocalRotasC82(Popup):
    def c82_r04(self):
        SelLocalRotasC82R04().open()

    def c82_r05(self):
        SelLocalRotasC82R05().open()

    def c82_r06(self):
        SelLocalRotasC82R06().open()

    def c82_r07(self):
        SelLocalRotasC82R07().open()

    def voltar_c82(self):
        SelLocalRegiao().open()


# Pop-up SOLDA

# No setor da solda, cada endereço foi ordenado, contendo no seu arquivo .kv um ScrollView para tornar mais dinâmico.
# O método escolha_solda() receberá qual botão foi pressionado nos endereços disponíveis
# e enviará para o Pop-up SelLocal(). Com sua formatação de endereço.
class SelLocalRotasSolda(Popup):
    def escolha_solda(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R08 SO{text}'
        destino.open()

    def voltar_solda(self):
        SelLocalRegiao().open()


# Pop-up Outros

# Na região de outros, são especificado setores como Pintura e área RIP G08.
class SelLocalRotasOutros(Popup):
    def escolha_out(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'OUT {text}'
        destino.open()

    def voltar_out(self):
        SelLocalRegiao().open()


# Pop-up R01-C81
class SelLocalRotasC81R01(Popup):
    def escolha_c81_r01(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R01 C81{text}'
        destino.open()

    def voltar_local_c81_r01(self):
        SelLocalRotasC81().open()


# Pop-up R02-C81
class SelLocalRotasC81R02(Popup):
    def escolha_c81_r02(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R02 C81{text}'
        destino.open()

    def voltar_local_c81_r02(self):
        SelLocalRotasC81().open()


# Pop-up R03-C81
class SelLocalRotasC81R03(Popup):
    def escolha_c81_r03(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R03 C81{text}'
        destino.open()

    def voltar_local_c81_r03(self):
        SelLocalRotasC81().open()


# Pop-up R04-C81
class SelLocalRotasC81R04(Popup):
    def escolha_c81_r04(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R04 C81{text}'
        destino.open()

    def voltar_local_c81_r04(self):
        SelLocalRotasC81().open()

# Pop-up R04-C82
class SelLocalRotasC82R04(Popup):
    def escolha_c82_r04(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R04 C82{text}'
        destino.open()

    def voltar_local_c82_r04(self):
        SelLocalRotasC82().open()

# Pop-up R05-C82
class SelLocalRotasC82R05(Popup):
    def escolha_c82_r05(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R05 C82{text}'
        destino.open()

    def voltar_local_c82_r05(self):
        SelLocalRotasC82().open()

# Pop-up R06-C82
class SelLocalRotasC82R06(Popup):
    def escolha_c82_r06(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R06 C82{text}'
        destino.open()

    def voltar_local_c82_r06(self):
        SelLocalRotasC82().open()


# Pop-up R07-C82
class SelLocalRotasC82R07(Popup):
    def escolha_c82_r07(self, btn_id):
        text = btn_id.text
        destino = SelLocal()
        end_sel = destino.ids['end_selec']
        end_sel.text = f'R07 C82{text}'
        destino.open()

    def voltar_local_c82_r07(self):
        SelLocalRotasC82().open()


# Pop-up SelLocal

# O método voltar_local() fará um particionamento da string para separar a rota e a linha.
# Com isso, utilizando um estrutura condicional fará o retorno específico na rota/linha em que estava.

# O método sel_ok() é o método onde vai pegar o texto do endereço selecionado e modificará o texto que está na página
# das posições do carrinho.
class SelLocal(Popup):
    def voltar_local(self):
        text = self.ids['end_selec'].text
        if len(text.split()) > 1:
            textconv = text.split()
            linha = textconv[1][0:3]
            rota = textconv[0]
            local = textconv[1][3:]
            if rota == 'OUT':
                SelLocalRotasOutros().open()
            if rota == 'R01' and linha == 'C81':
                SelLocalRotasC81R01().open()
            if rota == 'R02' and linha == 'C81':
                SelLocalRotasC81R02().open()
            if rota == 'R03' and linha == 'C81':
                SelLocalRotasC81R03().open()
            if rota == 'R04' and linha == 'C81':
                SelLocalRotasC81R04().open()
            if rota == 'R04' and linha == 'C82':
                SelLocalRotasC82R04().open()
            if rota == 'R05' and linha == 'C82':
                SelLocalRotasC82R05().open()
            if rota == 'R06' and linha == 'C82':
                SelLocalRotasC82R06().open()
            if rota == 'R07' and linha == 'C82':
                SelLocalRotasC82R07().open()
            if rota == 'R08':
                SelLocalRotasSolda().open()
        else:
            SelLocalRegiao().open()

    def sel_ok(self):
        app = App.get_running_app()
        tela = app.id_tela_pos
        btn_text = app.text_pos
        end_selec = self.ids['end_selec'].text
        page = app.root.ids[f'{tela}']
        if 'a' in btn_text:
            page.label_a(end_selec)
        elif 'b' in btn_text:
            page.label_b(end_selec)
        elif 'c' in btn_text:
            page.label_c(end_selec)
        elif 'd' in btn_text:
            page.label_d(end_selec)


# Pop-up ResCheck

# Mostrará qual endereço está na posição do carrinho, na página de resultados dos carrinhos.

# O método mudar_texto() receberá o texto do botão pressionado e mudará o texto.
class ResCheck(Popup):
    texto = StringProperty('')

    def mudar_texto(self, texto):
        self.texto = texto

