# Hill_Climbing_TSP
Hill Climbing algorithm to solve the Traveling Salesman Problem (TSP).
Bu proje, 20 şehirden oluşan bir gezgin satıcı problemi (TSP) için **Hill Climbing** algoritması ile yaklaşık en kısa rotayı bulmayı hedefler.

## 🚀 Kod İçeriği
20*20'lik şehirler arası mesafe matrisi
A’dan T’ye kadar şehir isimleri
Kodun ana bileşenleri:
random_route() → Rastgele bir başlangıç rotası oluşturur.
route_distance() → Rotanın toplam mesafesini hesaplar.
generate_neighbors() → Komşu rotalar üretir (iki şehir yer değiştirerek).
hill_climbing() → En iyi komşuyu seçerek en kısa rotayı bulmaya çalışır.

## 🚀 Kod Detayları
-Index ile iki şehir arasındaki mesafeyi döndüren fonksiyon
-Gezginin yolculuğa başlaması için rastgele bir rota oluşturur. shuffle() fonksiyonu şehirleri rastgele karıştırır.
-Bir rotanın toplam mesafesini hesaplayan fonksiyon oluşturulur. "range(len(route)-1)" ile son şehir hariç tüm şehirlere kadar olan indeksleri üretilir. Son şehri başlangıç noktasına bağlayarak tam rota hesaplanır.
-Her iterasyonda iki şehir yer değiştirir ve yeni bir komşu rota oluşturulur. (swap işlemi)
generate_neighbors(), mevcut rotanın komşularını üretir.
i, rotadaki şehirlerin indeksler. j, i'den sonraki tüm şehir indeksleridir.
len(route) - 1 ifadesi, son şehir hariç tüm şehirleri seçmek için kullanılır.
i indeksindeki şehir ile j indeksindeki şehri yer değiştirerek yeni bir rota oluşturmak.
-Hill Climbing uygulayan fonksiyonda ise, eğer en iyi komşunun mesafesi, mevcut mesafeden daha kötü veya eşitse dur. Çünkü Hill Climbing sadece daha iyi çözümler bulursa ilerler. Eğer daha iyi bir komşu yoksa şu anki çözüm yerel minimum olabilir ve algoritma burada durur.

## 🚀 Kod Çıktısı








