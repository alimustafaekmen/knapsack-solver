# 🎒 0/1 Knapsack Problem  -  0/1 Sırt Çantası Problemi

## 🇬🇧 English

A Python application that solves the **0/1 Knapsack Problem** using **Dynamic Programming**.

### About

Given a bag with a maximum weight capacity and a set of items with specific weights and values, this program finds the optimal combination of items that maximizes total value without exceeding the capacity.

### How It Works

1. User enters the bag capacity (Kg) and information for 5 items (name, value, weight)
2. The algorithm builds a DP table to find the maximum achievable value
3. Backtracking is used to identify which items were selected
4. Results are displayed with value/weight ratios for analysis

### Algorithm Details

- **Approach:** Dynamic Programming (Bottom-Up)
- **Time Complexity:** O(n × W) — n: number of items, W: scaled capacity
- **Space Complexity:** O(n × W)
- **Decimal Support:** Weights are scaled by 100x for integer-based DP (0.01 Kg precision)

### Usage

```bash
python knapsack.py
```

### Example Output

```
0/1 Knapsack Problem / 0/1 Sırt Çantası Problemi
-------------------------------------------------
Enter bag capacity (Kg) / Çanta kapasitesi (Kg): 10

Item 1 / Eşya 1:
  Name / İsim: Laptop
  Value (TL) / Değer (TL): 3000
  Weight (Kg) / Ağırlık (Kg): 2.5

...

==================================================
RESULTS / SONUÇLAR
==================================================

Selected Items / Seçilen Eşyalar:
  ✓ Laptop (Value/Değer: 3000.0 TL, Weight/Ağırlık: 2.5 Kg, Ratio/Oran: 1200.00)

Total Value / Toplam Değer: 5500.00 TL
Total Weight / Toplam Ağırlık: 8.50 Kg
Remaining Capacity / Kalan Kapasite: 1.50 Kg
```

---

## 🇹🇷 Türkçe

**0/1 Sırt Çantası Problemini** **Dinamik Programlama** ile çözen bir Python uygulamasıdır.

### Hakkında

Belirli bir kapasiteye sahip bir çanta ve her birinin ağırlığı ve değeri olan eşyalar verildiğinde, program kapasiteyi aşmadan toplam değeri maksimize eden en iyi eşya kombinasyonunu bulur.

### Nasıl Çalışır

1. Kullanıcı çanta kapasitesini (Kg) ve 5 eşyanın bilgilerini (isim, değer, ağırlık) girer
2. Algoritma, elde edilebilecek maksimum değeri bulmak için bir DP tablosu oluşturur
3. Geriye iz sürme ile hangi eşyaların seçildiği belirlenir
4. Sonuçlar, analiz için değer/ağırlık oranlarıyla birlikte gösterilir

### Algoritma Detayları

- **Yaklaşım:** Dinamik Programlama (Aşağıdan Yukarı)
- **Zaman Karmaşıklığı:** O(n × W) — n: eşya sayısı, W: ölçeklendirilmiş kapasite
- **Uzay Karmaşıklığı:** O(n × W)
- **Ondalık Desteği:** Ağırlıklar 100x ölçeklendirilerek tam sayı tabanlı DP'ye uyumlu hale getirilir

### Çalıştırma

```bash
python knapsack.py
```

---

## 📁 Project Structure / Proje Yapısı

```
Knapsack Project/
├── knapsack.py     # Main application / Ana uygulama
├── .gitignore      # Git ignore rules / Git yok sayma kuralları
└── README.md       # Documentation / Dokümantasyon
```

## 📄 License / Lisans

This project was developed for educational purposes. / Bu proje eğitim amaçlı geliştirilmiştir.
