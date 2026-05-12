# FarmTech Solutions — Modelagem de IA
## FIAP IA 2026/1 | Fase 3 — Cap 10 | Grupo 45

**Alunos:** Vinicius Anjos · Higor · igor · Humberto
**Prazo:** 19/05/2026

---

## Sobre o Projeto

Análise exploratória e modelagem preditiva com o dataset `produtos_agricolas.csv`.
O objetivo é recomendar a cultura agrícola ideal com base em condições de solo e clima.

## Estrutura do Repositório

```
fiap-ia-fase3-grupo45/
├── produtos_agricolas.csv                  # Dataset principal
├── parte1_exploracao_VINICIUS.ipynb        # Vinicius
├── parte2_descritiva_HIGOR.ipynb           # Higor
├── parte3_perfil_igor.ipynb             # igor
├── parte4_modelos_HUMBERTO.ipynb          # Humberto
├── referencia_notebook_completo.ipynb      # Referência (não editar)
└── README.md
```

## Divisão do Trabalho

| Parte | Responsável | Conteúdo |
|---|---|---|
| 1 | Vinicius | Carregamento + Análise Exploratória (gráficos 1-2) |
| 2 | Higor | Correlação + Análise Descritiva + Achados (gráficos 3-5) |
| 3 | igor | Perfil Ideal + Comparação de 3 Culturas (gráfico 6) |
| 4 | Humberto | 5 Modelos Preditivos + Comparação + Conclusões (gráficos 7-9) |

## Git Workflow

```bash
# 1. Clone o repositório
git clone https://github.com/vinialveslopesanjos/fiap-ia-fase3-grupo45.git
cd fiap-ia-fase3-grupo45

# 2. Crie sua branch (use seu nome)
git checkout -b parte1-vinicius   # ou parte2-higor, parte3-igor, parte4-humberto

# 3. Trabalhe no seu notebook

# 4. Salve e suba
git add seu_notebook.ipynb
git commit -m "feat: parte 1 concluída"
git push origin parte1-vinicius
```

## Como Rodar

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook
```
