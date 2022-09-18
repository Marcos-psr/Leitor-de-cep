from tkinter import *
from verificacep import BuscaEndereco

DARK_KHAKI = "#BDB76B"
GRAY = "#D3D3D3"
TEAL = "#008080"
WHEAT = "#F5DEB3"
WHITE = "#FFFFFF"
YELLOW_GREEN = "#ADFF2F"

cep_classe = BuscaEndereco("11111111")


class InterfaceCEP:
    def __init__(self):
        self.root = root = Tk()
        self.screen()
        self.cria_frame()
        self.cria_botao()
        self.cria_labels_entry()
        root.mainloop()

    def screen(self):
        self.root.configure(background=YELLOW_GREEN)
        self.root.geometry("800x400")
        self.root.resizable(False, False)
        self.root.title("Localizar endereços")

    def cria_frame(self):
        self.frame = Frame(self.root, background=WHEAT, highlightthickness=4, highlightbackground=DARK_KHAKI)
        self.frame.place(relx=0.04, rely=0.05, relwidth=0.92, relheight=0.9)

        self.label_titulo = Label(self.frame, text="BUSCADOR DE ENDEREÇOS", background=WHEAT,
                                  font=("courier", 18, "bold"))
        self.label_titulo.place(relwidth=0.4, relx=0.3, rely=0.1)

        self.formato = Label(self.frame, text="Formato: 00000000", background=WHEAT,
                             font=("courier", 14, "bold"))
        self.formato.place(relwidth=0.3, relx=0.35, rely=0.2)

    def cria_botao(self):
        self.button = Button(self.frame, text="Busca CEP", bd=3, bg=TEAL, fg=WHITE, font=("verdana", 10, "bold"),
                             command=self.locais)
        self.button.place(relx=0.65, rely=0.4, relwidth=0.25, relheight=0.07)

    def cria_labels_entry(self):
        self.label_cep = Label(self.frame, text="Insira o CEP:", bg=WHEAT, font=("verdana", 10, "bold"))
        self.label_cep.place(relx=0.1, rely=0.4, relwidth=0.15, relheight=0.07)
        self.entry_cep = Entry(self.frame, font=("arial", 10))
        self.entry_cep.place(relx=0.25, rely=0.4, relwidth=0.4, relheight=0.07)

        self.label_cidade = Label(self.frame, text="Cidade:", bg=WHEAT, font=("verdana", 10, "bold"))
        self.label_cidade.place(relx=0.15, rely=0.6, relheight=0.07)
        self.entry_cidade = Entry(self.frame, font=("arial", 10))
        self.entry_cidade.place(relx=0.25, rely=0.6, relwidth=0.4, relheight=0.07)

        self.label_bairro = Label(self.frame, text="Bairro:", bg=WHEAT, font=("verdana", 10, "bold"))
        self.label_bairro.place(relx=0.15, rely=0.7, relheight=0.07)
        self.entry_bairro = Entry(self.frame, font=("arial", 10))
        self.entry_bairro.place(relx=0.25, rely=0.7, relwidth=0.55, relheight=0.07)

        self.label_uf = Label(self.frame, text="UF:", bg=WHEAT, font=("verdana", 10, "bold"))
        self.label_uf.place(relx=0.67, rely=0.6, relheight=0.07)
        self.entry_uf = Entry(self.frame, font=("arial", 10, "bold"))
        self.entry_uf.place(relx=0.73, rely=0.6, relwidth=0.07, relheight=0.07)

    def locais(self):
        self.entry_cidade.delete(0, END)
        self.entry_bairro.delete(0, END)
        self.entry_uf.delete(0, END)

        try:
            entrada_cep = self.entry_cep.get()
            cep_classe.cep = entrada_cep
            endereco = cep_classe.acesso_via_cep()
            bairro = endereco[0]
            cidade = endereco[1]
            uf = endereco[2]

            self.entry_cidade.insert(0, cidade)
            self.entry_bairro.insert(0, bairro)
            self.entry_uf.insert(0, uf)

        except:
            self.entry_cep.delete(0, END)
            self.entry_cep.insert(0, "VERIFIQUE O CEP E TENTE NOVAMENTE!")


if __name__ == "__main__":
    InterfaceCEP()
