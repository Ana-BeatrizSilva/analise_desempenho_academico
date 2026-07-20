# Estrutura do Projeto

A organização do projeto segue a seguinte estrutura:

```text
analise_desempenho_academico/

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

## Descrição dos arquivos

### `main.py`

Arquivo principal da aplicação responsável por:

- Cadastro dos alunos;
- Registro das notas;
- Cálculo das médias;
- Classificação da situação acadêmica;
- Geração das estatísticas da turma;
- Criação do ranking dos alunos;
- Exportação dos relatórios;
- Geração dos gráficos.

### `requirements.txt`

Arquivo contendo as bibliotecas externas necessárias para execução do projeto.

### `documentacao/`

Pasta contendo os documentos técnicos:

- `descricao_projeto.md` → apresenta o objetivo, contexto e tecnologias utilizadas;
- `estrutura_projeto.md` → descreve a organização dos arquivos;
- `funcionamento.md` → explica o fluxo de execução da aplicação.

### `graficos/`

Pasta contendo os gráficos gerados automaticamente pelo programa:

- `grafico_medias_turma.png`;
- `grafico_situacoes_turma.png`.

### `imagens/`

Pasta contendo imagens utilizadas para apresentação do projeto no GitHub:

- `grafico_medias_turma.png`;
- `grafico_situacoes_turma.png`;
- `relatorio_desempenho_academico.png`.

### `relatorios/`

Pasta contendo os arquivos gerados pelo sistema:

- `relatorio_desempenho_academico.xlsx`.
```