# Sistema de Boletim Escolar

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## Sobre o Projeto

**Sistema de Boletim Escolar** é uma aplicação desenvolvida em Python para automatizar o processo de registro, análise e visualização do desempenho acadêmico de alunos.

O sistema permite cadastrar múltiplos alunos, registrar notas, calcular médias automaticamente, classificar o desempenho acadêmico e gerar relatórios completos em formato Excel.

Além da geração de planilhas, a aplicação produz gráficos estatísticos que facilitam a análise dos resultados da turma, oferecendo uma visualização clara do desempenho individual dos alunos e da distribuição das situações acadêmicas.

O projeto foi desenvolvido com fins educacionais para praticar conceitos de programação em Python, manipulação de planilhas com OpenPyXL e visualização de dados utilizando Matplotlib.

---

## Demonstração

### Relatório de Alunos

![Relatório de Alunos](relatorios/relatorio_turma_image.png)

*Planilha gerada automaticamente contendo os dados dos alunos cadastrados, suas notas, médias finais e respectivas situações acadêmicas.*

---

### Gráfico de Médias

![Gráfico de Médias](relatorios/grafico_medias_turma.png)

*Gráfico de barras apresentando a média de cada aluno, permitindo uma comparação visual do desempenho da turma.*

---

### Gráfico de Situações

![Gráfico de Situações](relatorios/grafico_situacoes_turma.png)

*Gráfico de pizza demonstrando a distribuição percentual de alunos aprovados, em recuperação e reprovados.*

---

## Objetivos de Aprendizagem

Este projeto foi criado para praticar e consolidar conhecimentos relacionados a:

- Estruturas condicionais;
- Estruturas de repetição;
- Manipulação de listas;
- Validação de dados;
- Estatística básica;
- Organização de fluxo lógico;
- Manipulação de arquivos Excel;
- Utilização de bibliotecas externas;
- Geração de relatórios automatizados;
- Visualização de dados;
- Estruturação de projetos Python;
- Documentação de projetos no GitHub.

---

## Funcionalidades

### Cadastro de Alunos

Permite cadastrar múltiplos alunos durante uma única execução do programa.

### Registro de Notas

Coleta e armazena quatro notas para cada aluno cadastrado.

### Validação de Dados

Verifica se todas as notas informadas estão dentro do intervalo permitido entre 0 e 10.

### Cálculo Automático de Médias

Calcula automaticamente a média final de cada aluno.

### Classificação Acadêmica

Classifica os alunos de acordo com a média obtida:

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

### Geração de Relatórios

Cria automaticamente uma planilha Excel contendo:

- Aba de alunos;
- Aba de estatísticas;
- Dados organizados em formato tabular;
- Cabeçalhos formatados;
- Ajuste de largura das colunas.

### Visualização de Dados

Gera gráficos para facilitar a interpretação dos resultados:

- Gráfico de barras das médias dos alunos;
- Gráfico de pizza das situações acadêmicas.

---

## Estrutura do Projeto

```text
Sistema-Boletim-Escolar/
│
├── main.py
│
└── relatorios/
    ├── grafico_medias_turma.png
    ├── grafico_situacoes_turma.png
    ├── relatorio_turma_image.png
    └── relatorio_turma.xlsx
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
- Rotação de rótulos;
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
- Utilização de bibliotecas externas;
- Automação de tarefas;
- Estatística básica;
- Visualização de dados;
- Geração de relatórios.

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema-boletim-escolar.git
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
- Exportação para CSV;
- Geração de relatórios em PDF;
- Interface gráfica com Tkinter;
- Integração com banco de dados;
- Dashboard web utilizando Flask ou FastAPI;
- Importação de dados a partir de arquivos externos.

---

Projeto desenvolvido para fins educacionais com o objetivo de praticar programação em Python, automação de relatórios e visualização de dados.
