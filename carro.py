def definir(carro, combustivel, portas, pessoas, bagageiro):
    km_por_litro = {
        "BMW": {"gasolina": 9.8, "alcool": 8.9},
        "AUDI": {"gasolina": 12.8, "alcool": 10.9},
        "FIAT": {"gasolina": 26.8, "alcool": 24.9},
        "FERRARI": {"gasolina": 13.8, "alcool": 12.9}
    } 

    km = km_por_litro[carro][combustivel]

    if portas > 4:
        km -= 0.5
    if pessoas > 2:
        km -= 1.2
    if bagageiro:
        km -= 0.2
    return km


carro = input("Digite o tipo de carro (BMW, AUDI, FIAT ou FERRARI): ").upper()
combustivel = input("Digite o tipo de combustível (gasolina ou alcool): ")
portas = int(input("Digite o número de portas do carro: "))
pessoas = int(input("Digite o número de pessoas viajando no carro: "))
bagageiro = input("O carro possui bagageiro (sim ou nao)? ").lower() == "sim"

km_rodado = definir(carro, combustivel, portas, pessoas, bagageiro)
print("Tipo de combustível:" + combustivel)
print(f"Tipo de carro: {carro}")
print("Tipos de casos escolhidos:")
print(f"Combustivel {combustivel} \n Portas: {str(portas)} \n Pessoas: {str(pessoas)}")

if bagageiro:
    print("Bagageiro: Sim")
else: 
    print("Bagageiro: Nao")

print(f"KM rodado: {km_rodado:.2f} Km/l")