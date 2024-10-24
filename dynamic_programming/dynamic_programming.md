# Dinamik Programlama Problemleri

## 1. En Uzun Ortak Alt Dizi (Longest Common Subsequence - LCS)

**Amaç:** İki dizi arasındaki en uzun ortak alt diziyi bulmak.

**Yaklaşım:**

1. **Son Karakterlerden Başlama:**

   - Dizilerin son karakterlerini (`X[i]` ve `Y[j]`) karşılaştırırız.

2. **Geriye Doğru Rekürsif İfade:**

   - Eğer `X[i] == Y[j]` ise:

     ```psuedocode
        dp[i][j] = dp[i+1][j+1] + 1
     ```

   - Aksi halde:

     ```psuedocode
        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
     ```

   - Burada `i` ve `j` değerlerini sondan başa doğru azaltırız.

3. **Temel Durum:**

   - Dizinin sonuna ulaştığımızda (`i = len(X)` veya `j = len(Y)`), `dp[i][j] = 0`

4. **Adım Adım Hesaplama:**

   - Tüm `i` ve `j` değerleri için `dp[i][j]` değerlerini hesaplarız.

5. **Sonuca Ulaşma:**
   - `dp[0][0]` değeri, en uzun ortak alt dizinin uzunluğunu verir.

**Örnek:**

- **Diziler:**

  - `X = "ABCBDAB"`
  - `Y = "BDCAB"`

- **Adımlar:**
  - `i` ve `j` değerlerini sondan (`i = len(X) - 1`, `j = len(Y) - 1`) başlayarak `0`'a doğru azaltırız.
  - Her adımda `dp[i][j]` değerini yukarıdaki formüllere göre hesaplarız.

---

## 2. Para Bozma Problemi (Coin Change Problem)

**Amaç:** Verilen miktarı, en az sayıda bozukluk kullanarak elde etmek.

**Yaklaşım:**

1. **Hedef Miktardan Başlama:**

   - Verilen miktar `amount` olsun.
   - `dp[amount]` değerini bulmak için geriye doğru hareket ederiz.

2. **Geriye Doğru İlerleme:**

   - Kullanılabilecek her bozukluk değeri için:

     ```psuedocode
     dp[x - coin] = min(dp[x - coin], dp[x] + 1)
     ```

     Burada `x` başlangıçta `amount`'tur ve `coin` bozukluk değeridir.

3. **Temel Durum:**

   - `dp[0] = 0` (0 miktarı elde etmek için 0 bozukluk gerekir).

4. **Adım Adım Hesaplama:**

   - `x` değerini `amount`'tan `0`'a doğru azaltarak her adımda `dp[x - coin]` değerlerini güncelleriz.

5. **Sonuca Ulaşma:**
   - En sonunda `dp[0]`'a ulaştığımızda, kullanılan bozukluk sayısını toplamış oluruz.

**Örnek:**

- **Bozukluklar:** `[1, 2, 5]`
- **Miktar:** `11`

- **Adımlar:**
  - `dp[11]`'den başlayarak geriye doğru `dp[0]`'a kadar tüm değerleri hesaplarız.

---

## 3. Matris Zincir Çarpımı (Matrix Chain Multiplication)

**Amaç:** Bir dizi matrisi, toplam çarpım maliyetini en aza indirecek şekilde çarpmak.

**Yaklaşım:**

1. **Son İki Matristen Başlama:**

   - Matris zincirinin son iki matrisi `A_n` ve `A_{n+1}`'i çarparak başlarız.

2. **Geriye Doğru Alt Problemleri Tanımlama:**

   - `dp[i][j]`: Matris `A_i`'den `A_j`'ye kadar olan çarpımın minimum maliyeti.
   - Sondan başlayarak, `dp[i][j]` değerlerini hesaplarız.

3. **Rekürsif İfade:**

   ```psuedocode
   dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j])  for  i ≤ k < j
   ```

   Burada `k` değerini `j-1`'den `i`'ye doğru azaltarak hesaplarız.

4. **Temel Durum:**

   - Tek bir matrisin çarpım maliyeti yoktur:

     ```psuedocode
     dp[i][i] = 0
     ```

5. **Sonuca Ulaşma:**
   - En sonunda `dp[1][n]` değeri, tüm matrislerin çarpımının minimum maliyetini verir.

**Örnek:**

- **Matris Boyutları:** `p = [40, 20, 30, 10, 30]` (4 matris: A1(40x20), A2(20x30), A3(30x10), A4(10x30))

- **Adımlar:**
  - Sondan başlayarak `dp[i][j]` değerlerini hesaplarız.

---

## 4. Evin Boyama Problemi (Paint House Problem)

**Amaç:** Yan yana evleri, aynı renk yan yana gelmeyecek şekilde en düşük maliyetle boyamak.

**Yaklaşım:**

1. **Son Evden Başlama:**

   - Toplam ev sayısı `n` olsun.
   - `n` numaralı evin her bir renk için boyama maliyetini hesaplarız.

2. **Geriye Doğru İlerleme:**

   - `i` numaralı evin (`i = n - 1` to `1`) boyama maliyetini hesaplamak için, bir sonraki evin (`i + 1`) maliyetlerini kullanırız.
   - Her renk için maliyet:

     ```psuedocode
     dp[i][color] = cost[i][color] + min(dp[i + 1][other_colors])
     ```

     Burada `other_colors`, `color` dışındaki renklerdir.

3. **Temel Durum:**

   - Son evin maliyetleri doğrudan `dp[n][color] = cost[n][color]` şeklinde alınır.

4. **Adım Adım Hesaplama:**

   - Her ev için üç renk seçeneği vardır (örneğin: kırmızı, mavi, yeşil).
   - Her adımda, mevcut evin her renk için toplam maliyetini hesaplarız.

5. **Sonuca Ulaşma:**

   - İlk ev için minimum maliyeti bulmak için:

     ```psuedocode
     min_total_cost = min(dp[1][red], dp[1][blue], dp[1][green])
     ```

**Örnek:**

- **Maliyet Matrisi:**

cost = [
[17, 2, 17], # 1. ev
[16, 16, 5], # 2. ev
[14, 3, 19] # 3. ev
]

- **Adımlar:**

1. **Son ev (3. ev):**

   ```psuedocode
   dp[3][red] = cost[3][red] = 14
   dp[3][blue] = cost[3][blue] = 3
   dp[3][green] = cost[3][green] = 19
   ```

2. **2. ev:**

   ```psuedocode
   dp[2][red] = cost[2][red] + min(dp[3][blue], dp[3][green]) = 16 + min(3, 19) = 19
   dp[2][blue] = cost[2][blue] + min(dp[3][red], dp[3][green]) = 16 + min(14, 19) = 30
   dp[2][green] = cost[2][green] + min(dp[3][red], dp[3][blue]) = 5 + min(14, 3) = 8
   ```

3. **1. ev:**

   ```psuedocode
   dp[1][red] = cost[1][red] + min(dp[2][blue], dp[2][green]) = 17 + min(30, 8) = 25
   dp[1][blue] = cost[1][blue] + min(dp[2][red], dp[2][green]) = 2 + min(19, 8) = 10
   dp[1][green] = cost[1][green] + min(dp[2][red], dp[2][blue]) = 17 + min(19, 30) = 36
   ```

- **Sonuç:**
- Minimum toplam maliyet: `min(dp[1][red], dp[1][blue], dp[1][green]) = min(25, 10, 36) = 10`

---

## 5. Çubuk Kesme Problemi (Rod Cutting Problem)

**Amaç:** Belirli bir uzunluktaki çubuğu keserek maksimum kar elde etmek.

**Yaklaşım:**

1. **Son Durumdan Başlama:**

   - Çubuğun toplam uzunluğu `n` olsun. Çözüm, uzunluğu `n` olan çubuk için maksimum karı bulmaktır.
   - Sondan başlayarak, çubuğun son kesimini düşünürüz.

2. **Son Kesimi Belirleme:**

   - Çubuğun son parçasının uzunluğu `i` (1 ≤ `i` ≤ `n`) olabilir.
   - Geriye kalan çubuğun uzunluğu `n - i` olacaktır.

3. **Rekürsif İfade:**

   - Maksimum kar, son parçanın fiyatı ile geriye kalan çubuğun maksimum karının toplamıdır.
   - Matematiksel olarak:

   ```psuedocode
       dp[n] = max(price[i] + dp[n - i])  for 1 ≤ i ≤ n
   ```

4. **Geriye Doğru İlerleme:**

   - `n`'den başlayarak `0`'a doğru tüm alt problemleri çözeriz.
   - Her adımda, farklı `i` değerleri için maksimum karı hesaplarız.

5. **Temel Durum:**

- `dp[0] = 0` (uzunluğu 0 olan çubuğun karı yoktur).

**Örnek:**

- **Fiyat Listesi:** `price = [0, 1, 5, 8, 9]` (indeksler uzunlukları temsil eder).
- **Çubuk Uzunluğu:** `n = 4`.

**Adımlar:**

1. `dp[4]` hesaplamak için:

   dp[4] = max(price[1] + dp[3], price[2] + dp[2], price[3] + dp[1], price[4] + dp[0])

   Yani:

   dp[4] = max(1 + dp[3], 5 + dp[2], 8 + dp[1], 9 + dp[0])

2. Alt problemleri çözerek `dp[3]`, `dp[2]`, `dp[1]` değerlerini buluruz.

3. Bu şekilde geriye doğru ilerleyerek `dp[0]` değerine ulaşırız.

**Sonuç:**

- Maksimum kar `dp[4]` değeri olarak bulunur.
