user=input('Kullanıcı Adı Girin')
password=input('Şifre Girin')
if user=='Admin' and password=='123': #İF EGER DEMEK YANİ BİR KOŞULU SAĞLŞAYACAK DEMEK 
    print('Hoşgeldiniz')
else: # DİGER BUR KOŞULU KULLANAMAK İÇİN  
    print('Ytetksisiz Giriş')
    

şifre='1234'
kullanıcıadı='ihsan'

K_giriş=input('Kullanıcı Adı Giriniz:')
if K_giriş==kullanıcıadı:
    S_şifre=input('Şifre Giriniz')
    if S_şifre==şifre:
        print('Hoşgeldiniz Kullanıcı')
    else:
        print('Şifre Hatalı')
else:
    print('Kullanıcı Adı Yanlış')
    

