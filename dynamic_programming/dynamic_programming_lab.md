# Laboratuvar Çalışması: Fibonacci Dizisini Dinamik Programlama ile Çözme

## Amaç

Bu laboratuvar çalışmasının amacı, Fibonacci dizisini dinamik programlama yaklaşımıyla hesaplamayı öğrenmek ve bu yöntemle algoritmanın verimliliğini artırmaktır. Öğrenciler, Fibonacci dizisinin geleneksel özyinelemeli (recursive) yöntemle hesaplanmasının neden verimsiz olduğunu anlayacak ve dinamik programlama tekniklerini uygulayarak daha etkili bir çözüm geliştireceklerdir.

## Ön Bilgiler

Fibonacci dizisi, her sayının kendisinden önce gelen iki sayının toplamı olduğu bir sayı dizisidir. Dizinin ilk iki elemanı genellikle 0 ve 1 olarak tanımlanır.

Matematiksel olarak:

- **Temel Durumlar:**
  - \( F(0) = 0 \)
  - \( F(1) = 1 \)
- **Özyinelemeli İfade:**
  - \( F(n) = F(n-1) + F(n-2) \) (n ≥ 2)

**Örnek:**

| n    | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F(n) | 0   | 1   | 1   | 2   | 3   | 5   | 8   | 13  | 21  | 34  | 55  |

## Görevler

### Görev 1: Geleneksel Özyinelemeli Yaklaşımı İnceleme

1. **Özyinelemeli Fonksiyonu Yazın:**

   - Fibonacci sayısını özyinelemeli bir fonksiyon kullanarak hesaplayan basit bir fonksiyon yazın.
   - Bu fonksiyon, temel durumlar için sabit değerler döndürmeli ve diğer durumlar için kendini çağırmalıdır.

2. **Fonksiyonu Test Edin:**

   - Küçük `n` değerleri için fonksiyonu test edin ve doğru sonuçlar aldığınızdan emin olun.
   - Örneğin, `n = 5`, `n = 10` değerleri için fonksiyonu çalıştırın.

3. **Verimliliği Değerlendirin:**

   - `n = 35` ve `n = 40` gibi daha büyük değerler için fonksiyonu çalıştırmayı deneyin.
   - Fonksiyonun çalışma süresini ölçün ve büyük `n` değerleri için neden verimsiz olduğunu tartışın.

### Görev 2: Dinamik Programlama ile İyileştirme

1. **Sorunu Tanımlayın:**

   - Özyinelemeli yöntemde aynı alt problemlerin defalarca hesaplandığını fark edin.
   - Bu tekrarlı hesaplamaların nasıl önlenebileceğini düşünün.

2. **Memoization (Belleğe Alma) Yöntemini Uygulayın:**

   - Hesaplanan Fibonacci sayılarının saklanması için bir veri yapısı kullanın (örneğin, bir sözlük veya liste).
   - Fonksiyonunuzu, hesaplanan değerleri bu veri yapısında saklayacak şekilde yeniden yazın.
   - Eğer bir Fibonacci sayısı daha önce hesaplandıysa, doğrudan saklanan değeri kullanın.

3. **Fonksiyonu Test Edin:**

   - `n = 40`, `n = 100`, ve `n = 500` gibi büyük değerler için fonksiyonu çalıştırın.
   - Çalışma süresindeki iyileşmeyi gözlemleyin.

4. **Analiz Edin:**

   - Memoization yönteminin nasıl verimliliği artırdığını açıklayın.
   - Bellek kullanımı hakkında düşüncelerinizi belirtin.

### Görev 3: Tabulation (Tablo Oluşturma) Yöntemini Uygulayın

1. **İleriye Doğru Dinamik Programlama:**

   - Fibonacci sayıları için bir tablo (liste) oluşturun ve ilk iki değeri tanımlayın.
   - Döngü kullanarak Fibonacci sayılarının değerlerini hesaplayın ve tabloya kaydedin.
   - Bu yöntemle, her Fibonacci sayısı sadece bir kez hesaplanır.

2. **Fonksiyonu Test Edin:**

   - `n = 1000`, `n = 10000` gibi daha büyük değerler için fonksiyonu çalıştırın.
   - Çalışma süresini ve bellek kullanımını gözlemleyin.

3. **Bellek Optimizasyonu:**

   - Yalnızca önceki iki değerin gerekli olduğunu fark edin.
   - Bellek kullanımını azaltmak için tablo yerine değişkenler kullanarak fonksiyonunuzu yeniden yazın.

4. **Sonuçları Karşılaştırın:**

   - Farklı yöntemlerin performansını karşılaştırın.
   - Hangi yöntemin hangi durumlarda daha uygun olduğunu tartışın.

### Görev 4: Sonuçların Görselleştirilmesi

1. **Grafik Çizimi:**

   - Farklı `n` değerleri için her yöntemin çalışma süresini ölçün.
   - Çalışma sürelerini grafik üzerinde gösterin (örneğin, matplotlib veya başka bir kütüphane kullanarak).

2. **Analiz:**

   - Grafik üzerinde yöntemlerin performans farklarını yorumlayın.
   - Özellikle büyük `n` değerleri için hangi yöntemlerin uygun olduğunu belirtin.

## Teslim Edilecekler

- Yazdığınız tüm kodlar (Python dosyaları veya Jupyter Notebook).
- Çalışma sürelerinin ve bellek kullanımının karşılaştırıldığı bir rapor.
- Sonuçların analiz edildiği ve hangi yöntemlerin hangi durumlarda tercih edilmesi gerektiğinin tartışıldığı bir değerlendirme.

## Ek Notlar

- Kodlarınızı temiz ve anlaşılır bir şekilde yazmaya özen gösterin.
- Yorum satırları ekleyerek kodunuzun ne yaptığını açıklayın.
- Herhangi bir kaynak kullanırsanız, referans vermeyi unutmayın.

## Değerlendirme Kriterleri

- **Doğruluk:** Fonksiyonların doğru sonuçlar üretmesi.
- **Verimlilik:** Kodların verimli çalışması ve optimize edilmiş olması.
- **Anlaşılabilirlik:** Kodun ve raporun açık ve anlaşılır olması.
- **Analiz ve Yorumlama:** Sonuçların doğru bir şekilde analiz edilmesi ve yorumlanması.

## Sonuç

Bu laboratuvar çalışması ile dinamik programlamanın temel prensiplerini uygulayarak, verimliliği artırmanın ve algoritmalarınızı optimize etmenin önemini kavrayacaksınız. Ayrıca, farklı yöntemlerin avantajlarını ve dezavantajlarını karşılaştırarak hangi durumlarda hangi yaklaşımların daha uygun olduğunu anlayacaksınız.

İyi çalışmalar!
