# ==============================================
# PROJETO: Lista de Mercado — Arquivo PRINCIPAL
# ==============================================

from kivymd.app import MDApp
from kivy.lang import Builder
import os

# Importa a tela que criamos
from telas.tela_lista import TelaLista

# Carrega o arquivo de design (.kv)
Builder.load_file(os.path.join("design", "tela_lista.kv"))


class ListaMercadoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # Cor verde do app
        return TelaLista()  # Mostra nossa tela


# Rodar o aplicativo
if __name__ == "__main__":
    ListaMercadoApp().run()