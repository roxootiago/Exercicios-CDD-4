# Escreva um algoritmo par ler uma temperatura
# em graus Fahrenheit, calcualar e escrever o
# valor correspondente em graus Celsius (
# baseado na fórmula abaixo): C = ((F-32)/9)*5
# Observação: Para testar se a sua resposta
# está correta saiba que 100 Cº =  212 F

tempFahrenheit = float(input("Digite a temperatura em fahrenheit: "))

celsius = ((tempFahrenheit - 32)/9) * 5

print(f"Temperatura em Fahrenheit: {tempFahrenheit}\nTemperatura em Celsius: {celsius}")
