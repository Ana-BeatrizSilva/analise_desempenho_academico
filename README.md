# Análise de Desempenho Acadêmico

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## Sobre o Projeto

**Análise de Desempenho Acadêmico** é uma aplicação desenvolvida em Python para automatizar o cadastro de alunos, cálculo de médias, classificação de desempenho e geração de relatórios acadêmicos.

O sistema permite registrar múltiplos alunos, armazenar suas notas, calcular automaticamente as médias finais e classificar cada estudante de acordo com sua situação acadêmica.

Além do processamento dos dados, o projeto realiza a geração automática de relatórios em Excel utilizando **OpenPyXL** e cria visualizações gráficas utilizando **Matplotlib**, permitindo uma análise mais clara do desempenho individual dos alunos e dos resultados gerais da turma.

O projeto foi desenvolvido com finalidade educacional, visando praticar conceitos de programação, organização de projetos Python, manipulação de arquivos, análise de dados e visualização gráfica.

---

# Demonstração

## Relatório Excel Gerado

![Relatório Excel](imagens/relatorio_desempenho_academico.png)

*Planilha Excel gerada automaticamente contendo os dados dos alunos, notas, médias finais, situação acadêmica, estatísticas da turma e ranking de desempenho.*

---

## Gráfico de Médias dos Alunos

![Gráfico de Médias](imagens/grafico_medias_turma.png)

*Gráfico de barras apresentando a média individual dos alunos, permitindo comparar o desempenho acadêmico da turma.*

---

## Distribuição das Situações Acadêmicas

![Gráfico de Situações](imagens/grafico_situacoes_turma.png)

*Gráfico de pizza demonstrando a distribuição percentual entre alunos aprovados, em recuperação e reprovados.*

---

# Objetivos de Aprendizagem

Este projeto foi desenvolvido para praticar e consolidar conhecimentos relacionados a:

- Variáveis e tipos de dados;
- Operadores aritméticos;
- Estruturas condicionais;
- Estruturas de repetição;
- Manipulação de listas e dicionários;
- Funções em Python;
- Validação de dados;
- Organização de código;
- Estatística básica;
- Manipulação de arquivos Excel;
- Uso de bibliotecas externas;
- Automação de relatórios;
- Visualização de dados;
- Organização de projetos no GitHub.

---

# Funcionalidades

## Cadastro de Alunos

Permite cadastrar múltiplos alunos durante uma execução do programa.

## Registro de Notas

Cada aluno possui quatro notas cadastradas para cálculo da média final.

## Validação de Dados

O sistema valida as notas informadas, garantindo que os valores estejam dentro do intervalo permitido entre 0 e 10.

## Cálculo Automático de Médias

Realiza o cálculo da média final utilizando as notas cadastradas.

## Classificação Acadêmica

Define automaticamente a situação do aluno:

- **Aprovação:** média maior ou igual a 7;
- **Recuperação:** média maior ou igual a 5 e menor que 7;
- **Reprovação:** média inferior a 5.

## Estatísticas da Turma

O sistema gera indicadores gerais de desempenho:

- Quantidade total de alunos;
- Média geral da turma;
- Maior média registrada;
- Menor média registrada;
- Quantidade de alunos aprovados;
- Quantidade de alunos em recuperação;
- Quantidade de alunos reprovados;
- Percentual de cada situação acadêmica.

## Ranking de Desempenho

Cria automaticamente uma classificação dos alunos organizada da maior para a menor média.

O ranking apresenta:

- Posição;
- Nome do aluno;
- Média final;
- Situação acadêmica.

## Relatório Excel

Gera automaticamente um arquivo `.xlsx` contendo:

### Aba Alunos

- Nome dos alunos;
- Quatro notas cadastradas;
- Média final;
- Situação acadêmica.

### Aba Estatísticas

- Indicadores gerais da turma.

### Aba Ranking

- Classificação dos alunos por desempenho.

Recursos aplicados:

- Cabeçalhos formatados;
- Ajuste de largura das colunas;
- Filtro automático;
- Congelamento do cabeçalho.

## Visualização de Dados

O projeto gera gráficos para facilitar a interpretação dos resultados:

- Gráfico de barras com desempenho individual dos alunos;
- Linha indicando a média geral da turma;
- Valores das médias exibidos no gráfico;
- Gráfico de pizza com distribuição das situações acadêmicas.

---

# Estrutura do Projeto

```
analise_desempenho_academico/
│
├── README.md
├── main.py
├── requirements.txt
│
├── documentacao/
│   ├── descricao_projeto.md
│   ├── estrutura_projeto.md
│   └── funcionamento.md
│
├── graficos/
│   ├── grafico_medias_turma.png
│   └── grafico_situacoes_turma.png
│
├── imagens/
│   ├── grafico_medias_turma.png
│   ├── grafico_situacoes_turma.png
│   └── relatorio_desempenho_academico.png
│
└── relatorios/
    └── relatorio_desempenho_academico.xlsx
```

---

# Tecnologias Utilizadas

- Python
- OpenPyXL
- Matplotlib
- Visual Studio Code

---

# Bibliotecas Utilizadas

## OpenPyXL

Biblioteca utilizada para criação e manipulação de planilhas Excel.

Principais recursos utilizados:

- Criação de arquivos `.xlsx`;
- Criação de múltiplas abas;
- Inserção de dados;
- Formatação de células;
- Ajuste de largura das colunas;
- Organização dos relatórios.

---

## Matplotlib

Biblioteca utilizada para geração das visualizações gráficas.

Principais recursos utilizados:

- Gráfico de barras;
- Gráfico de pizza;
- Personalização de títulos;
- Configuração dos eixos;
- Exportação dos gráficos em formato PNG.

---

# Conceitos Aplicados

Durante o desenvolvimento do projeto foram utilizados conceitos como:

- Variáveis;
- Tipos de dados;
- Operadores matemáticos;
- Estruturas condicionais;
- Estruturas de repetição;
- Listas;
- Dicionários;
- Funções;
- Acumuladores e contadores;
- Ordenação de dados;
- Manipulação de arquivos;
- Bibliotecas externas;
- Estatística básica;
- Automação de relatórios;
- Visualização de dados.

---

# Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone https://github.com/Ana-BeatrizSilva/analise_desempenho_academico.git
```

---

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 3. Execute o programa

```bash
python main.py
```

---

# Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas:

- Exportação de dados para CSV;
- Geração de relatórios em PDF;
- Interface gráfica utilizando Tkinter;
- Integração com banco de dados;
- Dashboard interativo;
- Importação de dados externos;
- Implementação de testes automatizados.

---

Projeto desenvolvido para fins educacionais com o objetivo de praticar programação em Python, análise de dados, geração de relatórios e visualização gráfica.
