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
   git clone https://github.com/Madoard/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   ```
3. **Execute o script (`pizzaria.py`):**
   ```bash
   python pizzaria.py
   ```

### ✦ Exemplo de Uso

### ✦ Exemplo de Uso

```text
Bem-vindo à Pizzaria de Maria Eduarda Gonçalves!
Aqui está o nosso cardápio:
Tamanho     Pizza Salgada (PS)     Pizza Doce (PD)
 P              R$ 30.00              R$ 34.00
 M              R$ 45.00              R$ 48.00
 G              R$ 60.00              R$ 66.00

Informe o sabor desejado (PS/PD): ps
Informe o tamanho desejado (P/M/G): m
Você pediu uma Pizza Salgada (Tamanho M): R$ 45.00

Deseja pedir mais alguma coisa? (S/N): s

Informe o sabor desejado (PS/PD): pd
Informe o tamanho desejado (P/M/G): p
Você pediu uma Pizza Doce (Tamanho P): R$ 34.00

Deseja pedir mais alguma coisa? (S/N): n

Obrigado pelo pedido! O total da sua conta é: R$ 79.00
```

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

O código completo está em [`pizzaria.py`](./pizzaria.py). Abaixo está a estrutura principal e como cada parte funciona:

```python
PRECOS = {
    "PS": {"P": 30, "M": 45, "G": 60},
    "PD": {"P": 34, "M": 48, "G": 66},
}
NOMES = {"PS": "Pizza Salgada", "PD": "Pizza Doce"}


def mostrar_cardapio():
    """Exibe a mensagem de boas-vindas e o cardápio a partir do dicionário de preços."""
    print("Bem-vindo à Pizzaria de Maria Eduarda Gonçalves!\nAqui está o nosso cardápio:")
    print("Tamanho     Pizza Salgada (PS)     Pizza Doce (PD)")
    for tamanho in ("P", "M", "G"):
        print(f" {tamanho}              R$ {PRECOS['PS'][tamanho]:.2f}              R$ {PRECOS['PD'][tamanho]:.2f}")


def pedir_opcao(mensagem, opcoes):
    """Pergunta até o usuário digitar uma das opções válidas e devolve a resposta."""
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
```

- **Estrutura de dados e funções (`PRECOS`, `NOMES`, `mostrar_cardapio`, `pedir_opcao`):** Centraliza os preços e nomes em dicionários, gera o cardápio com um laço `for` e reaproveita a validação de entradas com `.strip().upper()` e `not in`.
- **Fluxo principal e loop (`main` / `while`):** Controla múltiplos pedidos em uma mesma sessão, consulta `PRECOS[sabor][tamanho]` diretamente sem `if/elif` aninhados e acumula o valor em `total`.
- **Formatação de saída:** Exibe cada item e o fechamento da conta com `f-strings` formatadas em duas casas decimais (`:.2f`).

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
</div>
