# Fibonacci Sayılarını Farklı Yöntemlerle Hesaplama

Bu notebook, Fibonacci dizisini farklı yöntemlerle hesaplamayı ve bu yöntemlerin performansını incelemeyi amaçlar.

## Yöntemlerin Açıklaması

### 1. Özyinelemeli (Recursive) Yöntem

**Açıklama:**

Özyinelemeli yöntemde, Fibonacci sayıları doğrudan tanımına uygun olarak hesaplanır. Fonksiyon, kendisini `n-1` ve `n-2` değerleri için tekrar çağırır ve temel durumlara (`n = 0` veya `n = 1`) ulaştığında geri döner.

```python
def fib_recursive(n):
    """
    Fibonacci sayısını özyinelemeli olarak hesaplar.

    Parametre:
    n (int): Fibonacci dizisinde hesaplanacak terimin indeksi.

    Döndürür:
    int: n'inci Fibonacci sayısı.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
```

**Nasıl Çalışır:**

- **Temel Durumlar:** `n == 0` için `0`, `n == 1` için `1` döndürür.
- **Özyineleme:** `n > 1` durumunda, fonksiyon kendisini `n - 1` ve `n - 2` için çağırır.
- **Çağrı Yığını:** Her fonksiyon çağrısı, kendi alt çağrılarının tamamlanmasını bekler ve bu da çağrı yığınının derinleşmesine neden olur.

**Avantajları:**

- Basit ve anlaşılır bir yapıya sahiptir.
- Matematiksel tanıma doğrudan uyar.

**Dezavantajları:**

- Verimsizdir; zaman karmaşıklığı \( O(2^n) \)'dir.
- Aynı alt problemler defalarca hesaplanır.
- Büyük `n` değerleri için `RecursionError` oluşabilir.

### 2. Memoization (Belleğe Alma) Yöntemi

**Açıklama:**

Memoization, özyinelemeli fonksiyondaki tekrar hesaplamaları önlemek için hesaplanan sonuçları bir sözlükte saklar. Böylece, aynı fonksiyon tekrar çağrıldığında, hesaplanmış değer doğrudan geri döndürülür.

```python
memo = {}

def fib_memoization(n):
    """
    Fibonacci sayısını memoization yöntemiyle hesaplar.

    Parametre:
    n (int): Fibonacci dizisinde hesaplanacak terimin indeksi.

    Döndürür:
    int: n'inci Fibonacci sayısı.
    """
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fib_memoization(n - 1) + fib_memoization(n - 2)
    return memo[n]
```

**Nasıl Çalışır:**

- **Kontrol:** Fonksiyon çağrıldığında, `n` değerinin `memo` sözlüğünde olup olmadığı kontrol edilir.
- **Belleğe Alma:** Eğer `n` daha önce hesaplanmışsa, `memo[n]` değeri döndürülür.
- **Hesaplama:** Eğer hesaplanmamışsa, fonksiyon özyinelemeli olarak devam eder ve sonucu `memo` sözlüğüne kaydeder.
- **Temel Durumlar:** `n == 0` ve `n == 1` için değerler doğrudan atanır.

**Avantajları:**

- **Verimlilik:** Zaman karmaşıklığı \( O(n) \)'ye düşer.
- **Tekrarlı Hesaplamaları Önler:** Her alt problem yalnızca bir kez hesaplanır.

**Dezavantajları:**

- **Bellek Kullanımı:** Hesaplanan tüm değerler saklandığı için bellek kullanımı artar.
- **Karmaşıklık:** Kod biraz daha karmaşık hale gelir.

### 3. Tabulation (Tablo Oluşturma) Yöntemi

**Açıklama:**

Tabulation yöntemi, dinamik programlamanın ileriye doğru (bottom-up) yaklaşımıdır. Küçük alt problemlerin çözümleri tabloya kaydedilir ve daha büyük problemlerin çözümünde kullanılır.

```python
def fib_tabulation(n):
    """
    Fibonacci sayısını tabulation yöntemiyle hesaplar.

    Parametre:
    n (int): Fibonacci dizisinde hesaplanacak terimin indeksi.

    Döndürür:
    int: n'inci Fibonacci sayısı.
    """
    if n == 0:
        return 0
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]
```

**Nasıl Çalışır:**

- **Tablo Oluşturma:** `fib_table` adlı bir liste oluşturulur ve indeksleri Fibonacci sayılarını temsil eder.
- **Başlangıç Değerleri:** `fib_table[0]` ve `fib_table[1]` atanır.
- **Döngü:** `i` değeri 2'den `n`'e kadar artar ve her adımda `fib_table[i]` değeri hesaplanır.
- **Sonuç:** İstenen Fibonacci sayısı `fib_table[n]` olarak döndürülür.

**Avantajları:**

- **Verimlilik:** Zaman karmaşıklığı \( O(n) \)'dir.
- **Özyineleme Yok:** Stack overflow riski yoktur.
- **Anlaşılır Kod:** Takip edilmesi kolaydır.

**Dezavantajları:**

- **Bellek Kullanımı:** `fib_table` listesi için \( O(n) \) bellek kullanılır.
- **Gereksiz Veri Saklama:** Sadece son iki değere ihtiyaç varken tüm diziyi saklamak bellek israfına neden olabilir.

### 4. Optimize Edilmiş Yöntem

**Açıklama:**

Bu yöntemde, sadece önceki iki Fibonacci sayısını tutarak bellek kullanımı optimize edilir.

```python
def fib_optimized(n):
    """
    Fibonacci sayısını optimize edilmiş bir şekilde hesaplar.

    Parametre:
    n (int): Fibonacci dizisinde hesaplanacak terimin indeksi.

    Döndürür:
    int: n'inci Fibonacci sayısı.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

**Nasıl Çalışır:**

- **Başlangıç Değerleri:** `a = 0`, `b = 1` olarak atanır.
- **Döngü:** `n` değerine kadar döngü çalışır ve her adımda:
  - `a`, `b`'nin önceki değerini alır.
  - `b`, `a + b` toplamını alır.
- **Sonuç:** Son `b` değeri istenen Fibonacci sayısıdır.

**Avantajları:**

- **Bellek Verimliliği:** Sadece iki değişken kullanılır.
- **Hızlı ve Verimli:** Zaman karmaşıklığı \( O(n) \)'dir ve bellek kullanımı düşüktür.
- **Basitlik:** Kod sade ve anlaşılırdır.

**Dezavantajları:**

- **Sınırlamalar:** Çok büyük `n` değerleri için sayısal sınırlar aşılabilir.
- **Kayan Nokta Hatası:** Çok büyük sayılar için hassasiyet kaybı olabilir.

## Yöntemlerin Karşılaştırılması

| Yöntem           | Zaman Karmaşıklığı | Bellek Karmaşıklığı | Avantajları                         | Dezavantajları                     |
| ---------------- | ------------------ | ------------------- | ----------------------------------- | ---------------------------------- |
| Özyinelemeli     | \( O(2^n) \)       | \( O(n) \)          | Basit ve anlaşılır                  | Verimsiz, stack overflow riski     |
| Memoization      | \( O(n) \)         | \( O(n) \)          | Hızlı, tekrarlı hesaplamaları önler | Bellek kullanımı artar             |
| Tabulation       | \( O(n) \)         | \( O(n) \)          | Hızlı, özyineleme yok               | Bellek kullanımı yüksek            |
| Optimize Edilmiş | \( O(n) \)         | \( O(1) \)          | Hızlı ve bellek verimli             | Sayısal limitler, hassasiyet kaybı |

## Notlar

- Kodları çalıştırırken büyük `n` değerleri için dikkatli olunuz; bazı yöntemler bellek veya maksimum özyineleme sınırlarına takılabilir.
- Kodları geliştirip farklı senaryoları test etmek için değişiklikler yapabilirsiniz.
- Python'un özyineleme sınırı nedeniyle `fib_recursive` fonksiyonu büyük `n` değerleri için `RecursionError` verebilir.

```python
# Fonksiyonların Test Edilmesi

def test_functions():
    print("fib_recursive fonksiyonunun testi (n = 10):")
    print(f"fib_recursive(10) = {fib_recursive(10)}")

    print("\nfib_memoization fonksiyonunun testi (n = 500):")
    n = 500
    result = fib_memoization(n)
    print(f"fib_memoization({n}) = {result}")

    print("\nfib_tabulation fonksiyonunun testi (n = 10000):")
    n = 10000
    result = fib_tabulation(n)
    print(f"fib_tabulation({n}) hesaplandı.")

    print("\nfib_optimized fonksiyonunun testi (n = 100000):")
    n = 100000
    result = fib_optimized(n)
    print(f"fib_optimized({n}) hesaplandı.")

# Test fonksiyonunu çalıştırmak için aşağıdaki satırın yorumunu kaldırabilirsiniz
# test_functions()
```

**Not:** Grafik çizimi için `matplotlib` kütüphanesinin yüklü olması gerekmektedir. Eğer yüklü değilse, aşağıdaki komutu kullanarak yükleyebilirsiniz:

```bash
pip install matplotlib
```
