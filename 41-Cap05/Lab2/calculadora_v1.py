# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def operacao(operador,x,y):
    x = input("digite um valor")
    y=input('insira um valor')
    if operador == '+':
            soma= x+y
             print('o valor é',soma)
    if operador == '-':
            sub=x-y
             print('o resultado é:', sub)
    if operador == '*':
            mult=x*y
             print("o resultado é:",multi)
    if operador == '/':
            div=x/y
                print("o resultado é:", div)
                
                
                
operacao('+',2,2)              
    