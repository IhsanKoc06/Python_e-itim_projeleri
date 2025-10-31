def tek_mi_cift_mi(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"
try:
    girilen_sayi = int(input("Lütfen bir tam sayı girin: "))
    sonuc = tek_mi_cift_mi(girilen_sayi)
    print(f"Girdiğiniz sayı ({girilen_sayi}) bir {sonuc} sayıdır.")

except ValueError:
    # Kullanıcı sayı yerine harf vb. girerse hata mesajı veriyoruz
    print("Hata: Lütfen geçerli bir tam sayı girin.")