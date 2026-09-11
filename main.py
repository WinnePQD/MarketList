import os
import sys
import importlib.util

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


# ============================================================
# CAMINHO DO PROJETO
# ============================================================

base_path = os.path.dirname(os.path.abspath(__file__))

if base_path not in sys.path:
    sys.path.insert(0, base_path)


# ============================================================
# PASTAS DO PROJETO
# ============================================================

# Onde ficam os arquivos Python das telas
screens_folder = os.path.join(
    base_path,
    "telas"
)

# Onde ficam os arquivos KV
kv_folder = os.path.join(
    base_path,
    "design"
)


# ============================================================
# CARREGAR TELAS
# ============================================================

def carregar_telas_dinamicamente():

    """
    Procura todos os arquivos .py dentro da pasta telas/
    e carrega automaticamente o arquivo .kv correspondente
    dentro da pasta kv/.

    Exemplo:

        telas/tela_inicial.py
        kv/tela_inicial.kv
    """

    telas = []


    # --------------------------------------------------------
    # Verifica a pasta telas
    # --------------------------------------------------------

    if not os.path.exists(screens_folder):

        raise FileNotFoundError(
            f"\nA pasta 'telas' não foi encontrada!\n\n"
            f"Caminho:\n{screens_folder}"
        )


    # --------------------------------------------------------
    # Verifica a pasta kv
    # --------------------------------------------------------

    if not os.path.exists(kv_folder):

        raise FileNotFoundError(
            f"\nA pasta 'kv' não foi encontrada!\n\n"
            f"Caminho:\n{kv_folder}"
        )


    # --------------------------------------------------------
    # Percorre os arquivos Python
    # --------------------------------------------------------

    for filename in sorted(os.listdir(screens_folder)):

        # Somente arquivos .py
        if not filename.endswith(".py"):
            continue

        # Ignora __init__.py
        if filename.startswith("__"):
            continue


        # ----------------------------------------------------
        # Nome da tela
        # ----------------------------------------------------

        # Exemplo:
        #
        # tela_inicial.py
        #
        # vira:
        #
        # tela_inicial

        module_name = filename[:-3]


        # Caminho do arquivo Python

        filepath = os.path.join(
            screens_folder,
            filename
        )


        print()
        print("=" * 50)
        print(f"CARREGANDO TELA: {module_name}")


        # ----------------------------------------------------
        # Procura o KV correspondente
        # ----------------------------------------------------

        kv_file = os.path.join(
            kv_folder,
            module_name + ".kv"
        )


        # ----------------------------------------------------
        # Carrega o KV
        # ----------------------------------------------------

        if os.path.exists(kv_file):

            print(
                f"Carregando KV: "
                f"{module_name}.kv"
            )

            Builder.load_file(kv_file)

            print("✓ KV carregado")

        else:

            print(
                f"⚠ AVISO: "
                f"{module_name}.kv não encontrado"
            )


        # ----------------------------------------------------
        # Cria o módulo Python
        # ----------------------------------------------------

        spec = importlib.util.spec_from_file_location(
            module_name,
            filepath
        )


        if spec is None or spec.loader is None:

            print(
                f"✗ Não foi possível carregar "
                f"{filename}"
            )

            continue


        module = importlib.util.module_from_spec(spec)


        # Executa o arquivo Python
        spec.loader.exec_module(module)


        print(
            f"✓ Python carregado: "
            f"{filename}"
        )


        # ----------------------------------------------------
        # Procura uma classe MDScreen
        # ----------------------------------------------------

        tela_encontrada = False


        for nome_classe in dir(module):

            obj = getattr(module, nome_classe)


            try:

                if (
                    isinstance(obj, type)
                    and issubclass(obj, MDScreen)
                    and obj is not MDScreen
                ):

                    # ----------------------------------------
                    # Cria a tela
                    # ----------------------------------------

                    tela = obj(
                        name=module_name
                    )


                    telas.append(tela)


                    tela_encontrada = True


                    print(
                        f"✓ Classe encontrada: "
                        f"{nome_classe}"
                    )

                    print(
                        f"✓ Nome da tela: "
                        f"{module_name}"
                    )


                    break


            except TypeError:

                pass


        # ----------------------------------------------------
        # Nenhuma tela encontrada
        # ----------------------------------------------------

        if not tela_encontrada:

            print(
                f"✗ Nenhuma classe MDScreen "
                f"encontrada em {filename}"
            )


    # --------------------------------------------------------
    # Resultado
    # --------------------------------------------------------

    print()
    print("=" * 50)
    print(
        f"TOTAL DE TELAS: {len(telas)}"
    )
    print("=" * 50)
    print()


    return telas


# ============================================================
# SCREEN MANAGER
# ============================================================

class GerenciadorTelas(ScreenManager):
    pass


# ============================================================
# APLICAÇÃO
# ============================================================

class ListaMercadoApp(MDApp):

    def build(self):

        # ----------------------------------------------------
        # Tema
        # ----------------------------------------------------

        self.theme_cls.primary_palette = "Green"


        # ----------------------------------------------------
        # Carrega as telas
        # ----------------------------------------------------

        telas = carregar_telas_dinamicamente()


        # ----------------------------------------------------
        # Cria o ScreenManager
        # ----------------------------------------------------

        sm = GerenciadorTelas()


        # ----------------------------------------------------
        # Adiciona as telas
        # ----------------------------------------------------

        for tela in telas:

            sm.add_widget(tela)


        # ----------------------------------------------------
        # Tela inicial
        # ----------------------------------------------------

        if sm.has_screen("tela_inicial"):

            sm.current = "tela_inicial"

        else:

            raise ValueError(
                "\nA tela 'tela_inicial' não foi encontrada!\n\n"
                "Verifique se existe:\n\n"
                "telas/tela_inicial.py\n"
            )


        return sm


# ============================================================
# INICIAR
# ============================================================

if __name__ == "__main__":

    ListaMercadoApp().run()
