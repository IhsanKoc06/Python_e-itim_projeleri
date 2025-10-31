kelime=input('Kelime Giriniz:')
print (kelime,'nin tersi',kelime[::-1],'dir')
if kelime==kelime[::-1]:
    print(kelime,'Palidromdur')
else:
    print(kelime,'Palindrom Değildir Palindrom Olması Gerek')
    