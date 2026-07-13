#Importações
from openpyxl import Workbook
from openpyxl.styles import Font
import matplotlib.pyplot as plt

medias = []
nomes = []
aprovacao = 0
reprovacao = 0
recuperacao = 0

planilha = Workbook()
aba = planilha.active

aba.append([
    "Nome",
    "Nota 1",
    "Nota 2",
    "Nota 3",
    "Nota 4",
    "Média",
    "Situação"
])

for celula in aba[1]:
    celula.font = Font(bold=True) #definir fonte em negrito

#Fluxo de entrada de dados dos alunos
qtd_alunos = int(input("Quantidade de alunos que deseja cadastrar: "))

for i in range(qtd_alunos):
    nome = input(f"Informe o nome do {i+1}° aluno: ")
    
    notas = []
    for j in range(4):
        while True:
            nota = float(input(f"Informe a nota {j+1}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break

            print("A nota deve estar entre 0 e 10.")
    #Calcular média
    media = sum(notas)/len(notas)

    #Situações
    if media >= 7:
        situacao = "Aprovação"
        aprovacao += 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovação"
        reprovacao += 1

    nomes.append(nome)
    medias.append(media)

    #Salvar na planilha
    aba.append([
    nome,
    notas[0],
    notas[1],
    notas[2],
    notas[3],
    round(media, 2),
    situacao
])
    
#Estatísticas da turma
media_turma = sum(medias)/len(medias)
maior_media = max(medias)
menor_media = min(medias)

#Criação de aba de estatísticas
aba_estatisticas = planilha.create_sheet("Estatísticas")

aba_estatisticas.append([
    "Indicador",
    "Valor"
])
aba_estatisticas.append([
    "Média da turma",
    round(media_turma, 2)
])
aba_estatisticas.append([
    "Maior média",
    round(maior_media, 2)
])
aba_estatisticas.append([
    "Menor média",
    round(menor_media, 2)
])
aba_estatisticas.append([
    "Aprovados",
    aprovacao
])
aba_estatisticas.append([
    "Recuperação",
    recuperacao
])
aba_estatisticas.append([
    "Reprovados",
    reprovacao
])

for celula in aba_estatisticas[1]:
    celula.font = Font(bold=True)

#Ajuste na dimensão de colunas
aba.column_dimensions["A"].width = 25
aba.column_dimensions["B"].width = 10
aba.column_dimensions["C"].width = 10
aba.column_dimensions["D"].width = 10
aba.column_dimensions["E"].width = 10
aba.column_dimensions["F"].width = 12
aba.column_dimensions["G"].width = 15

print("\n=== ESTATÍSTICAS DA TURMA ===")

print(f"Média da turma: {media_turma:.2f}")
print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")

print(f"Aprovados: {aprovacao}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovacao}")

#Salvar
planilha.save("relatorios/relatorio_turma.xlsx")
print("\nPLANILHA GERADA COM SUCESSO!")

#Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(nomes, medias)
plt.title("Média dos alunos")
plt.xlabel("Aluno")
plt.ylabel("Média")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("relatorios/grafico_medias_turma.png")
plt.savefig("relatorios/grafico_medias_turma.png")
plt.show()

#Gráfico de pizza
situacoes = [aprovacao, recuperacao, reprovacao]
labels = ["Aprovaçaõ", "Recuperação", "Reprovação"]
plt.figure()
plt.pie(situacoes, labels=labels,autopct="%1.1f%%")
plt.title("Situaçaõ da Turma")
plt.savefig("relatorios/grafico_situacoes_turma.png")
plt.show()