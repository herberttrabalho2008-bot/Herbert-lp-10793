# ficheiro funcoes.py
def nivel_vendas(quantidade):
 if quantidade >= 50:
    return "alto"
 return "baixo"
# ficheiro test_vendas.py
from funcoes import nivel_vendas
def test_nivel_vendas():
 assert nivel_vendas(80) == "alto"
 assert nivel_vendas(49) == "baixo"
 assert nivel_vendas(50) == "alto"
