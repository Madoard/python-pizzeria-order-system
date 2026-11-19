<div align="center">

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 🍕 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <h1>˚₊‧꒰ა 🍅 Sistema de Pedidos de Pizzaria em Python 🍅 ໒꒱‧₊˚</h1>

  <p>
    <i>✧･ﾟ: *✧･ﾟ:* Sistema de pedidos em Python via linha de comando permitindo que clientes combinem sabores e tamanhos de pizza com validação de entradas e cálculo automatizado da conta *:･ﾟ✧*:･ﾟ✧</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Controle%20de%20Fluxo-Loops%20%26%20Condicionais-E6E6FA?style=for-the-badge&logoColor=555555" alt="Controle de Fluxo" />
    <img src="https://img.shields.io/badge/Console-Sistema%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Sistema CLI" />
  </p>

</div>

<br/>

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🍽️ ꒱ Cardápio & Matriz de Preços

Os clientes podem combinar duas categorias de pizza (**Salgada** ou **Doce**) em três tamanhos (**Pequena**, **Média** ou **Grande**):

| 🍕 Tamanho | 🧀 Pizza Salgada (`PS`) | 🍫 Pizza Doce (`PD`) |
| :---: | :---: | :---: |
| **P** *(Pequena)* | `R$ 30,00` | `R$ 34,00` |
| **M** *(Média)* | `R$ 45,00` | `R$ 48,00` |
| **G** *(Grande)* | `R$ 60,00` | `R$ 66,00` |

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🧾 ꒱ Como Foi Construído

- **₊˚🌿 Loop Contínuo de Pedidos (`while`):** Estruturação de um laço interativo que permite adicionar múltiplos itens em uma única sessão enquanto valida as entradas de sabor e tamanho.
- **₊˚🍅 Matriz de Decisão (`if / elif / else`):** Implementação de ramificações condicionais aninhadas mapeando cada combinação de sabor (`PS` / `PD`) e tamanho (`P` / `M` / `G`) ao seu respectivo preço.
- **₊˚🌿 Acúmulo de Estado e Sanitização:** Uso de uma variável acumuladora `total` em conjunto com normalização de strings via `.strip().upper()` e `f-strings` formatadas para o recibo final.

<br/>

<div align="center">
  <p>°•. 🍅 .•° ────── ꒰ 💗 ꒱ ────── °•. 🍅 .•°</p>
  <p><i>feito com 💗 por <b>Maria Eduarda Gonçalves</b></i></p>
</div>
