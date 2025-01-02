import heapq

def dijkstra(graf, başlangıç):
    
    mesafeler = {düğüm: float('inf') for düğüm in graf}
    mesafeler[başlangıç] = 0
    öncelik_kuyruğu = [(0, başlangıç)]  

    
    en_kısa_yol = {düğüm: [] for düğüm in graf}
    en_kısa_yol[başlangıç] = [başlangıç]

    while öncelik_kuyruğu:
        mevcut_mesafe, mevcut_düğüm = heapq.heappop(öncelik_kuyruğu)

        if mevcut_mesafe > mesafeler[mevcut_düğüm]:
            continue

        for komşu, ağırlık in graf[mevcut_düğüm]:
            mesafe = mevcut_mesafe + ağırlık
            if mesafe < mesafeler[komşu]:
                mesafeler[komşu] = mesafe
                heapq.heappush(öncelik_kuyruğu, (mesafe, komşu))
                en_kısa_yol[komşu] = en_kısa_yol[mevcut_düğüm] + [komşu]

    return mesafeler, en_kısa_yol



graf = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("D", 3), ("E", 8)],
    "D": [("E", 4), ("F", 6)],
    "E": [("F", 1)],
    "F": []
}


mesafeler, en_kısa_yol = dijkstra(graf, "A")


print("A -> F En Kısa Mesafe:", mesafeler["F"])
print("A -> F En Kısa Yol:", en_kısa_yol["F"])
