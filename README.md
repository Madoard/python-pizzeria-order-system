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
total = 0
resposta = "S"

while resposta == "S":
    sabor = input("\nInforme o sabor desejado (PS/PD): ").strip().upper()
    while sabor != "PS" and sabor != "PD":
        print("Sabor inválido. Tente novamente.")
        sabor = input("Informe o sabor desejado (PS/PD): ").strip().upper()

    tamanho = input("Informe o tamanho desejado (P/M/G): ").strip().upper()
    while tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")
        tamanho = input("Informe o tamanho desejado (P/M/G): ").strip().upper()

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

    resposta = input("\nDeseja pedir mais alguma coisa? (S/N): ").strip().upper()
    while resposta != "S" and resposta != "N":
        print("Opção inválida. Digite S ou N.")
        resposta = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()

print(f"\nObrigado pelo pedido! O total da sua conta é: R$ {total:.2f}")
```

- **Loop contínuo de pedidos (`while`):** Mantém o fluxo ativo enquanto o cliente desejar adicionar itens (`S`) e valida as respostas de sabor (`PS`/`PD`), tamanho (`P`/`M`/`G`) e continuidade (`S`/`N`).
- **Condicionais aninhadas (`if / elif / else`):** Mapeia cada combinação de sabor e tamanho ao valor correspondente do cardápio.
- **Acúmulo e formatação:** Soma os valores na variável `total`, sanitiza entradas com `.strip().upper()` e exibe o valor final formatado com `f-strings` (`:.2f`).

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
