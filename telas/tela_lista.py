# ==============================================
# TELA: Lista de Produtos
# ==============================================
# ==============================================
# TELA: Lista de Produtos — Versão KivyMD 2.x
# ==============================================

from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText

class TelaLista(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Nossa lista de produtos
        self.lista_produtos = []

        # Layout principal
        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        # Título
        titulo = MDLabel(
            text="🛒 Lista de Mercado",
            font_style="Headline",
            halign="center"
        )
        self.layout.add_widget(titulo)

        # Área onde aparece a lista
        self.texto_lista = MDLabel(
            text="📋 Adicione produtos para ver sua lista aqui!",
            halign="left"
        )
        self.layout.add_widget(self.texto_lista)


        botao_limpar = MDButton(
            MDButtonText(text="Limpar Lista"),
            style="elevated",  # ← faz o botão parecido com o antigo
            pos_hint={"center_x": 0.5},
            on_press=self.limpar_lista  
        )

        self.layout.add_widget(botao_limpar)

        # Adiciona tudo na tela
        self.add_widget(self.layout)

    # ✅ Função: Adicionar produto
    def adicionar_produto(self, nome, quantidade, preco):
        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
        self.lista_produtos.append(produto)
        self.atualizar_visualizacao()

    # ✅ Função: Atualizar a tela com os produtos
    def atualizar_visualizacao(self):
        if not self.lista_produtos:
            self.texto_lista.text = "📋 Lista vazia!"
            return

        texto = "\n📋 PRODUTOS:\n"
        total_geral = 0

        for numero, prod in enumerate(self.lista_produtos, start=1):
            subtotal = prod["quantidade"] * prod["preco"]
            total_geral += subtotal
            texto += f"{numero}. {prod['nome']}\n   Qtd: {prod['quantidade']} | R$ {prod['preco']:.2f} | Subtotal: R$ {subtotal:.2f}\n"

        texto += f"\n💡 TOTAL DA COMPRA: R$ {total_geral:.2f}"
        self.texto_lista.text = texto

    # ✅ Função: Limpar a lista
    def limpar_lista(self, instancia):
        self.lista_produtos.clear()
        self.texto_lista.text = "📋 Lista limpa! Adicione novos produtos."