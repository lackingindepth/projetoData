#  Análise de desigualdade no nordeste

## Objetivo

Este projeto tem como objetivo analisar a relação entre desigualdade socioeconômica e indicadores de saúde e educação no nordeste.

Através de um pipeline de ETL e Análise Exploratória de Dados (EDA), investigamos como fatores como renda estão associados a:

* Taxa de analfabetismo
* Taxa de mortalidade

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/lackingindepth/projetoData.git
cd projetoData
```

---

### 2. Criar ambiente virtual

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o ETL

```bash
python src/etl.py
```

Isso irá gerar o arquivo:

```
data/processed/dados_finais.csv
```

---

### 5. Rodar a análise (Jupyter)

```bash
jupyter notebook
```

Abra o arquivo:

```
notebooks/analise_desigualdade.ipynb
```

---

##  Sobre a análise

O notebook responde às seguintes perguntas:

1. Existe relação entre renda e analfabetismo?
2. Existe relação entre renda e mortalidade?
3. Educação está relacionada com saúde?

---

##  Tecnologias utilizadas

* Python
* Pandas
* Seaborn
* Matplotlib
* Jupyter Notebook

---

##  Observações

* Os dados utilizados são públicos (IBGE / DATASUS)
* O projeto utiliza dados agregados por estado
* Os resultados indicam correlação, não causalidade

---



