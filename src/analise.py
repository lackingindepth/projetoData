import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets/dadosProcessados/final_data.csv")

# Verificando dataset
print(df.head())
print(df.info())

print(df.describe())

# Existe correlação entre renda média e evasão escolar?
def renda_evasao(df):
    
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data = df,
        x = "salario_medio_mensal",
        y= "taxa_evasao_em"
    )

    sns.regplot(
        data=df,
        x="salario_medio_mensal",
        y="taxa_evasao_em",
        scatter=False,
        ci=None
    )
    
    for i in range(len(df)):
        plt.text(
        df["salario_medio_mensal"][i],
        df["taxa_evasao_em"][i],
        df["sigla_uf"][i]
    )

    plt.title("Relação entre Renda Média x taxa de evasão escolar")

    plt.xlabel("Renda Média")
    plt.ylabel("Taxa de Evasão do Ensino Médio por 100mil habitantes")

    #Salvar gráfico
    plt.savefig(
    "outputs/renda_evasao.png",
    bbox_inches="tight"
)
    plt.show()


# Existe correlação entre renda média e mortalidade evitável?
def renda_mortalidade(df):

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data = df,
        x = "salario_medio_mensal",
        y= "taxa_mortes_evitaveis"
    )
    sns.regplot(
        data=df,
        x="salario_medio_mensal",
        y="taxa_mortes_evitaveis",
        scatter=False,
        ci=None
    )

    for i in range(len(df)):
        plt.text(
            df["salario_medio_mensal"][i],
            df["taxa_mortes_evitaveis"][i],
            df["sigla_uf"][i]
        )

    plt.title("Relação entre Renda Média x Mortalidade Evitável")

    plt.xlabel("Renda Média")
    plt.ylabel("Mortalidade Evitável por 100mil habitantes")
    #Salvar gráfico
    plt.savefig(
    "outputs/renda_mortalidade.png",
    bbox_inches="tight"
)
    plt.show()

#Existe correlação entre renda média e acesso ao ensino superior?
def renda_acesso_superior(df):

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data = df,
        x = "salario_medio_mensal",
        y= "taxa_matriculas_superior"
    )
    sns.regplot(
        data=df,
        x="salario_medio_mensal",
        y="taxa_matriculas_superior",
        scatter=False,
        ci=None
    )

    for i in range(len(df)):
        plt.text(
            df["salario_medio_mensal"][i],
            df["taxa_matriculas_superior"][i],
            df["sigla_uf"][i]
        )

    plt.title("Relação entre Renda Média x Acesso ao Ensino Superior")

    plt.xlabel("Renda Média")
    plt.ylabel("Acesso ao Ensino Superior por 100mil habitantes")

    #Salvar gráfico
    plt.savefig(
        "outputs/renda_acesso_superior.png",
        bbox_inches="tight"
    )
    plt.show()

# Existe correlação entre renda média e conclusão no ensino superior?
def renda_conclusao_superior(df):

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data = df,
        x = "salario_medio_mensal",
        y= "taxa_concluintes_superior"
    )
    sns.regplot(
        data=df,
        x="salario_medio_mensal",
        y="taxa_concluintes_superior",
        scatter=False,
        ci=None
    )

    for i in range(len(df)):
        plt.text(
            df["salario_medio_mensal"][i],
            df["taxa_concluintes_superior"][i],
            df["sigla_uf"][i]
        )

    plt.title("Relação entre Renda Média x Conclusão no Ensino Superior")

    plt.xlabel("Renda Média")
    plt.ylabel("Conclusão no Ensino Superior por 100mil habitantes")
    
    #Salvar gráfico
    plt.savefig(
        "outputs/renda_conclusao_superior.png",
        bbox_inches="tight"
    )
    plt.show()

# Existe correlação entre taxa de escolarização de 6 a 14 anos e acesso ao ensino superior?
def escolarizacao_acesso_superior(df):

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data = df,
        x = "taxa_escolarizacao_6_14",
        y= "taxa_matriculas_superior"
    )
    sns.regplot(
        data=df,
        x="taxa_escolarizacao_6_14",
        y="taxa_matriculas_superior",
        scatter=False,
        ci=None
    )

    for i in range(len(df)):
        plt.text(
            df["taxa_escolarizacao_6_14"][i],
            df["taxa_matriculas_superior"][i],
            df["sigla_uf"][i]
        )

    plt.title("Relação entre Taxa de Escolarização de 6 a 14 anos x Acesso ao Ensino Superior")

    plt.xlabel("Taxa de Escolarização de 6 a 14 anos")
    plt.ylabel("Acesso ao Ensino Superior por 100mil habitantes")

    #Salvar gráfico
    plt.savefig(
        "outputs/escolarizacao_acesso_superior.png",
        bbox_inches="tight"
    )
    plt.show()

#Mapa de calor para verificar a correlação entre as variáveis
def heatmap_geral(df):

    plt.figure(figsize=(10,8))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True
    )

    plt.title("Correlação entre variáveis")

    #Salvar gráfico
    plt.savefig(
        "outputs/heatmap_geral.png",
        bbox_inches="tight"
    )

    plt.show()

