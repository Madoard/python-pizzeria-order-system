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
