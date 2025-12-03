Implementação do Algoritmo RSA com Crivo de Eratóstenes

Este repositório contém a implementação prática do algoritmo de criptografia assimétrica RSA, desenvolvida como requisito avaliativo para a disciplina de Segurança em Sistemas de Computação. O projeto inclui a geração automática de números primos utilizando o método clássico do Crivo de Eratóstenes, além das rotinas de cifragem e decifragem de mensagens textuais.
---------------
📋 Funcionalidades

O sistema realiza as seguintes operações:

Geração de Primos: Utiliza o algoritmo do Crivo de Eratóstenes para listar primos até um limite definido e seleciona aleatoriamente dois primos distintos ($p$ e $q$).

Cálculo de Chaves:

Calcula o módulo $n = p \times q$.

Calcula o tociente $\phi(n) = (p-1)(q-1)$.

Determina a chave pública ($e$) coprima de $\phi(n)$.

Calcula a chave privada ($d$) através do inverso modular.

Conversão Hexadecimal: Exibe a representação hexadecimal da mensagem original antes da cifragem.

Criptografia: Aplica a função $C = M^e \pmod n$.

Descriptografia: Restaura a mensagem original via $M = C^d \pmod n$.
---------------
🚀 Como Executar

Pré-requisitos

Python 3.x instalado.
---------------
Passos

Clone este repositório:

git clone [https://github.com/MateusRondon/CRIPTOGRAFIA_ERATOSTENES.git](https://github.com/MateusRondon/CRIPTOGRAFIA_ERATOSTENES.git)


Navegue até a pasta do projeto e execute o arquivo principal:

python rsa_main.py


Siga as instruções no terminal: digite a mensagem que deseja criptografar e observe o processo passo a passo.
---------------
🧪 Exemplo de Uso

--- GERADOR DE CHAVES RSA (com Crivo de Eratóstenes) ---

[1] Primos gerados e selecionados:
    p = 61
    q = 53

[3] Chaves Geradas:
    Chave Pública (e, n): (3, 3233)
    Chave Privada (d, n): (2011, 3233)

Digite a mensagem para criptografar: IFMT

[4] Representação Hexadecimal (Pré-codificação):
    49 46 4d 54

[5] Mensagem Criptografada:
    [2304, 1234, 432, 11]

[6] Mensagem Decifrada:
    IFMT

---------------
🛠 Tecnologias

Linguagem: Python 3
---------------
Bibliotecas: Apenas bibliotecas padrão (random).

📚 Referências Teóricas

Rivest, R. L., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems.

Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography.

👨‍💻 Autores

[@MateusRondon]
