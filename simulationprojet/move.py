def deplacement(img1move,canvas,fenetre):
    canvas.move(img1move,5,0)
    fenetre.after(50,bouger)
bouger()