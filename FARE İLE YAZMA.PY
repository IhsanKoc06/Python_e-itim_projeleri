from turtle import*
pensize(3)
win=Screen()
win.setup(900,900)

def nokta (x,y):
     goto (x,y)
win.onclick(nokta) # TIKLAMA OLDUGUNDA 
mainloop() 

from turtle import*
shape('turtle')
pensize(4)
w=Screen()
w.setup(500,500)

def soladön():
    left(90)
    write('sola döndün')
def sağadön():
    right(90)
    write(' sağa döndün')
def ileri():
    forward(10)
def geri():
    backward(10)
w.onkeypress(soladön,('Left'))
w.onkeypress(sağadön,('Right'))
w.onkeypress(ileri,('Up'))
w.onkeypress(geri,('Down'))
w.listen()