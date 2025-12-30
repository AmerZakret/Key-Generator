import matplotlib.pyplot as plt
import numpy as np
import collections
from collatz import collatz_dizisi, goreceli_kaotik_pencere, anahtar_uret


def hesapla_entropi(data):
    """
    Verilen veri dizisinin Shannon entropisini hesaplar.
    Maksimum entropi 8.0'dir (256 farklı değer için).
    """
    if not data:
        return 0
    counts = collections.Counter(data)
    probs = [c / len(data) for c in counts.values()]
    return -sum(p * np.log2(p) for p in probs)


def analiz_et(ornek_sayisi=1000):
    """
    Collatz tabanlı anahtar üretecinin istatistiksel analizini yapar.
    Birden fazla başlangıç değeriyle anahtar üretir ve:
    - Bayt dağılımı histogramı
    - Ardışık bayt korelasyon grafiği
    - Entropi değeri
    hesaplar.
    """
    tum_baytlar = []
    uzunluklar = []
    
    # Rastgele başlangıç noktalarından örnekler topla
    start_seed = 12345
    print(f"{ornek_sayisi} örnek için analiz yapılıyor...")
    
    for i in range(ornek_sayisi):
        n = start_seed + i
        dizi = collatz_dizisi(n)
        pencere = goreceli_kaotik_pencere(dizi)
        anahtar = anahtar_uret(pencere)
        
        if anahtar:  # Boş değilse
            tum_baytlar.extend(anahtar)
            uzunluklar.append(len(anahtar))

    # 1. Histogram Analizi (Dağılım Eşit mi?)
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.hist(tum_baytlar, bins=256, range=(0, 256), color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Bayt Dağılımı (0-255)")
    plt.xlabel("Bayt Değeri")
    plt.ylabel("Frekans")
    plt.grid(True, alpha=0.3)
    
    # 2. Scatter Plot (Korelasyon Var mı?)
    # x ekseni: i. bayt, y ekseni: (i+1). bayt
    x = tum_baytlar[:-1]
    y = tum_baytlar[1:]
    
    plt.subplot(1, 2, 2)
    plt.scatter(x, y, s=1, alpha=0.5, color='red')
    plt.title("Ardışık Bayt Korelasyonu (x[i] vs x[i+1])")
    plt.xlabel("Bayt[i]")
    plt.ylabel("Bayt[i+1]")
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    entropi = hesapla_entropi(tum_baytlar)
    print(f"\n=== ANALİZ SONUÇLARI ===")
    print(f"Toplam örnek sayısı: {ornek_sayisi}")
    print(f"Toplam üretilen bayt: {len(tum_baytlar)}")
    print(f"Ortalama anahtar uzunluğu: {np.mean(uzunluklar):.2f}")
    print(f"Entropi: {entropi:.4f} / 8.0000 (Max)")
    print(f"Entropi yüzdesi: {(entropi / 8.0) * 100:.2f}%")
    
    # Tekil değer sayısı
    tekil_degerler = len(set(tum_baytlar))
    print(f"Kullanılan farklı bayt değeri: {tekil_degerler} / 256")


if __name__ == "__main__":
    print("=== COLLATZ ANAHTAR ANALİZ ARACI ===\n")
    
    ornek = input("Kaç örnek analiz edilsin? (varsayılan: 1000): ").strip()
    ornek_sayisi = int(ornek) if ornek else 1000
    
    analiz_et(ornek_sayisi)
