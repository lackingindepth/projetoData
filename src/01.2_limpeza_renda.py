import pandas as pd

# Carregando os dados
pe = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PE.csv")
pe["UF"] = "PE"

al = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_AL.csv")
al["UF"] = "AL"

ba = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_BA.csv")
ba["UF"] = "BA"

ce = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_CE.csv")
ce["UF"] = "CE"

ma = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_MA.csv")
ma["UF"] = "MA"

pb = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PB.csv")
pb["UF"] = "PB"

pi = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_PI.csv")
pi["UF"] = "PI"

rn = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_RN.csv")
rn["UF"] = "RN"

se = pd.read_csv("datasets/dadosBrutos/renda_escol_trabalho_SE.csv")
se["UF"] = "SE"

renda = pd.concat([pe,al,ba,ce,ma,pb,pi,rn,se], ignore_index=True)
renda["ano"] = 2022



saúde = pd.read_csv("datasets/dadosBrutos/saude.csv")


# Limpeza dos dados de renda
renda["Salário médio mensal dos trabalhadores formais"] = renda["Salário médio mensal dos trabalhadores formais"].str.replace(",", ".").str.replace("salários mínimos", "")
renda["Salário médio mensal dos trabalhadores formais"] = pd.to_numeric(renda["Salário médio mensal dos trabalhadores formais"], errors="coerce")

# Limpeza dos dados de pessoas ocupado em postos de trabalho formais
renda["Pessoal ocupado em postos de trabalho formais"] = renda["Pessoal ocupado em postos de trabalho formais"].str.replace(".", "").str.replace(" pessoas", "")
renda["Pessoal ocupado em postos de trabalho formais"] = pd.to_numeric(renda["Pessoal ocupado em postos de trabalho formais"], errors="coerce")

# Limpeza dos dados de taxa de escolarização de 6 a 14 anos
renda["Taxa de escolarização de 6 a 14 anos"] = renda["Taxa de escolarização de 6 a 14 anos"].str.replace(",", ".").str.replace("%", "")
renda["Taxa de escolarização de 6 a 14 anos"] = pd.to_numeric(renda["Taxa de escolarização de 6 a 14 anos"], errors="coerce")

# Dataframe com a média de salário, pessoas ocupadas por estado e taxa de escolarização de 6 a 14 anos por estado
renda_estado = (
    renda.groupby("UF")
    .agg({ #.agg permite aplicar várias funções de agregação em diferentes colunas
        "Salário médio mensal dos trabalhadores formais": "mean",
        "Pessoal ocupado em postos de trabalho formais": "sum",
        "Taxa de escolarização de 6 a 14 anos": "mean"
    })
    .reset_index()
)
# Salvando os dados limpos
renda_estado.to_csv("datasets/dadosLimpos/renda_estado.csv", index=False)

#print(renda_estado.head())





