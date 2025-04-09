import random
import numpy as np

# Şehir isimleri
cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]

# Şehirler arası mesafe matrisi 20*20
distance_matrix = np.array([
 [0, 65, 49, 74, 72, 23, 71, 16, 20, 83, 48, 88, 55, 42, 60, 39, 43, 48, 45, 47],
    [65, 0, 46, 41, 71, 37, 22, 84, 82, 78, 64, 63, 68, 64, 26, 37, 21, 38, 15, 40],
    [49, 46, 0, 50, 20, 64, 67, 34, 67, 66, 49, 49, 32, 31, 41, 52, 64, 49, 63, 55],
    [74, 41, 50, 0, 50, 36, 34, 27, 36, 26, 15, 67, 75, 89, 18, 53, 72, 53, 36, 65],
    [72, 71, 20, 50, 0, 49, 88, 28, 60, 20, 31, 51, 30, 89, 53, 86, 73, 69, 45, 34],
    [23, 37, 64, 36, 49, 0, 57, 44, 54, 39, 74, 18, 69, 44, 59, 31, 83, 17, 47, 59],
    [71, 22, 67, 34, 88, 57, 0, 88, 44, 52, 63, 16, 46, 43, 32, 27, 58, 39, 67, 45],
    [16, 84, 34, 27, 28, 44, 88, 0, 75, 13, 25, 52, 60, 39, 53, 68, 53, 52, 24, 26],
    [20, 82, 67, 36, 60, 54, 44, 75, 0, 54, 53, 32, 55, 75, 20, 60, 43, 70, 48, 89],
    [83, 78, 66, 26, 20, 39, 52, 13, 54, 0, 78, 69, 29, 33, 69, 58, 45, 51, 40, 54],
    [48, 64, 49, 15, 31, 74, 63, 25, 53, 78, 0, 67, 24, 47, 30, 43, 42, 9, 75, 27],
    [88, 63, 49, 67, 51, 18, 16, 52, 32, 69, 67, 0, 25, 32, 57, 80, 55, 56, 57, 41],
    [55, 68, 32, 75, 30, 69, 46, 60, 55, 29, 24, 25, 0, 26, 17, 52, 37, 46, 21, 49],
    [42, 64, 31, 89, 89, 44, 43, 39, 75, 33, 47, 32, 26, 0, 34, 44, 35, 68, 34, 20],
    [60, 26, 41, 18, 53, 59, 32, 53, 20, 69, 30, 57, 17, 34, 0, 55, 65, 75, 2, 62],
    [39, 37, 52, 53, 86, 31, 27, 68, 60, 58, 43, 80, 52, 44, 55, 0, 89, 63, 25, 76],
    [43, 21, 64, 72, 73, 83, 58, 53, 43, 45, 42, 55, 37, 35, 65, 89, 0, 78, 74, 48],
    [48, 38, 49, 53, 69, 17, 39, 52, 70, 51, 9, 56, 46, 68, 75, 63, 78, 0, 53, 44],
    [45, 15, 63, 36, 45, 47, 67, 24, 48, 40, 75, 57, 21, 34, 2, 25, 74, 53, 0, 15],
    [47, 40, 55, 65, 34, 59, 45, 26, 89, 54, 27, 41, 49, 20, 62, 76, 48, 44, 15, 0]
])

# İki şehir arasındaki mesafeyi döndüren fonksiyon
def distance(city1, city2):
    return distance_matrix[cities.index(city1)][cities.index(city2)]

# Rastgele bir rota oluşturan fonksiyon
def random_route():
    route = cities[:]  # Şehirler listesinin bir kopyasını oluştur
    random.shuffle(route)  # Şehirleri rastgele sıraya diz
    return route  

# Bir rotanın toplam mesafesini hesaplayan fonksiyon
def route_distance(route):
    total_distance = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    total_distance += distance(route[-1], route[0])  # Başlangıç noktasına geri dön
    return total_distance

# Komşu rotaları üreten fonksiyon (Swap yöntemi ile)
def generate_neighbors(route):
    neighbors = []  # Boş bir liste oluştur
    for i in range(len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route[:]  # Mevcut rotanın bir kopyasını al
            new_route[i], new_route[j] = new_route[j], new_route[i]  # İki şehrin yerini değiştir (swap işlemi)
            neighbors.append(new_route)  # Yeni komşu rotayı listeye ekle
    return neighbors  # Tüm komşuları döndür

# Hill Climbing algoritmasını uygulayan fonksiyon
def hill_climbing():

    current_route = random_route()  # Başlangıç için rastgele bir rota seç
    current_distance = route_distance(current_route)  # Rotanın toplam mesafesini hesapla
    
    while True:
        neighbors = generate_neighbors(current_route)  # Komşu rotaları oluştur
        best_neighbor = min(neighbors, key=route_distance)  # En kısa mesafeli komşuyu seç
        best_distance = route_distance(best_neighbor)  # Seçilen komşunun mesafesini hesapla
        
        if best_distance >= current_distance:  # Eğer daha iyi bir komşu yoksa dur
            break
        
        current_route, current_distance = best_neighbor, best_distance  # Daha iyi komşuya geç
    
    return current_route, current_distance  # Bulunan en iyi rotayı ve mesafesini döndür

# Algoritmayı çalıştır
best_route, best_distance = hill_climbing()
print("En iyi rota:", best_route)
print("Toplam mesafe:", best_distance)
