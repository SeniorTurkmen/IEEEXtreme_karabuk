# A\* Algoritması

## 1. A\* Algoritması Nedir?

**A\* Algoritması**, bir grafikte belirli bir başlangıç düğümünden bir hedef düğüme olan en kısa ve en uygun yolu bulmak için kullanılan bir yol bulma algoritmasıdır. A\* algoritması, Dijkstra algoritmasının ve Greedy Best-First Search algoritmasının kombinasyonu olarak düşünülebilir ve bu nedenle genellikle daha verimli bir yol bulur.

### Uygulama Alanları

- Haritalar üzerinde rota bulma ve navigasyon
- Oyunlar ve yapay zeka
- Robotik ve otomasyon
- Ağlarda veri yönlendirme

## 2. Algoritmanın Genel Mantığı

A\* algoritması, her düğümü değerlendirirken iki faktöre bakar:

1. **G(x):** Başlangıç düğümünden mevcut düğüme kadar olan gerçek maliyet.
2. **H(x):** Mevcut düğümden hedef düğüme olan tahmini maliyet (heuristic - sezgisel).

### Formül

- **F(x) = G(x) + H(x)**
- `F(x)` toplam maliyettir ve algoritma bu değeri en düşük olan düğümü seçerek çalışır.

### Adım Adım Çalışma Prensibi

1. **Açık ve Kapalı Listeler:** Açık liste, değerlendirilmesi gereken düğümleri içerir. Kapalı liste ise zaten değerlendirilen düğümleri içerir.
2. **Başlangıç Düğümünü Ekleme:** Başlangıç düğümünü açık listeye ekleyin ve `G(x) = 0`, `H(x)` değerini hesaplayın.
3. **En Düşük `F(x)` Değeri Olan Düğümü Seçme:** Açık listeden `F(x)` değeri en düşük olan düğümü seçin.
4. **Komşu Düğümleri Değerlendirme:** Seçilen düğümün komşularını değerlendirin ve `G(x)`, `H(x)`, `F(x)` değerlerini güncelleyin. Komşulara ulaşmanın daha kısa bir yolu varsa, o düğümü güncelleyin.
5. **Düğümleri Açık ve Kapalı Listeye Ekleme:** Seçilen düğümü kapalı listeye ekleyin. Komşuları açık listeye ekleyin veya mevcutsa `F(x)` değerini güncelleyin.
6. **Hedef Düğüme Ulaşana Kadar Devam Et:** Hedef düğüme ulaşıldığında yol tamamlanır.

### Heuristik (Sezgisel) Fonksiyon

- A\* algoritmasının başarısı, kullanılan `H(x)` değerine bağlıdır. `H(x)` değeri, gerçek maliyete yakın bir tahmin olmalıdır. Örneğin, harita üzerinde bir hedefe olan düz çizgi mesafesi, uygun bir sezgisel olabilir.

## 3. Algoritmanın Zaman ve Uzay Karmaşıklığı

- **Zaman Karmaşıklığı:** `O(E)`, burada `E` kenar sayısıdır. Sezgisel fonksiyonun doğruluğuna bağlı olarak değişir.
- **Uzay Karmaşıklığı:** `O(V)`, burada `V` düğüm sayısıdır. Açık ve kapalı listelerin boyutuna bağlıdır.

## 4. Python ile A\* Algoritması

### Python Uygulaması

Aşağıdaki örnek, A\* algoritmasını bir grid harita üzerinde uygulayan temel bir Python kodunu göstermektedir:

```python
    import heapq

    class Node:
        def __init__(self, position, parent=None):
            self.position = position
            self.parent = parent
            self.g = float('inf')  # Gerçek maliyet (G)
            self.h = float('inf')  # Heuristik maliyet (H)
            self.f = float('inf')  # Toplam maliyet (F)

        def __lt__(self, other):
            return self.f < other.f

    def heuristic(a, b):
        # Manhattan mesafesi (x1 - x2) + (y1 - y2)
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star(graph, start, goal):
        open_list = []
        closed_list = set()
        start_node = Node(start)
        goal_node = Node(goal)

        start_node.g = 0
        start_node.h = heuristic(start, goal)
        start_node.f = start_node.g + start_node.h

        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            closed_list.add(current_node.position)

            if current_node.position == goal_node.position:
                path = []
                while current_node is not None:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]  # Yolu ters çevirin

            # Komşuları bul ve değerlendir
            x, y = current_node.position
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for next_position in neighbors:
                # Eğer geçerli değilse veya kapalı listede ise, atla
                if next_position in closed_list or next_position not in graph:
                    continue

                neighbor = Node(next_position, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor.position, goal_node.position)
                neighbor.f = neighbor.g + neighbor.h

                # Eğer açık listede daha düşük maliyetle varsa, atla
                if any(open_node.position == neighbor.position and open_node.f <= neighbor.f for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

        return None

    # Örnek harita (grid)
    graph = {
        (0, 0): True, (0, 1): True, (0, 2): True,
        (1, 0): True, (1, 1): False, (1, 2): True,
        (2, 0): True, (2, 1): True, (2, 2): True
    }

    start = (0, 0)
    goal = (2, 2)

    print("En kısa yol:", a_star(graph, start, goal))
```

### Çıktı

```bash
    En kısa yol: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
```

### Açıklama

1. Graf Temsili: Grafiği bir grid harita olarak temsil ediyoruz. Geçilebilir (True) ve engelli (False) noktalar var.
2. Manhattan Mesafesi: Heuristik olarak Manhattan mesafesi kullanılıyor. Bu, iki nokta arasındaki dikey ve yatay mesafelerin toplamıdır.
3. Açık ve Kapalı Listeler: A\* algoritması bu listeleri kullanarak düğümleri değerlendirir ve yolu bulur.

## 5. Örnek Senaryo

Bir robot, bir depoda bir noktadan başka bir noktaya gitmek istiyor. Depo, farklı koridorlardan ve engellerden oluşuyor. A*algoritması kullanarak robotun en kısa yolu bulmasını sağlayabiliriz. A* algoritması, robotun hedefe giderken en kısa ve en hızlı yolu bulmasına yardımcı olacaktır.

Graf Görselleştirmesi:

```bash
    S = Start, G = Goal, X = Engel
    S . .
    . X .
    . . G
```

Başlangıç: (0, 0), Hedef: (2, 2)

Algoritma ile bulunacak en kısa yol:

• (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)

## 6. Özet

• Kullanım Alanı: A*algoritması, yönlendirilmiş veya yönlendirilmemiş grafikleri çözebilir ve birçok gerçek dünya uygulamasında kullanılabilir.
• Heuristik Fonksiyon: A* algoritmasının başarısı büyük ölçüde doğru bir sezgisel fonksiyon seçimine bağlıdır.
• Zaman Karmaşıklığı: Sezgisel fonksiyonun doğruluğuna bağlı olarak değişir, ancak genellikle büyük grafiklerde hızlı ve etkilidir.

Bu doküman, A\* algoritmasının temel kavramlarını, çalışma prensibini ve bir örnek uygulamasını kapsamaktadır. Algoritmanın anlaşılması, grafiklerle ilgili diğer problemlerin çözümüne de yardımcı olacaktır.
