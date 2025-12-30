# Collatz Tabanlı Anahtar Üretim Algoritması

## 1. Amaç
Bu çalışmada, Collatz varsayımının deterministik fakat kaotik davranış
özelliklerinden faydalanarak özgün bir anahtar üretim mekanizması
tasarlanmıştır.

Amaç:
- Tek/çift (0–1) temelli basit anahtar üretimlerinden kaçınmak
- Collatz dizisinin **yerel düzensizliğini** kullanmak
- Deterministik 8–4–2–1 son davranışını yapay kurallar eklemeden dışarıda bırakmak

---

## 2. Collatz Dizisi
Bir başlangıç değeri \( n_0 \) için Collatz dizisi şu şekilde tanımlanır:

- \( n \) çift ise: \( n_{k+1} = n_k / 2 \)
- \( n \) tek ise: \( n_{k+1} = 3n_k + 1 \)

Dizi her zaman 1 değerine ulaşır.

Örnek:
40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1



---

## 3. Kaotik Pencere Seçimi

### 3.1 Temel Problem
Collatz dizisinin son kısmı:
8 → 4 → 2 → 1


tamamen deterministik ve monoton azalan bir yapıdadır.
Bu bölüm kriptografik anlamda yeni bilgi taşımaz.

Bu nedenle anahtar üretiminde kullanılmaması gerekir.

---

### 3.2 Çözüm: Monoton Azalan Kuyruğun Otomatik Kesilmesi

Bu algoritmada **özel bir sayı, eşik veya yasak küme tanımlanmaz**.

Uygulanan tek kural:

> Collatz dizisinin sonundaki tamamen monoton azalan kuyruk otomatik olarak dışlanır.

Bu kural sayesinde:
- 4, 2 ve 1 doğal olarak dışarıda kalır
- 8 de **aynı mekanizma ile** pencereye girmez
- Hiçbir sayıya özel muamele yapılmaz

Örnek:
Girdi dizisi:
[40, 20, 10, 5, 16, 8, 4, 2, 1]

Monoton azalan kuyruk:
8 > 4 > 2 > 1

Kaotik pencere:
[40, 20, 10, 5, 16]



---

## 4. Anahtar Üretimi

Kaotik pencere içindeki her eleman için,
önceki ve sonraki komşular da kullanılarak
doğrusal olmayan bir karışım fonksiyonu uygulanır:

\[
k_i = (7 \cdot n_{i-1} + n_i^2 + 13 \cdot n_{i+1}) \bmod 256
\]

Bu yaklaşım:
- Yerel bağlam bilgisini kullanır
- Lineer bağıntılardan kaçınır
- Tek bir Collatz değerinden anahtar tahminini zorlaştırır

Anahtar elemanları 0–255 aralığında bayt değerleridir.

---

## 5. İstatistiksel Gözlemler

Yapılan deneysel gözlemler:

- Farklı başlangıç değerleri için pencere uzunluğu değişkendir
- Kaotik pencere uzunluğu, başlangıç değerinin davranışına bağlıdır
- Küçük başlangıç değerlerinde pencere kısa olabilir
- Büyük ve kaotik başlangıçlarda anahtar dizisi daha düzensizdir

Örnek karşılaştırma:

| Başlangıç | Pencere Uzunluğu |
|---------|------------------|
| 40      | Kısa             |
| 27      | Uzun             |
| 97      | Daha uzun        |

Bu, algoritmanın deterministik ama **yüksek varyanslı** olduğunu gösterir.

---
