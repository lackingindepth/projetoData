import pandas as pd

# Carregar os datasets
renda = pd.read_csv("datasets/dadosProcessados/renda_estado.csv")   

mortes = pd.read_csv("datasets/dadosProcessados/mortes_evitaveis_estado.csv")

educacao = pd.read_csv("datasets/dadosProcessados/educacao_por_estado.csv")

populacao = pd.read_csv("datasets/dadosBrutos/populacao.csv")

"""Eles estão limpos, mas ainda não estão prontos para serem usados na análise. 
Precisamos fazer uma fusão dos dados para criar um dataframe final que contenha todas as informações relevantes para a análise.
O método merge do pandas chama o dataframe que queremos juntar, o nome do dataframe que queremos juntar, a coluna que queremos usar para juntar os dataframes e o tipo de junção que queremos fazer (inner, outer, left, right).

Ao final, teremos um dataframe com as seguintes colunas:

sigla_uf, 
salário médio mensal dos trabalhadores formais,
pessoal ocupado em postos de trabalho formais,
taxa de escolarização de 6 a 14 anos de idade,
mortes evitáveis por estado,
taxa de evasão do ensino médio,
taxa de repetência do ensino médio,
taxa de promoção do ensino médio.
"""

final = pd.merge(renda, mortes, on="sigla_uf", how="inner") # inner join para manter apenas os estados que estão presentes em ambos os datasets

final = pd.merge(final, educacao, on="sigla_uf", how="inner")

final = pd.merge(final, populacao, on="sigla_uf", how="inner")

# Renomear a coluna de salário médio mensal para facilitar a análise
final = final.rename(columns={
    "Salário médio mensal dos trabalhadores formais ": "salario_medio_mensal",
    "Taxa de escolarização de 6 a 14 anos de idade": "taxa_escolarizacao_6_14",})



""" Para aumentar a precisão da análise, usaremos 100mil habitantes como base para calcular as taxas
Isso é feito para evitar que os estados com populações maiores tenham um peso desproporcional na análise, 
e para permitir uma comparação mais justa entre os estados, independentemente do tamanho da população.
"""

final["taxa_mortes_evitaveis"] = (
    final["mortes_evitaveis"] #mortes dividas pelo número de habitantes vezes 100mil
    / final["populacao"]
) * 100000

final["taxa_matriculas_superior"] = (
    final["quantidade_matriculas_superior"] #matrículas no ensino superior dividas pelo número de habitantes vezes 100mil
    / final["populacao"]
) * 100000

final["taxa_concluintes_superior"] = (
    final["quantidade_concluintes_superior"] #concluintes no ensino superior dividas pelo número de habitantes vezes 100mil
    / final["populacao"]
) * 100000

final["taxa_evasao_em"] = (
    final["taxa_evasao_em"] #taxa de evasão do ensino médio divida pelo número de habitantes vezes 100mil
    / final["populacao"]
) * 100000


final.to_csv("datasets/dadosProcessados/final_data.csv", index=False)

print(final.shape)
print(final["sigla_uf"].unique())