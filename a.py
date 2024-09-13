#Esse aqui é um exemplo de criação de classe e modelo
class Carro:
    def __init__(self, modelo, cor, valor, ano):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.ano = ano
#Aqui abaixo estão suas definições e atributos colocados a classe
    def calcular_valor_com_desconto(self, desconto):
        """
        Calcula o valor do carro aplicando um desconto fixo.

        :param desconto: Valor do desconto a ser aplicado.
        :return: Valor do carro após aplicar o desconto.
        """
        return self.valor - desconto

    def calcular_valor(self):
        """
        Retorna o valor atual do carro.

        :return: Valor do carro.
        """
        return self.valor

# Exemplo de uso com input do usuário
if __name__ == "__main__":
    modelo = input("Digite o modelo do carro: ")
    cor = input("Digite a cor do carro: ")
    valor = float(input("Digite o valor do carro: R$"))
    ano = int(input("Digite o ano do carro: "))
    
    carro = Carro(modelo=modelo, cor=cor, valor=valor, ano=ano)
    
    print(f"\nModelo: {carro.modelo}")
    print(f"Cor: {carro.cor}")
    print(f"Ano: {carro.ano}")
    print(f"Valor original: R${carro.calcular_valor():.2f}")
    
    desconto = float(input("\nDigite o valor do desconto fixo: R$"))
    valor_com_desconto = carro.calcular_valor_com_desconto(desconto)
    print(f"Valor com desconto de R${desconto:.2f}: R${valor_com_desconto:.2f}")
#Demonstro uma função aqui