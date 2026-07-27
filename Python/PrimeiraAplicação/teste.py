from decimal import Decimal
# a = Decimal("1.8")

# print(type(a))



a = Decimal(input("digite um número: "))
b = Decimal(input("digite outro número: "))

resultado = a + (a * b)

print(f"O valor final é: {resultado}")