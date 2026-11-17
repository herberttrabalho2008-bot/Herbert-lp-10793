def total_acidentes_por(df, coluna):
    return df.groupby(coluna)["acidentes"].sum()
