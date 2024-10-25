# Dijkstra Algoritması

## 1. Dijkstra Algoritması Nedir?

**Dijkstra Algoritması**, bir grafikte belirli bir başlangıç düğümünden diğer tüm düğümlere olan en kısa yolları bulmak için kullanılan bir algoritmadır. Algoritma, negatif olmayan ağırlıklara sahip yönlendirilmiş veya yönlendirilmemiş grafikler üzerinde çalışır ve en kısa yolu bulmak için **açgözlü bir strateji** kullanır.

### Uygulama Alanları

- Yol bulma ve navigasyon sistemleri
- Ağlarda veri iletimi ve rota bulma
- Haritalama ve lojistik planlama

## 2. Algoritmanın Genel Mantığı

Dijkstra algoritması, bir grafikte bir başlangıç düğümünden diğer düğümlere olan en kısa yolları bulur. Bunu yaparken her düğüme olan en kısa mesafeyi belirler ve bu mesafeleri sürekli güncelleyerek en kısa yol ağacını oluşturur.

### Adım Adım Çalışma Prensibi

1. **Başlangıç Düğümünü Seçin:** Algoritmayı başlatacağınız düğümü seçin ve bu düğüme olan mesafeyi `0` olarak ayarlayın. Diğer tüm düğümlere olan mesafeyi sonsuz (`∞`) olarak başlatın.
2. **Ziyaret Edilmemiş Düğümler Listesi:** Henüz ziyaret edilmemiş düğümleri tutan bir liste oluşturun.
3. **En Kısa Mesafeyi Bulma:** Her adımda, mevcut düğümler arasından en kısa mesafeye sahip olanı seçin ve bu düğümü ziyaret edilmiş olarak işaretleyin.
4. **Mesafeleri Güncelleyin:** Seçilen düğüme komşu olan tüm düğümler için, bu düğüme olan en kısa mesafeyi güncelleyin. Eğer mevcut yol, daha önce bulunan yoldan daha kısa ise mesafeyi ve önceki düğümü güncelleyin.
5. **Diğer Düğümleri Kontrol Edin:** Ziyaret edilmemiş düğümler bitene kadar adımları tekrarlayın.
6. **Sonuç:** Her düğüme olan en kısa yol ve mesafe bulunur.

### Önemli Not

Dijkstra algoritması **negatif ağırlıklı kenarları** olan grafikleri doğru şekilde işleyemez. Bunun nedeni, algoritmanın bir kez işaretlenen en kısa yolun güncellenmeyeceği varsayımıdır. Negatif ağırlıklı kenarlar için farklı algoritmalar (örneğin, Bellman-Ford) kullanılmalıdır.

## 3. Algoritmanın Zaman Karmaşıklığı

Dijkstra algoritmasının zaman karmaşıklığı, kullanılan veri yapılarına bağlı olarak değişir:

- **Priority Queue (Min Heap) ile:** `O((V + E) * log V)`, burada `V` düğüm sayısı ve `E` kenar sayısıdır.
- **Basit Bir Dizi ile:** `O(V^2)`, daha basit ve küçük grafikleri işlerken tercih edilir.

## 4. Python ile Dijkstra Algoritması

### Python Uygulaması

Aşağıdaki örnek, Dijkstra algoritmasını bir yönlendirilmemiş grafikte uygulayan temel bir Python kodunu göstermektedir:

```python
    import heapq

    def dijkstra(graph, start):
        # Her düğüm için en kısa mesafeleri saklayan bir sözlük
        shortest_paths = {vertex: float('infinity') for vertex in graph}
        shortest_paths[start] = 0

        # Öncelik kuyruğu (Min Heap)
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Eğer kuyruktan çıkan mesafe, bilinen en kısa mesafeden daha büyükse, atla
            if current_distance > shortest_paths[current_vertex]:
                continue

            # Komşuları kontrol et ve mesafeleri güncelle
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                # Daha kısa bir yol bulduysak güncelle
                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths

    # Örnek bir grafik
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Başlangıç düğümü 'A'
    start = 'A'
    print("En kısa yollar:", dijkstra(graph, start))
```

### Çıktı

```bash
    En kısa yollar: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

## Açıklama

1. Graf Temsili: Grafiği, her düğümün komşu düğümleri ve kenar ağırlıklarını içeren bir sözlük olarak temsil ederiz.
2. Min Heap: Öncelik kuyruğu olarak kullanılan heapq kütüphanesi ile en kısa yolu her adımda verimli bir şekilde buluruz.
3. En Kısa Yolu Güncelleme: Her komşu düğüm için mesafeleri güncelleyerek, en kısa yolu buluruz.

## 5. Örnek Senaryo

Bir şehir haritası üzerinde düşünelim. Şehirler arası yolların her biri farklı mesafelere sahiptir ve amacımız belirli bir şehirden (örneğin, A şehri) başlayarak diğer tüm şehirlere olan en kısa mesafeyi bulmaktır. Bu durumda Dijkstra algoritması aşağıdaki gibi çalışır:

1. Başlangıç: A şehrinden başlayarak, B şehri ve C şehrine olan mesafeleri kontrol eder.
2. En Kısa Mesafeyi Seç: A’dan B’ye doğrudan gitmek, C’ye gitmekten daha kısa olduğu için B’yi ziyaret eder.
3. Mesafeleri Güncelle: B’den D’ye olan mesafe de bulunur ve kaydedilir.
4. Sonuç: A şehrinden diğer tüm şehirlere olan en kısa yollar bulunur.

## Graf Görselleştirmesi

```bash
     A ----1---- B
     |         / \
     4       2   5
     |     /     |
     C --1------- D
```

Başlangıç A şehri, algoritma ile bulunacak en kısa yollar:

• A -> B: 1
• A -> C: 3 (A -> B -> C)
• A -> D: 4 (A -> B -> D veya A -> C -> D)

## 6. Özet

• Kullanım Alanı: Dijkstra algoritması, yönlendirilmiş veya yönlendirilmemiş grafikleri çözebilir ve gerçek dünya uygulamalarında sıklıkla kullanılır.
• Sınırlamalar: Negatif ağırlıklı kenarları olan grafiklerle doğru çalışmaz. Negatif ağırlıklar varsa Bellman-Ford algoritması kullanılmalıdır.
• Zaman Karmaşıklığı: Kullanılan veri yapılarına bağlı olarak değişir, ancak genellikle büyük grafiklerde bile hızlı ve etkilidir.

Bu doküman, Dijkstra algoritmasının temel kavramlarını, çalışma prensibini ve bir örnek uygulamasını kapsamaktadır. Algoritmanın anlaşılması, grafiklerle ilgili diğer problemlerin çözümüne de yardımcı olacaktır.
