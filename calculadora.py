
quantidade = int(input("Quantas notas você deseja calcular? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota

media = soma / quantidade
print(f"\nA média das {quantidade} notas é: {media:.2f}")   