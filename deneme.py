import random
import math

# Şehirlerin koordinatları
cities = {
    "A": (2, 3),
    "B": (5, 8),
    "C": (1, 9),
    "D": (7, 2),
    "E": (3, 6),
    "F": (8, 5),
}

# Mesafe hesaplama fonksiyonu (Öklidyen Mesafe)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Rastgele bir rota oluştur
def random_route():
    route = list(cities.keys())  # Şehirlerin isim listesini al
    route.remove("A")  # A başlangıç noktası
    random.shuffle(route)  # Şehirleri rastgele karıştır
    return ["A"] + route + ["A"]  # Başlangıç ve bitiş noktası A olsun

# Rotanın toplam mesafesini hesapla
def route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    return total_distance

# Komşu çözümleri üret (Swap yöntemi ile)
def get_neighbors(route):
    neighbors = []
    for i in range(1, len(route) - 2):  # İlk ve son elemanı değiştirme
        for j in range(i + 1, len(route) - 1):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap işlemi
            neighbors.append(new_route)
    return neighbors

# Hill Climbing Algoritması
def hill_climbing():
    current_route = random_route()
    current_distance = route_distance(current_route)
    
    while True:
        neighbors = get_neighbors(current_route)
        best_neighbor = min(neighbors, key=route_distance)  # En iyi komşuyu seç
        best_distance = route_distance(best_neighbor)
        
        if best_distance >= current_distance:  # Eğer iyileşme yoksa dur
            break
        
        current_route = best_neighbor
        current_distance = best_distance

    return current_route, current_distance

# Çalıştır ve sonucu göster
best_route, best_distance = hill_climbing()
print("En iyi rota:", best_route)
print("Toplam mesafe:", best_distance)
