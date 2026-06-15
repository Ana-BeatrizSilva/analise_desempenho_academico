# Sistema de Avaliação Acadêmica 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---
## Sobre o Projeto

**Sistema de Avaliação Acadêmica** é uma aplicação desenvolvida em Python para automatizar o cadastro de alunos, o cálculo de médias e a geração de relatórios acadêmicos.

O sistema permite registrar múltiplos alunos, armazenar suas notas, calcular automaticamente as médias finais e classificar cada estudante de acordo com seu desempenho acadêmico.

Além da geração de planilhas Excel utilizando OpenPyXL, o projeto também produz gráficos estatísticos com Matplotlib, permitindo uma análise visual clara do desempenho individual dos alunos e dos resultados gerais da turma.

O projeto foi desenvolvido com fins educacionais para praticar conceitos fundamentais e intermediários de programação, manipulação de planilhas Excel, análise de dados e visualização gráfica.

---

## Demonstração

### Relatório Gerado

![Relatório](relatorios/relatorio_turma_image.png)

*Planilha Excel gerada automaticamente contendo os alunos cadastrados, suas notas, médias finais e respectivas situações acadêmicas.*

---

### Gráfico de Médias dos Alunos

![Gráfico de Médias](relatorios/grafico_medias_turma.png)

*Gráfico de barras que apresenta a média individual de cada aluno, permitindo comparar facilmente o desempenho da turma.*

---

### Distribuição das Situações Acadêmicas

![Gráfico de Situações](relatorios/grafico_situacoes_turma.png)

*Gráfico de pizza que exibe a distribuição percentual de alunos aprovados, em recuperação e reprovados.*

---

## Objetivos de Aprendizagem

Este projeto foi criado para praticar e consolidar conhecimentos relacionados a:

- Variáveis e tipos de dados;
- Estruturas condicionais;
- Estruturas de repetição;
- Manipulação de listas;
- Validação de dados;
- Estatística básica;
- Organização de fluxo lógico;
- Manipulação de arquivos Excel;
- Utilização de bibliotecas externas;
- Geração automatizada de relatórios;
- Visualização de dados;
- Estruturação de projetos Python;
- Documentação de projetos no GitHub.

---

## Funcionalidades

### Cadastro de Alunos

Permite cadastrar múltiplos alunos durante uma única execução do programa.

### Registro de Notas

Coleta e armazena quatro notas para cada aluno.

### Validação de Dados

Garante que todas as notas informadas estejam dentro do intervalo permitido entre 0 e 10.

### Cálculo Automático de Médias

Calcula automaticamente a média final de cada aluno.

### Classificação Acadêmica

Determina a situação de cada estudante com base em sua média final:

- Aprovação (média maior ou igual a 7);
- Recuperação (média maior ou igual a 5 e menor que 7);
- Reprovação (média inferior a 5).

### Estatísticas da Turma

Gera indicadores gerais de desempenho:

- Média da turma;
- Maior média registrada;
- Menor média registrada;
- Quantidade de aprovados;
- Quantidade de alunos em recuperação;
- Quantidade de reprovados.

### Relatório Excel

Cria automaticamente uma planilha contendo:

- Aba de alunos;
- Aba de estatísticas;
- Dados organizados em formato tabular;
- Cabeçalhos formatados em negrito;
- Ajuste de largura das colunas.

### Visualização de Dados

Gera gráficos para facilitar a interpretação dos resultados:

- Gráfico de barras com as médias dos alunos;
- Gráfico de pizza com a distribuição das situações acadêmicas.

---

## Estrutura do Projeto

```text
Sistema_Boletim_Escolar/
│
├── README.md
├── main.py
│
└── relatorios/
    ├── grafico_medias_turma.png
    ├── grafico_situacoes_turma.png
    ├── relatorio_turma.xlsx
    └── relatorio_turma_image.png
```

---

## Tecnologias Utilizadas

- Python
- OpenPyXL
- Matplotlib
- Visual Studio Code

---

## Bibliotecas Utilizadas

### OpenPyXL

Biblioteca utilizada para criação e manipulação de planilhas Excel.

Principais recursos utilizados:

- Criação de arquivos `.xlsx`;
- Criação de múltiplas abas;
- Inserção de dados;
- Formatação de células;
- Ajuste de largura de colunas.

### Matplotlib

Biblioteca utilizada para visualização gráfica dos dados.

Principais recursos utilizados:

- Gráficos de barras;
- Gráficos de pizza;
- Personalização de títulos;
- Configuração dos eixos;
- Exportação de gráficos como imagens.

---

## Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- Variáveis;
- Tipos de dados;
- Operadores aritméticos;
- Estruturas condicionais;
- Estruturas de repetição;
- Listas;
- Acumuladores e contadores;
- Validação de entrada de dados;
- Manipulação de arquivos;
- Importação de módulos;
- Bibliotecas externas;
- Estatística básica;
- Automação de tarefas;
- Visualização de dados;
- Geração de relatórios.

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Ana-BeatrizSilva/Sistema_Boletim_Escolar.git
```

### 2. Instale as dependências

```bash
pip install openpyxl matplotlib
```

### 3. Execute o programa

```bash
python main.py
```

---

## Possíveis Melhorias Futuras

- Tratamento de exceções com `try/except`;
- Exportação de dados para CSV;
- Geração de relatórios em PDF;
- Interface gráfica com Tkinter;
- Integração com banco de dados;
- Dashboard web com Flask;
- Importação de dados externos.

---

Projeto desenvolvido para fins educacionais com o objetivo de praticar programação em Python, geração de relatórios e visualização de dados.
