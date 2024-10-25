# Fibonacci Sayılarını Farklı Yöntemlerle Hesaplama

import time

import matplotlib.pyplot as plt


# 1. Özyinelemeli Yöntem
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

# 2. Memoization (Belleğe Alma) Yöntemi
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

# 3. Tabulation (Tablo Oluşturma) Yöntemi
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
    fib_table[0] = 0
    fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

# 4. Optimize Edilmiş Yöntem
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

# Fonksiyonların Test Edilmesi
def test_functions():
    print("fib_recursive fonksiyonunun testi (n = 0 ila 10):")
    for i in range(11):
        print(f"F({i}) = {fib_recursive(i)}")

    print("\fib_recursive fonksiyonunun testi (n = 10):")
    n = 25
    start_time = time.time()
    result = fib_recursive(n)
    end_time = time.time()
    print(f"F({n}) hesaplandı.")
    print(f"Çalışma Süresi: {end_time - start_time:.4f} saniye")

    print("\nfib_memoization fonksiyonunun testi (n = 500):")
    n = 500
    start_time = time.time()
    result = fib_memoization(n)
    end_time = time.time()
    print(f"F({n}) hesaplandı.")
    print(f"Çalışma Süresi: {end_time - start_time:.4f} saniye")

    print("\nfib_tabulation fonksiyonunun testi (n = 10000):")
    n = 10000
    start_time = time.time()
    result = fib_tabulation(n)
    end_time = time.time()
    print(f"F({n}) hesaplandı.")
    print(f"Çalışma Süresi: {end_time - start_time:.4f} saniye")

    print("\nfib_optimized fonksiyonunun testi (n = 100000):")
    n = 100000
    start_time = time.time()
    result = fib_optimized(n)
    end_time = time.time()
    print(f"F({n}) hesaplandı.")
    print(f"Çalışma Süresi: {end_time - start_time:.4f} saniye")

# Performansın Görselleştirilmesi
def plot_performance():
    methods = [
        ('Özyinelemeli', fib_recursive),
        ('Memoization', fib_memoization),
        ('Tabulation', fib_tabulation),
        ('Optimize Edilmiş', fib_optimized)
    ]

    ns = [5, 10, 20, 30, 35]
    times = {name: [] for name, _ in methods}

    for name, method in methods:
        for n in ns:
            try:
                start_time = time.time()
                method(n)
                end_time = time.time()
                times[name].append(end_time - start_time)
            except (RecursionError, MemoryError):
                times[name].append(None)

    # Grafik çizimi
    for name in times:
        plt.plot(ns, times[name], label=name)

    plt.xlabel('n Değeri')
    plt.ylabel('Çalışma Süresi (saniye)')
    plt.title('Fibonacci Yöntemlerinin Performans Karşılaştırması')
    plt.legend()
    plt.show()

# Test fonksiyonlarını çalıştırmak için aşağıdaki satırların yorumunu kaldırabilirsiniz
#test_functions()
plot_performance()