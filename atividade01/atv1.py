#item a
with open ("/workspaces/atv_IC/atividade01/DNA.txt", 'r') as arquivo:
    texto = arquivo.read()

def contar_nucleotideo(texto):
    nucleotideos = {'A':0,'G':0,'C':0,'T':0}
    for nucleotideo in texto :
        if nucleotideo in nucleotideos:
            nucleotideos[nucleotideo]+=1

    return nucleotideos

resultado = contar_nucleotideo(texto)
print ("Contagem de Nucleotideos\n")
print("A:",resultado ['A'])
print("G:",resultado ['G'])
print("C:",resultado ['C'])
print("T:",resultado ['T'])
#item b
print("\nRNA\n") 
novo_texto = open('RNA.txt','w', encoding='UTF-8')
novo_texto.write(texto.replace('T','U'))
novo_texto.close()

with open ("RNA.txt", 'r') as arquivo2:
    texto2 = arquivo2.read()
print (texto2)
#item c

AMINO = {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu', 'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu','AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile', 'AUG':'Met', 'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val','UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro','ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr', 'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala','UAU':'Tyr', 'UAC':'Tyr', 'UAA':'Stop', 'UAG':'Stop', 'CAU':'His', 'CAC':'His', 'CAA':'Gln', 'CAG':'Gln','AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys', 'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu','UGU':'Cys', 'UGC':'Cys', 'UGA':'Stop', 'UGG':'Trp', 'CGU':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg','AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly'}         

# Função para converter RNA em aminoácidos
def rna_to_aminoacids(rna_sequence):
    amino_acids = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acids.append(AMINO.get(codon, ''))
    return ' '.join(amino_acids)





