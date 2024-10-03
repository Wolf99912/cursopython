
def capturar_nome():
    return input("Digite o nome do aluno: ")

def capturar_notas():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / 4  # Dividido por 4, pois são 4 notas

def programa_principal():
    nome = capturar_nome()  # Captura o nome
    notas = capturar_notas()  # Captura as 4 notas
    media = calcular_media(notas)  # Calcula a média das notas

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print(f"{nome} está APROVADO!")
    else:
        print(f"{nome} está REPROVADO.")

programa_principal()