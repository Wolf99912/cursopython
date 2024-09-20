# Definindo a classe Carro
class Carro:
    # Inicializando os atributos da classe
    def __init__(self, codigo, fabricante, modelo, cor, valor, ano):
        # Atributos do carro
        self.codigo = codigo  # Código identificador do carro
        self.fabricante = fabricante  # Nome do fabricante
        self.modelo = modelo  # Modelo do carro
        self.cor = cor  # Cor do carro
        self.valor = valor  # Valor do carro
        self.ano = ano  # Ano de fabricação do carro

    # Método para calcular o valor das parcelas
    def calcular_parcelas(self):
        # Solicita ao usuário a quantidade de parcelas
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        
        # Calcula o valor de cada parcela (sem juros, neste caso)
        valor_parcela = self.valor / quantidade_parcelas
        
        # Exibe o valor da parcela
        print(f"O valor de cada parcela é: R$ {valor_parcela:.2f}")

    # Método para exibir os dados do carro
    def exibir_dados(self):
        # Exibe os atributos do carro
        print(f"Código: {self.codigo}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Ano: {self.ano}")

# Criando o objeto carro com dados fornecidos pelo usuário
codigo = input("Digite o código do carro: ")
fabricante = input("Digite o fabricante do carro: ")
modelo = input("Digite o modelo do carro: ")
cor = input("Digite a cor do carro: ")
valor = float(input("Digite o valor do carro: "))  # Converte o valor para float
ano = int(input("Digite o ano do carro: "))  # Converte o ano para inteiro

# Criando um objeto da classe Carro
carro = Carro(codigo, fabricante, modelo, cor, valor, ano)

# Exibindo os dados do carro
carro.exibir_dados()

# Calculando as parcelas
carro.calcular_parcelas()
