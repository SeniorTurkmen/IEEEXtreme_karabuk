# Proje Dökümanı: Komşuluk Matrisi ile Graf Traversal

## Proje: Komşu Düğümleri Bulma

### 1. Proje Amacı

Bu projede öğrenciler, komşuluk matrisi kullanarak bir graf üzerindeki düğümlerin birbirine nasıl bağlı olduğunu ve hangi düğümlerin komşu olduğunu öğrenirler. Amaç, BFS ve DFS algoritmalarını kullanarak komşu düğümleri bulmayı ve bu algoritmaların temel çalışma mantığını kavramaktır.

### 2. Komşuluk Matrisi Nedir?

Komşuluk matrisi, bir graf'taki düğümlerin birbirleriyle olan bağlantılarını gösteren bir 2D matristir. Eğer `matris[i][j]` değeri `1` ise, `i` ve `j` düğümleri arasında bir kenar (bağlantı) vardır. `0` değeri ise bağlantının olmadığını belirtir.

Örneğin, aşağıdaki matris:

0, 1, 1, 0, 0, 1, 0  
1, 0, 0, 1, 1, 0, 0  
0, 1, 1, 1, 0, 1, 0  
0, 1, 0, 0, 1, 0, 0  
1, 0, 1, 1, 0, 1, 0  
0, 1, 0, 1, 0, 0, 1  
1, 0, 1, 0, 1, 0, 0

Bu matris 7 düğümlü bir grafı ifade eder ve öğrenciler bu matristen hareketle komşu düğümleri bulmayı öğrenecekler.

### 3. Uygulama Adımları

1. **Matrisin Tanımlanması:**

   - Öğrenciler yukarıdaki gibi bir komşuluk matrisi tanımlar.
   - Düğümler `0`, `1`, `2`, `3`, `4`, `5`, `6` olarak isimlendirilir.

2. **Komşu Düğümleri Bulma (BFS ve DFS):**
   - Öğrenciler BFS ve DFS algoritmalarını yazarak belirli bir düğümden başlayarak hangi düğümlerin komşu olduğunu bulurlar.
   - **BFS:** Genişlik öncelikli arama ile sırayla komşu düğümleri ziyaret ederek bağlantıları keşfetmek.
   - **DFS:** Derinlik öncelikli arama ile bir düğümden başlayarak derinlemesine keşif yaparak bağlantıları bulmak.

### 5. Beklenen Çıktı

BFS ile dolaşım: 0 1 2 5 3 4 6
DFS ile dolaşım: 0 1 3 4 2 5 6

### 6. Derleme ve Çalıştırma

#### 1. C Kodunu Kaydedin

Kodu bir .c dosyasına kaydedin, örneğin graph_search.c.

#### 2. Derleyin

gcc graph_search.c -o graph_search

#### 3. Çalıştırın

./graph_search

### 7. Sonuç

Bu proje ile öğrenciler, komşuluk matrislerini kullanarak düğümler arasındaki bağlantıları kolayca keşfetmeyi öğrenirler. Ayrıca BFS ve DFS algoritmalarının temel çalışma prensiplerini basit bir örnekle anlama fırsatı bulurlar.
