def selamlama(isminiz=''): #DEF KOMUTU FONKSİYON YAPMAK İÇİN
    print('Hoşgeldniz',isminiz)
while True: # SONSUZ DÖNGÜ İÇİN 
        Ad=input('isminiz nedir')
        if (Ad=='dur'): #BURDA PRGRAMI NEREDE BIRAKMAKASINI DURMASINI İSTİYORSAK ORDA DURMASI İÇİN KOMUTU GİRİŞ BULUNUDU
              break
        selamlama(Ad)

