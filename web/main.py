import random
import string
import glob
from flask import Flask, render_template, redirect, url_for, request, session,send_file
from reportlab.pdfgen.canvas import Canvas


app = Flask(__name__)
app.secret_key = 'teste'

@app.route('/',methods = ['POST','GET'])
def home():
    if request.method == "POST":
        lista = request.form['nm']
        session['lista'] = lista.upper()
        session['dica'] = request.form['dica']
        session['x'] = request.form['dimensoes'] 
        
        session['y'] = request.form['dimensoes']
        session['nome_arquivo'] = request.form['arquivo']
        return redirect(url_for('gerador'))
    else:
        return render_template('index.html')

@app.route('/acervo')
def acervo():
    files = []
    names= []
    for file in glob.glob('./static/img/*.*'):
        files.append(file)
    for name in files:
        names.append(name.split('/')[-1])
    return render_template('acervo.html',files = files, names = names)

@app.route('/gerador')
def gerador():
    if 'lista' in session:
        x= int(session['x'])
        y = int(session['y'])
        titulo = session['dica']
        lista = session['lista'].split(',')
        nome_arquivo = session['nome_arquivo']
        import random
        import string
        alf = string.ascii_uppercase
        
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
        lista_de_palavras = lista
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
                    CP[x_ran][y_ran] = palavra[i].upper()
                    lista_alvos_usados.append((x_ran,y_ran))
                    y_ran += 1
        
        # arquivo = 'files/'+ nome_arquivo + '.txt'
        
        # # with open(arquivo, 'w+') as text_file:
        #     text_file.write(titulo)
        #     text_file.write('\n')
        #     text_file.write('\n')
            
        #     for i in CP:
        #         for n in i:
        #             text_file.write(n)
        #             text_file.write(' ')
                
        #         text_file.write('\n')
        arquivo ='files/' + nome_arquivo + '.pdf'
        canvas = Canvas(arquivo, pagesize = 'LETTER')
        canvas.setFont('Times-Bold',20)
        canvas.drawString(220,700,titulo)
        canvas.setFont('Times-Roman',10)
        
        if x == 30:
            v = 600
            for i in CP:
                h = 100
                for n in i:
                
                    canvas.drawString(h,v,n)
                    h += 15
                v -= 15    
            canvas.save()
            return send_file(arquivo,as_attachment=True)
        if x == 20:
            v = 600
            for i in CP:
                h = 150
                for n in i:
                
                    canvas.drawString(h,v,n)
                    h += 15
                v -= 15    
                
            canvas.save()
            return send_file(arquivo,as_attachment=True)
    else:
        return redirect(url_for('home'))
