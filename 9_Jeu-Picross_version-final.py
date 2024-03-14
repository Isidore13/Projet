
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("Jeu Picross")

#-------------------------------------------------------------------
photo = PhotoImage(file="logo_PI-Games.png")

info_case = {}

#-------------------------------------------------------------------
def Grille(tab,x,y):
    taille_case=40
    canvas = Canvas(tab, width=x*taille_case+2, height=y*taille_case+2, background='white')

    canvas.create_rectangle (562, 2, 2, 562)

    t=0
    while t<400:
        ligne_v = canvas.create_line(162+t, 0, 162+t, y*taille_case+2)
        ligne_h = canvas.create_line(0, 162+t, x*taille_case+2, 162+t)
        t+=40
    canvas.pack()


    canvas.create_image(7, 7, anchor=NW, image=photo)
    canvas.pack()

    separationV = canvas.create_line(363, 0, 363, 562)
    separationH = canvas.create_line(0, 361, 562, 361)


    canvas.create_text(181, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(181, 116, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(223, 143, text= "3",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(223, 116, text= "4",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(261, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(261, 116, text= "3",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(261, 89, text= "2",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(302, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(302, 116, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(302, 89, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(342, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(342, 116, text= "2",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(342, 89, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(383, 143, text= "2",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(383, 116, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(383, 89, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(421, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(421, 116, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(421, 89, text= "2",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(461, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(461, 116, text= "5",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(502, 143, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(502, 116, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(541, 143, text= "4",fill="black",font=('Helvetica 17 bold'))


    canvas.create_text(142, 183, text= "5",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 223, text= "2",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 223, text= "2",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 262, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 262, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(92, 262, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 303, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 303, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(92, 303, text= "2",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 343, text= "2",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 343, text= "4",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 383, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 383, text= "2",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(92, 383, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 422, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 422, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(92, 422, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 462, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 462, text= "2",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 502, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(117, 502, text= "1",fill="black",font=('Helvetica 17 bold'))
    canvas.create_text(92, 502, text= "1",fill="black",font=('Helvetica 17 bold'))

    canvas.create_text(142, 543, text= "7",fill="black",font=('Helvetica 17 bold'))


    casesJoueur = [[0]*10 for i in range(10)]


    def clic_Button1(event):
        r = taille_case // 2
        cJx = (event.x // taille_case) - 4
        cJy = (event.y // taille_case) - 4

        casesJoueur[cJx][cJy] = 1
        #print(casesJoueur)
        X = 40.2*(cJx + 4) + r
        Y = 40.2*(cJy + 4) + r

        if X < 162 or Y < 162:
            clic_Button1 = False
        else:
            key =  str(X) + ',' + str(Y)
            if key not in info_case :
                canvas.create_rectangle(X-r, Y-r, X+r, Y+r, fill='black')
                info_case[key]="Black"
            elif info_case[key] == "X" :
                canvas.create_rectangle(X-r, Y-r, X+r, Y+r, fill='black')
                info_case[key]="Black"
        #print (info_case [key])

    canvas.bind('<Button-1>', clic_Button1)
    canvas.pack()


    def clic_Button3(event):
        r = taille_case // 2
        cJx = (event.x // taille_case) - 4
        cJy = (event.y // taille_case) - 4

        casesJoueur[cJx][cJy] = 3
        #print(casesJoueur)
        X = 40.2*(cJx + 4) + r
        Y = 40.2*(cJy + 4) + r

        if X < 162 or Y < 162:
            clic_Button3 = False
        else:
            key =  str(X) + ',' + str(Y)
            if key not in info_case :
                canvas.create_text(X, Y, text= "X", fill="orange", font=('Helvetica 17 bold'))
                info_case[key]="X"
            elif info_case[key] == "Black" :
                canvas.create_rectangle(X-r, Y-r, X+r, Y+r, fill = 'white')
                canvas.create_text(X, Y, text= "X", fill="orange", font=('Helvetica 17 bold'))
                info_case[key]="X"
        #print (info_case[key])

    canvas.bind('<Button-3>', clic_Button3)
    canvas.pack()


    def fin():
        if casesJoueur == [[3, 3, 3, 3, 1, 3, 3, 1, 3, 3],[3, 1, 1, 1, 1, 3, 1, 1, 1, 3],[1, 1, 3, 1, 1, 1, 3, 3, 3, 1],
        [1, 3, 3, 3, 1, 3, 3, 3, 3, 1], [1, 3, 1, 1, 3, 3, 3, 3, 3, 1], [1, 3, 3, 3, 3, 3, 1, 3, 1, 1], [1, 1, 3, 3, 3, 1, 3, 3, 3, 1],
        [3, 1, 1, 1, 1, 1, 3, 3, 3, 1], [3, 3, 3, 3, 1, 3, 3, 3, 3, 1], [3, 3, 3, 3, 3, 1, 1, 1, 1, 3]]:
            showinfo("Wou win", "Bravo, vous avez réussi !!")
        else:
            showerror("Nope", "Ce n'est pas ça, essaie encore!")

    Button(text="Valider", command=fin).pack()


Grille(fenetre,14,14)

#-------------------------------------------------------------------
fenetre.mainloop()


