import pandas as pd

# Carregar o dataset
saude = pd.read_csv('datasets/dadosBrutos/Saúde_causas_uf_ano.csv')

# Filtrar os dados para o ano de 2022
saude = saude[
    saude['ano'] == 2022
]

# Garantir a coluna 'causa_basica' como string
saude['causa_basica'] = (saude['causa_basica'].astype(str))

""" 
Aqui vai ser listado prefixos de CIDs que representam causas evitáveis de morte.
Esses CIDs foram listados a partir do artigo X(achar), que classifica as causas de morte em evitáveis e não evitáveis.
Entre causas de mortes evitáveis estão: doenças imunopreveníveis, doenças infecciosas, causas externas, doenças não transmissíveis, etc...
 """
# Lista de CIDs que representam causas evitáveis de morte
cid_prefixos = [
    # Imunoprevenção
    "A17", "A19", "A34", "A35", "A36",
    "A37", "A80", "B05", "B06", "B16",
    "B26", "G00",

    # Doenças infecciosas
    "A15", "A16", "A18",
    "B20", "B21", "B22", "B23", "B24",
    "A09",

    # Doenças não transmissíveis
    "I20", "I21", "I22", "I23", "I24", "I25",
    "I60", "I61", "I62", "I63", "I64", "I65", "I66", "I67", "I68", "I69",
    "E10", "E11", "E12", "E13", "E14",
    "N18",
    "C34"
]

# Filtrar mortes 
saude = saude[
    (
        saude["causa_basica"]
        .str.startswith(tuple(cid_prefixos))
    )
    |
    (
        saude["causa_basica"]
        .str.startswith(("O", "V", "W", "X", "Y"))
    )
]

# Contar mortes por estado
mortes_estado = (
    saude.groupby("sigla_uf")
    .size()
    .reset_index(name="mortes_evitaveis")
)

#print(mortes_estado.head())

# Salvar dataset processado
mortes_estado.to_csv(
    "datasets/dadosProcessados/mortes_evitaveis_estado.csv",
    index=False
)




