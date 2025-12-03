import random

# ==============================================================================
# SISTEMA DE CRIPTOGRAFIA RSA COM CRIVO DE ERATÓSTENES
# Disciplina: Segurança em Sistemas de Computação
# ==============================================================================

def crivo_de_eratostenes(limite):

    # 1. Cria uma lista de booleanos, inicialmente todos True
    # Índices representam os números. 0 e 1 não são primos.
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False

    p = 2
    # 2. O algoritmo termina quando o quadrado do número atual ultrapassa o limite
    while (p * p <= limite):
        # Se primos[p] não foi modificado, então é um primo
        if (primos[p] == True):
            # 3. Elimine (marque) todos os múltiplos de p
            for i in range(p * p, limite + 1, p):
                primos[i] = False
        p += 1

    # Retorna a lista de números que permaneceram como True (Primos)
    lista_primos = [p for p in range(limite + 1) if primos[p]]
    return lista_primos

def mdc(a, b):
    """Calcula o Máximo Divisor Comum entre a e b (Algoritmo de Euclides)."""
    while(b != 0):
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """
    Calcula o inverso multiplicativo modular de e módulo phi
    usando o Algoritmo de Euclides Estendido.

    """
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = extended_gcd(e, phi)
    if g != 1:
        # Não existe inverso modular se e e phi não forem coprimos
        return None
    else:
        return x % phi

def gerar_chaves():

   # Gera as chaves pública e privada do RSA.

    # Gera primos até 1000 para garantir que n seja maior que 255 (tabela ASCII)
    # e para fins didáticos de performance.
    lista_primos = crivo_de_eratostenes(1000)

    # Filtra primos muito pequenos para garantir segurança mínima na demonstração
    # n deve ser maior que o maior valor de caractere possível (255 para ASCII estendido)
    primos_uteis = [p for p in lista_primos if p > 50]

    if len(primos_uteis) < 2:
        raise Exception("Não há primos suficientes no intervalo definido.")

    # Escolhe dois primos distintos aleatoriamente
    p = random.choice(primos_uteis)
    q = random.choice(primos_uteis)
    while p == q:
        q = random.choice(primos_uteis)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Escolha de 'e' (Chave Pública)
    # e deve ser 1 < e < phi e coprimo de phi
    e = 3
    while e < phi:
        if mdc(e, phi) == 1:
            break
        e += 2

    # Cálculo de 'd' (Chave Privada)
    d = mod_inverse(e, phi)

    return ((e, n), (d, n), (p, q))

def texto_para_hex(texto):
    """Converte string para representação hexadecimal (para visualização)."""
    return " ".join("{:02x}".format(ord(c)) for c in texto)

def cifrar(mensagem, chave_publica):
    """
    Cifra a mensagem usando a chave pública (e, n).
    C = M^e mod n
    """
    e, n = chave_publica
    mensagem_cifrada = []

    for char in mensagem:
        k = ord(char) # Converte char para inteiro (ASCII/Unicode)
        c = pow(k, e, n) # Criptografia: (k ^ e) % n
        mensagem_cifrada.append(c)

    return mensagem_cifrada

def decifrar(mensagem_cifrada, chave_privada):
    """
    Decifra a mensagem usando a chave privada (d, n).
    M = C^d mod n
    """
    d, n = chave_privada
    mensagem_decifrada = []

    for char_code in mensagem_cifrada:
        m = pow(char_code, d, n) # Descriptografia: (c ^ d) % n
        mensagem_decifrada.append(chr(m)) # Converte inteiro de volta para char

    return "".join(mensagem_decifrada)

# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    print("--- GERADOR DE CHAVES RSA (com Crivo de Eratóstenes) ---")

    try:
        # 1. Geração de Chaves
        public_key, private_key, primos_escolhidos = gerar_chaves()
        p, q = primos_escolhidos

        print(f"\n[1] Primos gerados e selecionados:")
        print(f"    p = {p}")
        print(f"    q = {q}")
        print(f"\n[2] Cálculos Auxiliares:")
        print(f"    n (Módulo) = p * q = {public_key[1]}")
        print(f"    phi(n) = (p-1)*(q-1) = {(p-1)*(q-1)}")
        print(f"\n[3] Chaves Geradas:")
        print(f"    Chave Pública (e, n): {public_key}")
        print(f"    Chave Privada (d, n): {private_key}")

        # 2. Entrada de Dados
        print("\n" + "="*50)
        texto_original = input("Digite a mensagem para criptografar: ")
        # Exemplo padrão se o usuário der Enter vazio
        if not texto_original:
            texto_original = "InstitutoFederal"
            print(f"Nenhuma entrada detectada. Usando padrão: '{texto_original}'")

        # 3. Pré-codificação (Visualização Hexadecimal)
        hex_view = texto_para_hex(texto_original)
        print(f"\n[4] Representação Hexadecimal (Pré-codificação):")
        print(f"    {hex_view}")

        # 4. Criptografia
        texto_cifrado = cifrar(texto_original, public_key)
        print(f"\n[5] Mensagem Criptografada (Lista de Inteiros Cifrados):")
        print(f"    {texto_cifrado}")

        # Visualização Hexadecimal do Cifrado (opcional, mas interessante)
        hex_cifrado = " ".join("{:x}".format(c) for c in texto_cifrado)
        print(f"    (Hex do Cifrado: {hex_cifrado})")

        # 5. Descriptografia
        texto_recuperado = decifrar(texto_cifrado, private_key)
        print(f"\n[6] Mensagem Decifrada:")
        print(f"    {texto_recuperado}")

        print("\n" + "="*50)
        if texto_original == texto_recuperado:
            print("SUCESSO: A mensagem decifrada corresponde à original.")
        else:
            print("ERRO: A mensagem decifrada NÃO corresponde à original.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")