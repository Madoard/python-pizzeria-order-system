# Exibe mensagem de boas-vindas e o cardápio
print("Bem-vindo à Pizzaria de Maria Eduarda Gonçalves!\nAqui está o nosso cardápio:")
print("Tamanho     Pizza Salgada (PS)     Pizza Doce (PD)")
print(" P              R$ 30.00              R$ 34.00")
print(" M              R$ 45.00              R$ 48.00")
print(" G              R$ 60.00              R$ 66.00")

total = 0  # Variável acumuladora para o total do pedido
resposta = "S"  # Variável de controle para múltiplos pedidos

# Loop principal: roda enquanto o cliente quiser continuar pedindo
while resposta == "S":
    # Solicita o sabor da pizza e valida a entrada
    sabor = input("\nInforme o sabor desejado (PS/PD): ").strip().upper()
    while sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente.")
        sabor = input("Informe o sabor desejado (PS/PD): ").strip().upper()

    # Solicita o tamanho da pizza e valida a entrada
    tamanho = input("Informe o tamanho desejado (P/M/G): ").strip().upper()
    while tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")
        tamanho = input("Informe o tamanho desejado (P/M/G): ").strip().upper()

    # Condicionais aninhadas para definir o preço e somar ao total
    if sabor == "PS":
        if tamanho == "P":
            print("Você pediu uma Pizza Salgada (Tamanho P): R$ 30.00")
            total += 30
        elif tamanho == "M":
            print("Você pediu uma Pizza Salgada (Tamanho M): R$ 45.00")
            total += 45
        else:
            print("Você pediu uma Pizza Salgada (Tamanho G): R$ 60.00")
            total += 60
    else:
        if tamanho == "P":
            print("Você pediu uma Pizza Doce (Tamanho P): R$ 34.00")
            total += 34
        elif tamanho == "M":
            print("Você pediu uma Pizza Doce (Tamanho M): R$ 48.00")
            total += 48
        else:
            print("Você pediu uma Pizza Doce (Tamanho G): R$ 66.00")
            total += 66

    # Pergunta se o cliente deseja adicionar mais itens
    resposta = input("\nDeseja pedir mais alguma coisa? (S/N): ").strip().upper()
    while resposta != "S" and resposta != "N":
        print("Opção inválida. Digite S ou N.")
        resposta = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()

# Exibe o valor final do pedido
print(f"\nObrigado pelo pedido! O total da sua conta é: R$ {total:.2f}")
