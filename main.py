import random

#Dimensões
x = 20
y = 20
#Lista de palavras
lista_de_palavras =['mangaba','acerola','manga', 'mamao','banana','framboesa','caju','pitanga','abacaxi']
#Pista
titulo = 'Emcontre 9 frutas'

def caça_palavras(x,y):
    alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','m','o','p','q','r','s','t','u','v','w','y','z']
    
    CP =[]
    for i in range(x):
        linha = []
        for j in range(y):
            linha.append(0)
            
        CP.append(linha)
        
    
    cont = 1
    for n in range(x):
        for i in range(y):
            rand = len(alf)
            num = random.randrange(rand)
            
            CP[n][i] = alf[num]
            
            cont += 1
        
    lista_alvos_usados=[]
    for palavra in lista_de_palavras:
        x_ran = random.randrange(x)
        y_ran = random.randrange(y)
        
        if y - y_ran < len(palavra):
            
            if x - x_ran < len(palavra):
                caça_palavras(x,y)
            else:
                for i in range(len(palavra)):
                    CP[x_ran][y_ran]= palavra[i]
                    lista_alvos_usados.append((x_ran,y_ran))
                    x_ran += 1
                    
                    
        else:
            for i in range(len(palavra)):
                CP[x_ran][y_ran] = palavra[i]
                lista_alvos_usados.append((x_ran,y_ran))
                y_ran += 1
    
    with open('caça-palavras.txt', 'w+') as text_file:
        text_file.write(titulo)
        text_file.write('\n')
        text_file.write('\n')
        
        for i in CP:
            for n in i:
                text_file.write(n)
                text_file.write(' ')
            
            text_file.write('\n')
    return print('Caça-palavras gerado com sucesso!')


caça_palavras(x,y)