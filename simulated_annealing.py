import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Şehirler ve mesafe matrisi
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

# 2. İki şehir arasındaki mesafeyi bulmak için fonksiyon
def distance(city1, city2):
    index1 = cities.index(city1)
    index2 = cities.index(city2)
    return distance_matrix[index1][index2]

# 3. Rastgele bir rota oluştur
def create_random_route():
    route = cities.copy()
    random.shuffle(route)
    return route

# 4. Bir rotanın toplam mesafesini hesapla
def calculate_route_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    total += distance(route[-1], route[0])  # Son şehirden tekrar başlangıca dön
    return total

# 5. Bir rotadan yeni bir komşu rota oluştur
def create_neighbor(route):
    new_route = route.copy()
    i, j = random.sample(range(1, len(route)), 2)  # Başlangıç şehrini sabit tutmak için 1'den başlıyoruz
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

# 6. Simulated Annealing algoritması
def simulated_annealing(temperature = 1000, cooling_rate = 0.995, max_steps = 1000):

    current_route = create_random_route()     # Başlangıç rotası
    current_distance = calculate_route_distance(current_route)

    best_route = current_route
    best_distance = current_distance

    distances_during_steps = []  # Her adımda mesafeyi kaydedeceğiz

    for step in range(max_steps):
        # Bir komşu rota oluştur
        neighbor = create_neighbor(current_route)
        neighbor_distance = calculate_route_distance(neighbor)

        # Yeni rotanın ne kadar daha kötü veya iyi olduğunu hesapla
        difference = neighbor_distance - current_distance

        # 1. Eğer daha iyi ise direkt kabul et
        if difference < 0:
            current_route = neighbor
            current_distance = neighbor_distance

        # 2. Eğer daha kötü ise belli bir ihtimalle kabul et
        else:
            acceptance_probability = math.exp(-difference / temperature)
            if random.random() < acceptance_probability:
                current_route = neighbor
                current_distance = neighbor_distance

        # Şu ana kadarki en iyi çözümü kaydet
        if current_distance < best_distance:
            best_route = current_route
            best_distance = current_distance

        # Bu adımın mesafesini kaydet
        distances_during_steps.append(current_distance)

        # Sıcaklığı azalt
        temperature *= cooling_rate

    return best_route, best_distance, distances_during_steps

best_route, best_distance, distances_during_steps = simulated_annealing(max_steps=200)
# Sonuçları yazdır
print("En iyi bulunan rota:")
print(" -> ".join(best_route))
print("Toplam mesafe:", best_distance)


plt.figure(figsize=(10, 5))
plt.plot(distances_during_steps, marker='o', linestyle='-', color='teal')
plt.title("Simulated Annealing – Rota Mesafesinin İterasyon Boyunca Değişimi")
plt.xlabel("İterasyon")
plt.ylabel("Toplam Mesafe")
plt.grid(True)
plt.tight_layout()
plt.savefig("C:/Users/ASUS/Desktop/simulated_annealing_iterasyon_grafik.png")
plt.show()