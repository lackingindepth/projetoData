import pandas as pd

# Carregando os dados
pe = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PE.csv")
pe["sigla_uf"] = "PE"

al = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_AL.csv")
al["sigla_uf"] = "AL"

ba = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_BA.csv")
ba["sigla_uf"] = "BA"

ce = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_CE.csv")
ce["sigla_uf"] = "CE"

ma = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_MA.csv")
ma["sigla_uf"] = "MA"

pb = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PB.csv")
pb["sigla_uf"] = "PB"

pi = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PI.csv")
pi["sigla_uf"] = "PI"

rn = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_RN.csv")
rn["sigla_uf"] = "RN"

se = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_SE.csv")
se["sigla_uf"] = "SE"

renda = pd.concat([pe,al,ba,ce,ma,pb,pi,rn,se], ignore_index=True)
renda["ano"] = 2022


#renda.columns = renda.columns.str.strip() # Remove espaços em branco dos nomes das colunas *Tirei pq tava dando bug

# Limpeza dos dados de renda
renda["Salário médio mensal dos trabalhadores formais "] = (
    renda["Salário médio mensal dos trabalhadores formais "]
    .str.replace(",", ".").str.replace("salários mínimos", "").str.strip()
)

# Convertendo a coluna de salário médio mensal dos trabalhadores formais para numérica, tratando erros como NaN
renda["Salário médio mensal dos trabalhadores formais "] = pd.to_numeric(renda["Salário médio mensal dos trabalhadores formais "], errors="coerce")

# Limpeza dos dados de pessoas ocupado em postos de trabalho formais
renda["Pessoal ocupado em postos de trabalho formais"] = (
    renda["Pessoal ocupado em postos de trabalho formais"]
    .str.replace(".", "").str.replace(" pessoas", "")
)

# Convertendo a coluna de pessoas ocupado em postos de trabalho formais para numérica, tratando erros como NaN
renda["Pessoal ocupado em postos de trabalho formais"] = pd.to_numeric(renda["Pessoal ocupado em postos de trabalho formais"], errors="coerce")

# Limpeza dos dados de taxa de escolarização de 6 a 14 anos
renda["Taxa de escolarização de 6 a 14 anos de idade"] = (
    renda["Taxa de escolarização de 6 a 14 anos de idade"]
    .str.replace(",", ".").str.replace("%", "")
)

# Convertendo a coluna de taxa de escolarização de 6 a 14 anos de idade para numérica, tratando erros como NaN
renda["Taxa de escolarização de 6 a 14 anos de idade"] = pd.to_numeric(renda["Taxa de escolarização de 6 a 14 anos de idade"], errors="coerce")

# Dataframe com a média de salário, pessoas ocupadas por state e taxa de escolarização de 6 a 14 anos de idade por state
renda_estado = (
    renda.groupby("sigla_uf")
    .agg({ #.agg permite aplicar várias funções de agregação em diferentes colunas
        "Salário médio mensal dos trabalhadores formais ": "mean",
        "Pessoal ocupado em postos de trabalho formais": "sum",
        "Taxa de escolarização de 6 a 14 anos de idade": "mean"
    })
    .reset_index()
)

print(renda_estado["Salário médio mensal dos trabalhadores formais "]) #test

# Salvando os dados limpos
renda_estado.to_csv("datasets/dadosProcessados/renda_estado.csv", index=False)

#print(renda_estado.head())





