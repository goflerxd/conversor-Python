# Conversor de temperatura - CEL - FAH - KEL
# Dia - 20/05/2021

print("###################################")
print("#### Conversor de Temperaturas ####")
print("###################################")

c = 0
f = 0
k = 0
opcao = True

while opcao != False:
    print("Menu:")
    print('1 - Celsius para Fahrenheit')
    print('2 - Fahrenheit para Celsius')
    print('3 - Celsius para Kelvin')
    print('4 - Kelvin para Celsius')
    print('5 - Fahrenheit para Kelvin')
    print('6 - Kelvin para Fahrenheit')
    print('0 - Sair')


    menu = int(input("Digite a temperatura desejada   "))
    
    if (menu >= 0 ) and (menu <= 6):
        if menu == 1:
            c = float(input('Digite a temperatura em Celsius:  '))
            f = (c * 9/5) + 32
            print('A temperatura em Fahrenheit é de:   ',round(f,2),'º')
        if menu == 2:
            f = float(input('Digite a temperatura em Fahrenheit: '))
            c = (f - 32) * 5/9
            print('Temperatura em Celsius é de',round(c,2),'º')
        if menu == 3:
            c = float(input('Digite a temperatura em Celsius: '))
            k = c + 273.15
            print('Temperatura em Kelvin é de',round(k,2),'º')
        if menu == 4:
            k = float(input('Digite a temperatura em Kelvin: '))
            c = k - 273.15
            print('Temperatura em Celsius é de',round(c,2),'º')
        if menu == 5:
            f = float(input('Digite a temperatura em Fahrenheit: '))
            k = (f - 32) * 5/9 + 273.15
            print('Temperatura em Celsius é de',round(c,2),'º')
        if menu == 6:
            k = float(input('Digite a temperatura em Kelvin:  '))
            f = (k - 272.15) * 9/5 + 32
            print('A Temperatura em Fahrenheit:  ', round(f,2),'º')

    else:
        print('####### Opção inválida! #######')
    

    
    
print('#########################################################')
print('############# Obrigado por usar nosso App! ##############')
print('######### Digite Enter para continuar    ###############')
input("Enter")