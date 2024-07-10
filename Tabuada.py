#message
print("*"*31)
print("*Tabuada completa (do 1 ao 10)*")
print("*"*31)
#num input
numero = int( input("Digite um número: ") )

#function
def tabuada():
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

#call function
tabuada()
