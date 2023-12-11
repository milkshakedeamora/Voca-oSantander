altura = float(input("Digite sua altura:"))
if(altura > 100):
    altura/=100
peso = float(input("Digite seu peso:"))
print(f"IMC:{(peso/(altura*altura)):.2f}")