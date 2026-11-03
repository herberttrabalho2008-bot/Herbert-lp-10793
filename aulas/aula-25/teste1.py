from funcoes import dobro, e_par, escalao
assert dobro(5) == 10
assert e_par(3) == True
assert escalao(20) == "maior"
print("Chegou ao fim")
# o segundo asserto vai dar erro, porque 3 não é par. O correto seria assert e_par(3) == False
# não chegou a aprarecer a mensagem "Chegou ao fim" porque o programa parou no segundo asserto.