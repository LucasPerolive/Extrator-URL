import re

#######################################################
##### Mostra o valor do parametro da URL dasejado #####
#######################################################

# Cria o objeto URL
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    # Tira os espaçamentos da URL caso tenha
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    # Caso a URL estaja vazia retorna o erro para o usuário
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
    
        # Validando todas as opções posíveis
        padrao_url = re.compile('(http(s)?://)?(www.)?[].com(.br)?/[]')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é valida.")


    # Retorna o que há antes do "?"
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    # Retorna o que há depois do "?"
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    # Procura o parametro definido pelo usuário
    # Define qual o valor do parametro
    # E mostra até o que separa os parametros (&)
    # Confere se é o último da lista
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    

    def __len__ (self):
        return len(self.url)

    # Retorna algumas informações no lugar do valor que está na mémoria
    def __str__(self):
        return (f'URL: {self.url} \n'
                f'Parâmentros: {self.get_url_parametros()} \n'
                f'URL Base: {self.get_url_base()}\n')

    # Compara os objetos pela URL, no lugar de ser pelo o valor da mémoria
    def __eq__(self, other):
        return self.url == other.url

#######################################################################################

#Faz a conversão do real para o dolar vice-versa
def converter(origem, destino, quantidade):
    print('CONVERSÃO: ')

    if(origem == 'dolar' and destino == 'real'):
        total = ((quantidade) * valor_dolar)
        print(f"O valor de R${quantidade:,.2f} dólares é igual a ${total:,.2f} reais.")
    elif(origem == 'real' and destino == 'dolar'):
        total = ((quantidade) / valor_dolar)
        print(f"O valor de R${quantidade:,.2f} reais é igual a ${total:,.2f} dólares.")
    else:
        print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")        

#######################################################################################



# Faz a requisição do objeto
# Define a URL e o parametro
# Mostra o resultado
url = "https://bytebank.com/cambio?moedaDestino=real&quantidade=100&moedaOrigem=dolar"
extrator_url = ExtratorURL(url)
print(extrator_url)


# Desafio
valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
valor_quantidade = int(extrator_url.get_valor_parametro("quantidade"))
converter(moeda_origem, moeda_destino, valor_quantidade)