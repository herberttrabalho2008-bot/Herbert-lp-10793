import pandas as pd
from funcoes import total_acidentes_por


def test_total_acidentes_por():
    df = pd.DataFrame({
        "causa": ["Velocidade", "Distração", "Velocidade"],
        "acidentes": [4, 5, 3],
    })
    resultado = total_acidentes_por(df, "causa")
    assert resultado["Velocidade"] == 7
    assert resultado["Distração"] == 5
