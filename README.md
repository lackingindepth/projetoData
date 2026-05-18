#  Análise de desigualdade no nordeste

## Objetivo

Este projeto tem como objetivo analisar a relação entre renda e indicadores de saúde e educação no nordeste.

Através de um pipeline de ETL e Análise Exploratória de Dados (EDA), investigamos como fatores como renda estão associados a:

* Taxa de analfabetismo
* Taxa de mortalidade evitável

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

```
```

##  Sobre a análise

Os gráficos respondem às seguintes perguntas:

1. Existe relação entre renda e analfabetismo?
2. Existe relação entre renda e mortalidade evitável?
3. Educação está relacionada com saúde?

---

##  Tecnologias utilizadas

* Python
* Pandas
* Seaborn
* Matplotlib

---

##  Observações

* Os dados utilizados são públicos (IBGE / DATASUS / Censo)
* O projeto utiliza dados agregados por estados e municípios 
* Os resultados indicam correlação, não causalidade

---



