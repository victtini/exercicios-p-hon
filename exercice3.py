import csv 
dados =[
    ['nome','idade','nota'],
    ['ana',16,5],
    ['carlos',14,15]
]
with open('aluno.txt', 'a') as escrever:
    professor =csv.writer(escrever)
    professor.writerows (dados)
    with open('aluno.txt', 'r') as arquivo:
            conteudo =csv.reader(arquivo)
            print(conteudo)
