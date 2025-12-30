import math

def collatz_dizisi(n):
    """
    Verilen n başlangıç değeri için Collatz dizisini
    doğal haliyle (1'e kadar) üretir.
    """
    dizi = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        dizi.append(n)
    return dizi


def goreceli_kaotik_pencere(dizi):
    """
    Collatz dizisinin sonundaki tamamen monoton azalan
    deterministik kuyruğu otomatik olarak keser.
    """
    if len(dizi) < 2:
        return dizi

    kesme_indeksi = len(dizi) - 1

    # sondan başa doğru git
    for i in range(len(dizi) - 1, 0, -1):
        if dizi[i] < dizi[i - 1]:
            kesme_indeksi = i - 1
        else:
            break

    return dizi[:kesme_indeksi + 1]



def anahtar_uret(pencere, mod=256):
    """
    Collatz dizisinin yerel bağlamını kullanan,
    doğrusal olmayan bir karışım fonksiyonu ile
    bayt tabanlı anahtar üretir.

    k_i = (7*n_{i-1} + n_i^2 + 13*n_{i+1}) mod 256
    """
    anahtar = []
    uzunluk = len(pencere)

    for i in range(uzunluk):
        onceki = pencere[(i - 1) % uzunluk]
        simdiki = pencere[i]
        sonraki = pencere[(i + 1) % uzunluk]

        k = (onceki * 7 + simdiki ** 2 + sonraki * 13) % mod
        anahtar.append(k)

    return anahtar


if __name__ == "__main__":
    baslangic_degeri = int(input("Başlangıç değerini girin: "))

    dizi = collatz_dizisi(baslangic_degeri)
    pencere = goreceli_kaotik_pencere(dizi)
    anahtar = anahtar_uret(pencere)

    print("\nCollatz dizisi:", dizi)
    print("Kaotik pencere:", pencere)
    print("Üretilen anahtar:", anahtar)
    print(f"Anahtar uzunluğu: {len(anahtar)} bayt")

