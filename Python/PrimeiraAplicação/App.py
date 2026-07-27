import os 

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('clear')
    print('Finalizando app')


if opcao == 1:
    print('Cadastrar restaurante')
elif opcao == 2:
    print('Listar restaurantes')
elif opcao == 3:
    print('Ativar restaurantes')
else:
    finalizar_app()



a = 3.5
    