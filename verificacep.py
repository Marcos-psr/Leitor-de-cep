import re
import requests


class BuscaEndereco:
    
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep Inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_valido(self, cep):
        buscador = re.search("[0-9]{5}-*[0-9]{3}", cep)
        if buscador:
            return True
        else:
            return False

    def format_cep(self):
        if len(self.cep) == 8:
            return "{}-{}".format(self.cep[:5], self.cep[5:])
        else:
            return self.cep

    def acesso_via_cep(self):
        cep_url = ""
        for caracter in self.cep:
            if caracter.isdigit():
                cep_url += caracter
        url = "https://viacep.com.br/ws/{}/json/".format(cep_url)
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )

BuscaEndereco("06660290")