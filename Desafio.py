#1 digite seu nome

nome = input("Digite seu nome: ")
print(f"Olá, {nome}")

#2 Digite seu salário
salario = float(input("Digite seu salário: "))

#3 Valor do bônus

bonus = float(input("Digite o valor do bônus: "))

#4 calculando a bagaça

TTbonus = (bonus + salario) * bonus

# Resultado da bagaça

print(f"O AA {nome} possui o bonus de {TTbonus}")
