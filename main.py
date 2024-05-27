from tkinter import *
from PIL import Image, ImageTk
import random

co0 = "#f0f3f5"  # cinza / grey
co1 = "#feffff"  # branca / white
co2 = "#DA70D6"  # Violeta / Orchid 
co3 = "#38576b"  # azul / blue
co4 = "#FF69B4"  # Rosa / HotPink

janela = Tk()
janela.title("Mini game")
janela.geometry('400x260')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

# Criando frames
frame_cima = Frame(janela, width=500, height=50, bg=co2)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=210, bg=co4)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame cima
l_app = Label(frame_cima, text='Acenda as Lâmpada', anchor=NE, font=('Comic Sans MS', 20, 'bold'), bg=co2, fg=co0)
l_app.place(x=5, y=5)  

# Configurando frame baixo
img_2 = Image.open('2.png')
img_2 = img_2.resize((40, 40))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('3.png')
img_3 = img_3.resize((40, 40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('4.png')
img_4 = img_4.resize((40, 40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('5.png')
img_5 = img_5.resize((40, 40))
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo, image=img_2, bg=co4)
l_img.place(x=30, y=10)
l_estado = Label(frame_baixo, text='Estou sem luz', anchor=NE, font=('Comic Sans MS', 13), bg=co4, fg=co1)
l_estado.place(x=80, y=20)

global control, attempts, max_attempts

def ligarLampada(i):
    global control, attempts

    if attempts >= max_attempts:
        game_over()
        return

    lista = i
    if lista[1] == 'interruptor - 1':
        b_interruptor_1['state'] = 'disable'
    elif lista[1] == 'interruptor - 2':
        b_interruptor_2['state'] = 'disable'
    elif lista[1] == 'interruptor - 3':
        b_interruptor_3['state'] = 'disable'
    elif lista[1] == 'interruptor - 4':
        b_interruptor_4['state'] = 'disable'
    else:
        b_interruptor_5['state'] = 'disable'
    
    def substituirValor(i):
        global control
        novaLista = []

        for i in control:
            novoValor = i.replace(i[0],i[1])
            novaLista.append(novoValor)

        control = novaLista

    
    valorSelecionado = random.choice(lista[0])
    
    if int(valorSelecionado) == 1:
        if control[0] == 'lampada_1':
            l_img_1['image'] = img_1
            l_img['image'] = img_3
            l_estado['text'] = 'Obrigada!'
            substituirValor(['lampada_1',str(1)])
        else:
            if control[1] == 'lampada_2':
                l_img_2['image'] = img_1
                l_img['image'] = img_4
                l_estado['text'] = 'Ascenda a ultima'
                substituirValor(['lampada_2',str(2)])
            else:
                if control[2] == 'lampada_3':
                    l_img_3['image'] = img_1
                    l_img['image'] = img_5
                    l_estado['text'] = 'Você conseguiu!'
                    substituirValor(['lampada_3',str(3)])
    
    attempts += 1
    if attempts >= max_attempts:
        game_over()

def game_over():
    global attempts
    attempts = 0
    game_over_window = Toplevel(janela)
    game_over_window.title("Você perdeu :c")
    game_over_window.geometry("300x100")
    game_over_window.configure(background=co4)
    Label(game_over_window, text="GAME OVER", font=('Comic Sans MS', 20, 'bold'), bg=co4, fg=co0).pack(pady=10) 
    Button(game_over_window, text="Pressione ENTER para reiniciar", font=('Comic Sans MS', 8, 'bold'), bg=co1, fg=co2, command=lambda: reset_game(game_over_window)).pack(pady=10)
    game_over_window.bind('<Return>', lambda event: reset_game(game_over_window))

def reset_game(window):
    global control, attempts
    control = ['lampada_1', 'lampada_2', 'lampada_3']
    attempts = 0
    for button in [b_interruptor_1, b_interruptor_2, b_interruptor_3, b_interruptor_4, b_interruptor_5]:
        button['state'] = 'normal'
    window.destroy()

control = ['lampada_1', 'lampada_2', 'lampada_3']
attempts = 0
max_attempts = 3

def vitoria():
    global attempts
    attempts = 0
    vitoria_window = Toplevel(janela)
    vitoria_window.title("Você Venceu!")
    vitoria_window.geometry("300x100")
    vitoria_window.configure(background=co4)
    Label(vitoria_window, text="Você Venceu!", font=('Comic Sans MS', 20, 'bold'), bg=co4, fg=co0).pack(pady=10)  
    Button(vitoria_window, text="Pressione ENTER para reiniciar", font=('Comic Sans MS', 10, 'bold'), bg=co4, fg=co0, command=lambda: reset_game(vitoria_window)).pack(pady=5)
    Button(vitoria_window, text="Pressione ESPAÇO para fechar", font=('Comic Sans MS', 10, 'bold'), bg=co4, fg=co0, command=janela.quit).pack(pady=5)
    vitoria_window.bind('<Return>', lambda event: reset_game(vitoria_window))
    vitoria_window.bind('<space>', lambda event: janela.quit())


if control == ['lampada_1', 'lampada_2', 'lampada_3']:
    vitoria()


lista = [0,1,0,1,0]

# Lampada On
img_1 = Image.open('1.png')
img_1 = img_1.resize((110, 110))
img_1 = ImageTk.PhotoImage(img_1)

# Lampada off
img_0 = Image.open('0.png')
img_0 = img_0.resize((110, 110))
img_0 = ImageTk.PhotoImage(img_0)

l_img_1 = Label(frame_baixo, image=img_0, bg=co4)
l_img_1.place(x=5, y=70)

l_img_2 = Label(frame_baixo, image=img_0, bg=co4)
l_img_2.place(x=105, y=70)

l_img_3 = Label(frame_baixo, image=img_0, bg=co4)
l_img_3.place(x=205, y=70)


b_interruptor_1 = Button(frame_baixo, command=lambda i=[lista,'interruptor - 1']: ligarLampada(i), text='Interruptor - 1', anchor=NW, font=('Ivy', 9, 'bold'), relief=RAISED,
                        overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_1.place(x=300, y=50)


b_interruptor_2 = Button(frame_baixo,command=lambda i=[lista,'interruptor - 2']: ligarLampada(i), text='Interruptor - 2', anchor=NW, font=('Ivy', 9, 'bold'), relief=RAISED,
                        overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_2.place(x=300, y=80)


b_interruptor_3 = Button(frame_baixo, command=lambda i=[lista,'interruptor - 3']: ligarLampada(i), text='Interruptor - 3', anchor=NW, font=('Ivy', 9, 'bold'), relief=RAISED,
                        overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_3.place(x=300, y=110)


b_interruptor_4 = Button(frame_baixo, command=lambda i=[lista,'interruptor - 4']: ligarLampada(i), text='Interruptor - 4', anchor=NW, font=('Ivy', 9, 'bold'), relief=RAISED,
                        overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_4.place(x=300, y=140)


b_interruptor_5 = Button(frame_baixo, command=lambda i=[lista,'interruptor - 5']: ligarLampada(i), text='Interruptor - 5', anchor=NW, font=('Ivy', 9, 'bold'), relief=RAISED,
                        overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_5.place(x=300, y=170)

janela.mainloop()
