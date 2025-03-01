import time
import bisect

# Carregar a lista de palavras do arquivo
def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo]
    return palavras

# Busca Linear
def busca_linear(lista, palavra):
    for item in lista:
        if item == palavra:
            return True
    return False

# Busca Binária
def busca_binaria(lista, palavra):
    index = bisect.bisect_left(lista, palavra)
    return index < len(lista) and lista[index] == palavra

# Medir tempo de execução
def medir_tempo(busca_func, lista, palavra):
    inicio = time.perf_counter()  # Marca o tempo inicial
    resultado = busca_func(lista, palavra)
    fim = time.perf_counter()  # Marca o tempo final
    tempo_gasto = (fim - inicio) * 1e6  # Convertendo para microssegundos (µs)
    return resultado, tempo_gasto

# Frase a ser buscada
frase = """Não atire o pau no gato
Porque isso
Não se faz
O gatinho
É nosso amigo
Não devemos maltratar os animais
Jamais"""

# Processamento
palavras_lista = carregar_palavras("br-utf8.txt")  # Carregar lista
palavras_lista.sort()  # Ordenar para busca binária

# Converter frase em palavras tratadas
palavras_frase = [palavra.lower() for palavra in frase.split()]

# Resultados
print("| Palavra       | Linear (µs) | Binária (µs) |")
print("|--------------|------------|-------------|")

for palavra in palavras_frase:
    _, tempo_linear = medir_tempo(busca_linear, palavras_lista, palavra)
    _, tempo_binaria = medir_tempo(busca_binaria, palavras_lista, palavra)
    print(f"| {palavra:<12} | {tempo_linear:10.2f} | {tempo_binaria:10.2f} |")
