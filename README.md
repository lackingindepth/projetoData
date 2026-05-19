# Análise de Desigualdade Social no Nordeste Brasileiro

## Objetivo

Este projeto tem como objetivo analisar relações entre indicadores de renda, educação e saúde nos estados do Nordeste brasileiro no ano de 2022.

Através de ETL e de uma Análise Exploratória de Dados, investigamos como fatores socioeconômicos estão associados a indicadores educacionais e de mortalidade evitável.

As análises buscam identificar possíveis associações entre:

- renda média da população;
- acesso ao ensino superior;
- evasão escolar;
- taxa de escolarização;
- mortalidade por causas evitáveis.

---

# Bases de dados utilizadas

Os dados utilizados são públicos e provenientes de:

- IBGE
- Base dos Dados
- DATASUS
- Censo Demográfico

Os datasets utilizados contemplam:

- renda média e emprego formal;
- taxa de escolarização;
- indicadores da educação básica;
- indicadores do ensino superior;
- mortalidade por causas evitáveis classificadas segundo CID-10.

---

# Estrutura do projeto

```text
projetoData/
│
├── datasets/
│   ├── dadosBrutos/
│   └── dadosProcessados/
│
├── graficos/
│
├── src/
│   ├── limpeza_renda.py
│   ├── limpeza_educacao_basica.py
│   ├── limpeza_educacao_superior.py
│   ├── limpeza_saude.py
│   ├── merge_datasets.py
│   └── analise.py
│
├── main.py
├── requirements.txt
└── README.md

```
# Como executar o projeto

1. Clonar o repositório
```
git clone https://github.com/lackingindepth/projetoData.git
cd projetoData
```

2. Criar ambiente virtual
```
Windows
python -m venv venv
venv\Scripts\activate
```
```
Linux
python3 -m venv venv
source venv/bin/activate
```
4. Instalar dependências
```
pip install -r requirements.txt
```

6. Executar o projeto
```
python main.py
```

O script irá:

realizar a análise dos dados processados;
gerar automaticamente os gráficos;
salvar os resultados na pasta graficos/.
Variáveis analisadas
Indicadores de renda
salário médio dos trabalhadores formais;
quantidade de empregados formais;
taxa de alfabetização.
Indicadores educacionais
Educação básica
taxa de evasão no ensino médio;
taxa de repetência no ensino médio;
taxa de promoção no ensino médio.
Ensino superior
taxa de matrículas no ensino superior;
taxa de concluintes no ensino superior.
Indicadores de saúde
taxa de mortalidade por causas evitáveis.

As mortes evitáveis foram definidas a partir de grupos CID-10 relacionados a:

doenças imunopreveníveis;
doenças infecciosas;
doenças crônicas não transmissíveis;
causas maternas;
causas externas.

# Perguntas da análise

## Os gráficos produzidos pelo projeto buscam responder às seguintes perguntas:

Existe relação entre renda média e evasão escolar?
Existe relação entre renda média e mortalidade evitável?
Existe relação entre renda média e acesso ao ensino superior?
Existe relação entre renda média e conclusão no ensino superior?
Existe relação entre acesso ao ensino superior e mortalidade evitável?

# Metodologia

## O projeto foi desenvolvido em três etapas principais:

### 1. ETL
limpeza dos datasets;
padronização das colunas;
tratamento de valores ausentes;
filtragem para o ano de 2022;
integração dos datasets.

### 2. Normalização dos indicadores

Variáveis absolutas foram normalizadas pela população estadual para evitar distorções causadas por diferenças populacionais entre os estados.

### 3. Análise exploratória

Foram utilizados gráficos de dispersão, linhas de regressão e matrizes de correlação para identificar tendências e associações entre os indicadores.

## Tecnologias utilizadas
Python
Pandas
Matplotlib
Seaborn


## Observações
Os dados utilizados são públicos.
O projeto utiliza dados agregados por estado.
Os resultados representam associações estatísticas e não relações de causalidade.
O projeto possui caráter educacional.

