PRECOS = {
    "PS": {"P": 30, "M": 45, "G": 60},
    "PD": {"P": 34, "M": 48, "G": 66},
}
NOMES = {"PS": "Pizza Salgada", "PD": "Pizza Doce"}


def mostrar_cardapio():
    #Exibe a mensagem de boas-vindas e o cardápio a partir do dicionário de preços.
    print("Bem-vindo à Pizzaria de Maria Eduarda Gonçalves!\nAqui está o nosso cardápio:")
    print("Tamanho     Pizza Salgada (PS)     Pizza Doce (PD)")
    for tamanho in ("P", "M", "G"):
        print(f" {tamanho}              R$ {PRECOS['PS'][tamanho]:.2f}              R$ {PRECOS['PD'][tamanho]:.2f}")


def pedir_opcao(mensagem, opcoes):
    #Pergunta até o usuário digitar uma das opções válidas e devolve a resposta.
    resposta = input(mensagem).strip().upper()
    while resposta not in opcoes:
        print("Opção inválida. Tente novamente.")
        resposta = input(mensagem).strip().upper()
    return resposta


def main():
    mostrar_cardapio()

    total = 0  # Variável acumuladora para o total do pedido
    resposta = "S"  # Variável de controle para múltiplos pedidos

    # Loop principal: roda enquanto o cliente quiser continuar pedindo
    while resposta == "S":
        print()
        sabor = pedir_opcao("Informe o sabor desejado (PS/PD): ", ("PS", "PD"))
        tamanho = pedir_opcao("Informe o tamanho desejado (P/M/G): ", ("P", "M", "G"))

        preco = PRECOS[sabor][tamanho]
        total += preco
        print(f"Você pediu uma {NOMES[sabor]} (Tamanho {tamanho}): R$ {preco:.2f}")

        print()
        resposta = pedir_opcao("Deseja pedir mais alguma coisa? (S/N): ", ("S", "N"))

    # Exibe o valor final do pedido
    print(f"\nObrigado pelo pedido! O total da sua conta é: R$ {total:.2f}")


if __name__ == "__main__":
    main()
