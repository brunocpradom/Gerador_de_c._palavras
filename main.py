import random
import string
from reportlab.pdfgen.canvas import Canvas


class CaçaPalavras():
    
    def __init__(self,lista_de_palavras,dimensoes,dica , nome_do_arquivo):
        """
        CaçaPalavras.__init__(self, lista_de_palavras, dimensoes, dica, nome_do_arquivo)
        
            self.lista_de_palavras : list
                parâmetro : lista contendo todas as palavras que serão inseridas no caça-palavras
            
                ex: self.lista_de_palavras = ['azul','vermelho','amarelo','preto',]
                
            self.dimensoes : int
                parâmetro : número inteiro representando as dimensões do caça-palavras. Ao escolher
            o número 10, será gerado um de dimensões 10 X 10 , escolhendo 20 , 20 X 20 , sendo a unidade
            relativa a uma letra.
            
                ex: self.dimensoes = 20
            
            self.dica : str
                parâmetro : String contendo uma dica referente às palavras que devem ser encontradas.
                
                ex: 'Encontre 4 cores'
            
            self.nome_do_arquivo : str
                parâmetro : string contendo o nome do arquivo
        
        """
        
        self.lista_de_palavras = lista_de_palavras
        self.dimensoes = dimensoes
        self.dica = dica
        self.nome_do_arquivo = nome_do_arquivo
        
    
    def gerador(self):
        #Criando lista de letras que serão usadas para criar a base do caça-palavras
        alf = string.ascii_uppercase
        #Definindo dimensões do caça-palavras
        x = y = self.dimensoes
        #Criando base, que consiste de uma matriz com letras escolhidas aleatoriamente
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
        for palavra in self.lista_de_palavras:
            x_ran = random.randrange(x)
            y_ran = random.randrange(y)
            
            if y - y_ran < len(palavra):
                
                if x - x_ran < len(palavra):
                    self.gerador()
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
        #Salvando em um arquivo PDF
        nome_do_arquivo = self.nome_do_arquivo + '.pdf'
        #Criando PDF
        canvas = Canvas(nome_do_arquivo, pagesize = 'LETTER')
        canvas.setFont('Times-Bold', 20)
        #Escrevendo a dica do caça-palavras nas coordenadas 250, 700
        canvas.drawString(250,700, self.dica)
        #Mudando fonte para escrever o corpo do caça palavras
        canvas.setFont('Times-Roman',10)
        
        v = 600
        for i in CP:
            h = 150
            for n in i:
            
                canvas.drawString(h,v,n)
                h += 15
            v -= 15    
            
        canvas.save()
        return True

if __name__ == '__main__':
    #Exemplo 
    teste = CaçaPalavras(['BRASIL', 'ARGENTINA','BOLIVIA'],20,'Encontre três países','paises')
    teste.gerador()

