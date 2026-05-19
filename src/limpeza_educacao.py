import pandas as pd

# Carregando os dados
educacao_superior = pd.read_csv("datasets/dadosBrutos/Edu_EnsinoSuperior.csv")

educacao_basica = pd.read_csv("datasets/dadosBrutos/Edu_EnsinoBasico_UF.csv")

#---------------------Limpeza dos dados de educação superior

# Selecionando apenas as colunas relevantes para a análise
educacao_superior = educacao_superior[
    [   
        "ano",
        "sigla_uf",
        "quantidade_matriculas",
        "quantidade_concluintes"
    ]
]

educacao_superior = educacao_superior.rename(columns={
    "quantidade_matriculas": "quantidade_matriculas_superior",
    "quantidade_concluintes": "quantidade_concluintes_superior"
})

# Removendo espaços em branco das colunas de quantidade de matrículas e concluintes
educacao_superior["quantidade_matriculas_superior"] = educacao_superior["quantidade_matriculas_superior"].str.strip()

educacao_superior["quantidade_concluintes_superior"] = educacao_superior["quantidade_concluintes_superior"].str.strip()



# Garantindo padrão de sigla de estado
educacao_superior["sigla_uf"] = (
    educacao_superior["sigla_uf"]    .str.strip()
    .str.upper()
)

# Convertendo as colunas de quantidade de matrículas e concluintes para numéricas, tratando erros como NaN
colunas_numericas = [
    "quantidade_matriculas_superior",
    "quantidade_concluintes_superior"
]

educacao_superior[colunas_numericas] = (
    educacao_superior[colunas_numericas]
    .apply(pd.to_numeric, errors="coerce")
)

# Agrupando os dados por estado e somando as matrículas e concluintes
educacao_superior_estado = (
    educacao_superior.groupby("sigla_uf")
    [
        [
            "quantidade_matriculas_superior",
            "quantidade_concluintes_superior"
        ]
    ]
    .sum()
    .reset_index()
)





"""-----------------------------------------------------------------------------------
Limpeza dos dados de educação básica
--------------------------------------------------------------------------------------"""

# Selecionando apenas as colunas relevantes para a análise
educacao_basica = educacao_basica[
    educacao_basica["rede"] == "Pública"
]
educacao_basica = educacao_basica[
    [
        "sigla_uf",
        "taxa_evasao_em",
        "taxa_repetencia_em",
        "taxa_promocao_em"
    ]
]

# Removendo espaços em branco das colunas de taxa de evasão, repetência e promoção
educacao_basica["taxa_evasao_em"] = educacao_basica["taxa_evasao_em"].str.strip()
educacao_basica["taxa_repetencia_em"] = educacao_basica["taxa_repetencia_em"].str.strip()
educacao_basica["taxa_promocao_em"] = educacao_basica["taxa_promocao_em"].str.strip()


# Garantindo padrão de sigla de estado
educacao_basica["sigla_uf"] = (
    educacao_basica["sigla_uf"]    .str.strip()
    .str.upper()
)

# Convertendo as colunas de taxa de evasão, repetência e promoção para numéricas, tratando erros como NaN
colunas_num = [
    "taxa_evasao_em",
    "taxa_repetencia_em",
    "taxa_promocao_em"
]

educacao_basica[colunas_num] = (
    educacao_basica[colunas_num].apply(pd.to_numeric, errors="coerce")
)
# Agrupar por estado
educacao_basica_estado = (
    educacao_basica.groupby("sigla_uf")
    [
        [
            "taxa_evasao_em",
            "taxa_repetencia_em",
            "taxa_promocao_em"
        ]
    ]
    .mean()
    .reset_index()
)

#Visualizando os dados de educação superior e básica por estado
#print(educacao_superior_estado.head())
#print(educacao_basica_estado.head())

"""Concatenando os dataframes de educação superior e básica por estado
gerando um dataframe final com as seguintes colunas:

sigla_uf,
quantidade_matriculas_superior,
quantidade_concluintes_superior,
taxa_evasao_em,
taxa_repetencia_em,
taxa_promocao_em

"""
educacao_por_estado = pd.merge(
    educacao_superior_estado,
    educacao_basica_estado,
    on="sigla_uf",
    how="inner"
)

# Salvando os dataframes limpos

#educacao_superior_estado.to_csv("datasets/dadosLimpos/educacao_superior_estado.csv", index=False)
#educacao_basica_estado.to_csv("datasets/dadosLimpos/educacao_basica_estado.csv", index=False)

educacao_por_estado.to_csv("datasets/dadosProcessados/educacao_por_estado.csv", index=False)

#print(educacao_por_estado.head())