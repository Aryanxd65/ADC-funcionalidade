def adicionar_usuario(usuarios):
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = peso / (altura ** 2)
    situacao = ("Abaixo do peso" if imc < 18.5 else
                "Peso normal" if imc < 25 else
                "Sobrepeso" if imc < 30 else
                "Obesidade grau I" if imc < 35 else
                "Obesidade grau II" if imc < 40 else
                "Obesidade grau III (mórbida)")

    usuarios.append({'nome_completo': f"{nome} {sobrenome}", 'imc': imc, 'situacao': situacao})

def exibir_resultados(usuarios):
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome_completo']}, IMC: {usuario['imc']:.2f}, Situação: {usuario['situacao']}")
    else:
        print("Nenhum usuário cadastrado.")

usuarios = []

while True:
    opcao = input("Escolha uma opção (1 - Adicionar usuário, 2 - Exibir resultados e sair): ")

    if opcao == '1':
        adicionar_usuario(usuarios)
    elif opcao == '2':
        exibir_resultados(usuarios)
        break
    else:
        print("Opção inválida. Tente novamente.")