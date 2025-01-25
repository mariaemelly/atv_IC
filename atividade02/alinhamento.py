from Bio import SeqIO

def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("As sequências devem ter o mesmo comprimento para calcular a distância de Hamming")
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

with open('atividade02/alinhamento.fasta', 'r') as arquivo:
    sequencias = [record.seq for record in SeqIO.parse(arquivo, 'fasta')]

if len(sequencias) < 3:
    raise ValueError("O arquivo deve conter pelo menos três sequências para calcular as distâncias de Hamming")

# Calcular a distância de Hamming entre a linha 1 e a linha 2
distancia_B_A = hamming_distance(sequencias[1], sequencias[0])
print(f"Distância de Hamming da sequencia B em relacao a A: {distancia_B_A}")

# Calcular a distância de Hamming entre a linha 2 e a linha 3
distancia_C_A = hamming_distance(sequencias[2], sequencias[0])
print(f"Distância de Hamming da sequencia C em relacao a A: {distancia_C_A}")
distancia_C_B = hamming_distance(sequencias[2], sequencias[1])
print(f"Distância de Hamming da sequencia C em relacao a B: {distancia_C_B}")