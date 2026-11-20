<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>˚₊‧꒰ა Sistema de Pedidos de Pizzaria em Python ໒꒱‧₊˚</h1>

  <p>
    <i>Sistema de pedidos em Python via linha de comando para combinar sabores e tamanhos de pizza com cálculo automático do total.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Controle%20de%20Fluxo-Loops%20%26%20Condicionais-E6E6FA?style=for-the-badge&logoColor=555555" alt="Controle de Fluxo" />
    <img src="https://img.shields.io/badge/Console-Sistema%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Sistema CLI" />
  </p>

</div>

<br/>

### ✦ Resumo

Permite registrar pedidos de pizza diretamente no terminal escolhendo entre opções salgadas (`PS`) ou doces (`PD`) e tamanhos (`P`, `M` ou `G`), validando entradas, acumulando vários itens na mesma sessão e exibindo o valor final da conta.

### ✦ Tecnologias

- **Python 3.x:** Linguagem principal para laços de repetição, estruturas condicionais, tratamento de strings e interação via console (sem bibliotecas externas).

### ✦ Regras

Os preços variam conforme a categoria (**Salgada `PS`** ou **Doce `PD`**) e o tamanho (**`P`**, **`M`** ou **`G`**):

| Tamanho | Pizza Salgada (`PS`) | Pizza Doce (`PD`) |
| :---: | :---: | :---: |
| **P** *(Pequena)* | `R$ 30,00` | `R$ 34,00` |
| **M** *(Média)* | `R$ 45,00` | `R$ 48,00` |
| **G** *(Grande)* | `R$ 60,00` | `R$ 66,00` |

- Entradas são normalizadas com `.strip().upper()` para aceitar letras minúsculas ou espaços extras.
- O cliente pode adicionar quantos itens quiser no loop até encerrar o pedido, somando tudo no total.
<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Executar

1. **Pré-requisitos:** Tenha o **Python 3.x** instalado na máquina.
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Madoard/NOME-DO-REPOSITORIO.git](https://github.com/Madoard/NOME-DO-REPOSITORIO.git)
   cd NOME-DO-REPOSITORIO
   ```
3. **Execute o script (`pizzaria.py`):**
   ```bash
   python pizzaria.py
   ```

### ✦ Exemplo de Uso

```text
Welcome to Maria Eduarda Gonçalves's Pizzeria!
Here is our menu:
Size     Savory Pizza (SP)     Sweet Pizza (SW)
 S            $ 30.00              $ 34.00
 M            $ 45.00              $ 48.00
 L            $ 60.00              $ 66.00

Enter the desired flavor (SP/SW): sp
Enter the desired size (S/M/L): m
You ordered a Savory Pizza (Size M): $ 45.00

Would you like to order anything else? (Y/N): y

Enter the desired flavor (SP/SW): sw
Enter the desired size (S/M/L): s
You ordered a Sweet Pizza (Size S): $ 34.00

Would you like to order anything else? (Y/N): n

Thank you for your order! Your total is: $ 79.00
```

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

O código completo está em [`pizzaria.py`](./pizzaria.py). Abaixo está a estrutura principal e como cada parte funciona:

```python
total = 0
answer = "Y"

while answer == "Y":
    flavor = input("\nEnter the desired flavor (SP/SW): ").strip().upper()
    while flavor != "SP" and flavor != "SW":
        print("Invalid flavor. Please try again.")
        flavor = input("Enter the desired flavor (SP/SW): ").strip().upper()

    size = input("Enter the desired size (S/M/L): ").strip().upper()
    while size != "S" and size != "M" and size != "L":
        print("Invalid size. Please try again.")
        size = input("Enter the desired size (S/M/L): ").strip().upper()

    if flavor == "SP":
        if size == "S":
            print("You ordered a Savory Pizza (Size S): $ 30.00")
            total += 30
        elif size == "M":
            print("You ordered a Savory Pizza (Size M): $ 45.00")
            total += 45
        else:
            print("You ordered a Savory Pizza (Size L): $ 60.00")
            total += 60
    else:
        if size == "S":
            print("You ordered a Sweet Pizza (Size S): $ 34.00")
            total += 34
        elif size == "M":
            print("You ordered a Sweet Pizza (Size M): $ 48.00")
            total += 48
        else:
            print("You ordered a Sweet Pizza (Size L): $ 66.00")
            total += 66

    answer = input("\nWould you like to order anything else? (Y/N): ").strip().upper()
    while answer != "Y" and answer != "N":
        print("Invalid option. Please enter Y or N.")
        answer = input("Would you like to order anything else? (Y/N): ").strip().upper()

print(f"\nThank you for your order! Your total is: $ {total:.2f}")
```

- **Loop contínuo de pedidos (`while`):** Mantém o fluxo ativo enquanto o cliente desejar adicionar itens (`Y`) e valida as respostas de sabor (`SP`/`SW`), tamanho (`S`/`M`/`L`) e continuidade (`Y`/`N`).
- **Condicionais aninhadas (`if / elif / else`):** Mapeia cada combinação de sabor e tamanho ao valor correspondente do cardápio.
- **Acúmulo e formatação:** Soma os valores na variável `total`, sanitiza entradas com `.strip().upper()` e exibe o valor final formatado com `f-strings` (`:.2f`).

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
