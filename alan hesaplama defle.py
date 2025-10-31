def alan (u,g):
    A=u*g
    return A
def cevre (u,g):
    C=2*(u+g)
    return C 
u=int(input('UZUN KENARI GİR'))
g=int(input('Kısa Kenarı Gir'))
print('Dikdortgen Alanı=',alan(u,g))
print('Dikdortgen Çevresi=',cevre(u,g))

