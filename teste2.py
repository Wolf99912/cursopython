funcionarios = [
    {"nome": "João Silva"},
    {"nome": "Maria Oliveira"},
    {"nome": "Pedro Almeida"},
    {"nome": "Ana Souza"},
    {"nome": "Lucas Fernandes"}
]

while True:
    print("=== Menu ===")
    print("1. Pesquisar por nome")
    print("2. Cadastrar um funcionário")
    print("3. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do funcionário: ")
        encontrado = False
        for funcionario in funcionarios:
            if funcionario["nome"].lower() == nome.lower():
                print(f"Nome: {funcionario['nome']}")
                encontrado = True
                break
        if not encontrado:
            print("Funcionário não encontrado.")

    elif opcao == "2":
        novo_nome = input("Digite o nome do novo funcionário: ")
        if any(funcionario["nome"].lower() == novo_nome.lower() for funcionario in funcionarios):
            print("Funcionário já cadastrado.")
        else:
            funcionarios.append({"nome": novo_nome})
            print(f"Funcionário '{novo_nome}' cadastrado com sucesso!")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

