from Ex01 import Pessoa

people = Pessoa("Tiago", 20, 58)
people.Comer("maçã")
people.Comer("maçã")


print(vars(people))  # traz todas as informações
# em dicionário