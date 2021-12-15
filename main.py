import tkinter
from tkinter import *
from tkinter import ttk

#Cores

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# Cria janela principal

janela = Tk()
janela.title('Tic Tac Toe')
janela.geometry('260x374')
janela.configure(bg=fundo)
janela.resizable(False, False)
janela.iconphoto(False, PhotoImage(file='./logo.png'))



# Dividindo a janela em 2 frames
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando o frame_cima
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=16)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)

# Configurando o frame_baixo

# Criando Lógica

jogador_1 = 'X'
jogador_2 = 'O'

pontos_1 = 0
pontos_2 = 0

tabela = [['1','2','3'], ['4','5','6'], ['7','8','9']]

jogando = 'X'
jogar = ''
contador = 0
contador_de_rodadas = 0

def iniciar_jogo():
    b_jogar.place(x=800, y=800)
    #controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        # comparando valor recebido
        if i == str(1):
            # verificando se a posicao está vazia
            if b_0['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(2):
            # verificando se a posicao está vazia
            if b_1['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(3):
            # verificando se a posicao está vazia
            if b_2['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(4):
            # verificando se a posicao está vazia
            if b_3['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(5):
            # verificando se a posicao está vazia
            if b_4['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(6):
            # verificando se a posicao está vazia
            if b_5['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(7):
            # verificando se a posicao está vazia
            if b_6['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(8):
            # verificando se a posicao está vazia
            if b_7['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        if i == str(9):
            # verificando se a posicao está vazia
            if b_8['text'] == '':
                # verificando quem está jogando e definir símbolo
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definir a cor do texto e gravar posicao na tabela
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                # verifica quem está jogando para trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementar contador
                contador += 1

        # verifica se houve vencedor
        if contador >= 5:
                # linhas
                if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                    vencedor(jogando)
                elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                    vencedor(jogando)
                elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                    vencedor(jogando)

                # colunas
                if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                    vencedor(jogando)
                elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                    vencedor(jogando)
                elif tabela[0][0] == tabela[1][2] == tabela[2][2] != "":
                    vencedor(jogando)

                # colunas
                if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                    vencedor(jogando)

                # empate
                if contador >= 9:
                    vencedor('Foi empate!')



    # para decidir o vencedor
    def vencedor(i):
        global tabela
        global pontos_1
        global pontos_2
        global contador_de_rodadas
        global contador


        #bloqueando botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=40, y=224)

        if i == 'X':
            pontos_2+=1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_o_pontos['text'] = pontos_2

        if i == 'O':
            pontos_1+=1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_x_pontos['text'] = pontos_1

        if i == 'Foi empate!':
            app_vencedor['text'] = 'Foi empate!'

        def restart():
            # limpando tela
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

            # reiniciando a tabela
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

            app_vencedor.destroy()
            b_jogar.destroy()



        # botão start
        b_jogar = Button(frame_baixo, command=restart, text='Próxima Rodada', font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=65, y=195)


        def game_over():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if pontos_1 == 3:
            game_over()
        elif pontos_2 == 3:
            game_over()
        else:
            contador_de_rodadas +=1
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0

    # terminar o jogo
    def terminar():
        global tabela
        global contador_de_rodadas
        global pontos_1
        global pontos_2
        global contador

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contador_de_rodadas = 0
        pontos_1 = 0
        pontos_2 = 0
        contador = 0

        #bloqueando botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_fim = Label(frame_baixo, text='O JOGO ACABOU', relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_fim.place(x=55, y=90)

        # jogar de novo

        def jogar_novamente():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            iniciar_jogo()

        # botão start
        b_jogar = Button(frame_baixo, command=jogar_novamente, text='Jogar Novamente', font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=65, y=195)

    # linhas verticais
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0,
                 fg=co0)
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0,
                 fg=co0)
    app_.place(x=157, y=15)

    # linhas horizontais
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'),
                 bg=co0, fg=co0)
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'),
                 bg=co0, fg=co0)
    app_.place(x=30, y=123)


    # botões linha 0
    b_0 = Button(frame_baixo, command=lambda:controlar('1'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_0.place(x=30, y=15)
    b_1 = Button(frame_baixo, command=lambda:controlar('2'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_1.place(x=96, y=15)
    b_2 = Button(frame_baixo, command=lambda:controlar('3'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_2.place(x=163, y=15)

    # botões linha 1
    b_3 = Button(frame_baixo, command=lambda:controlar('4'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_3.place(x=30, y=75)
    b_4 = Button(frame_baixo, command=lambda:controlar('5'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_4.place(x=96, y=75)
    b_5 = Button(frame_baixo, command=lambda:controlar('6'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_5.place(x=163, y=75)

    # botões linha 2
    b_6= Button(frame_baixo, command=lambda:controlar('7'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_6.place(x=30, y=135)
    b_7= Button(frame_baixo, command=lambda:controlar('8'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_7.place(x=96, y=135)
    b_8= Button(frame_baixo, command=lambda:controlar('9'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat' , bg=fundo, fg=co7)
    b_8.place(x=163, y=135)

# botão jogar
b_jogar = Button(frame_baixo, command=iniciar_jogo,  text='Jogar', width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised' , bg=fundo, fg=co0)
b_jogar.place(x=80, y=195)



janela.mainloop()