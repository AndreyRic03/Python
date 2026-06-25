# senhas
usuarios = {
    "Rosilene": "19780906",
    "Leandro": "19782111",
    "Willamy": "20070408",
    "Andrey": "20160703"
}

nome = input("Digite o nome: ")

def pedirsenha(senha_correta):
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso Liberado! Autorizado.")
    else:
        print("Senha incorreta! Não autorizado.")

def semlicenca():
    print("Não autorizado, você está sem licença.")


if nome in usuarios:

    senha_cadastrada = usuarios[nome]
    pedirsenha(senha_cadastrada)
else:
    semlicenca()
