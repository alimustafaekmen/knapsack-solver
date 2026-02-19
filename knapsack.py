def knapsack(values, weights, capacity):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    0/1 Knapsack problemini Dinamik Programlama ile çözer.

    Parameters / Parametreler:
        values   : List of item values (TL) / Eşyaların değerleri
        weights  : List of item weights (Kg) / Eşyaların ağırlıkları
        capacity : Maximum capacity of bag (Kg) / Çantanın maksimum kapasitesi

    Returns / Dönüş:
        max_value       : Total value of selected items / Seçilen eşyaların toplam değeri
        total_weight    : Total weight of selected items / Seçilen eşyaların toplam ağırlığı
        selected_items  : Indices of selected items / Seçilen eşyaların indeksleri
    """

    # Scaling: Multiply by 100 to handle decimal weights as integers
    # Ölçeklendirme: Ondalıklı ağırlıkları tam sayıya çevirmek için 100 ile çarpıyoruz
    # Example / Örnek: 2.5 Kg → 250, 1.5 Kg → 150
    scale = 100
    capacity = int(capacity * scale)

    # Scale each weight individually / Her ağırlığı ayrı ayrı ölçeklendir
    scaled_weights = []
    for w in weights:
        scaled_weights.append(int(w * scale))
    weights = scaled_weights

    n = len(values)  # Number of items / Eşya sayısı

    # Create DP table filled with zeros
    # Sıfırlarla dolu DP tablosu oluştur
    # dp[i][w] = Best value using first i items with capacity w
    # dp[i][w] = İlk i eşyayla w kapasitede elde edilebilecek en iyi değer
    dp = []
    for i in range(n + 1):
        row = []
        for w in range(capacity + 1):
            row.append(0)
        dp.append(row)

    # Fill the DP table / DP tablosunu doldur
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Two choices: take the item or skip it
                # İki seçenek: eşyayı al veya atla
                take = values[i - 1] * scale + dp[i - 1][w - weights[i - 1]]
                skip = dp[i - 1][w]

                # Pick the better option / Daha iyi olanı seç
                if take > skip:
                    dp[i][w] = take
                else:
                    dp[i][w] = skip
            else:
                # Item is too heavy, skip it / Eşya çok ağır, atla
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]  # Optimal solution / Optimal çözüm

    # Backtracking: Find which items were selected
    # Geriye iz sürme: Hangi eşyaların seçildiğini bul
    selected_items = []
    total_weight = 0
    w = capacity

    # Go backwards from last item to first / Son eşyadan ilke doğru git
    i = n
    while i > 0:
        # If value changed, this item was selected
        # Değer değiştiyse bu eşya seçilmiş demektir
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            total_weight = total_weight + weights[i - 1]
            w = w - weights[i - 1]
        i = i - 1

    selected_items.reverse()  # Sort in original order / Orijinal sıraya çevir

    # Convert back to original scale / Orijinal ölçeğe geri çevir
    max_value = max_value / scale
    total_weight = total_weight / scale

    return max_value, total_weight, selected_items


def get_positive_float(prompt):
    """
    Gets a positive float number from user with input validation.
    Kullanıcıdan pozitif ondalıklı sayı alır, giriş doğrulaması yapar.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value. / Lütfen pozitif bir değer girin.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number. / Geçersiz giriş! Lütfen sayı girin.")


def get_name(prompt):
    """
    Gets a valid name (only letters) from user.
    Kullanıcıdan geçerli bir isim (sadece harf) alır.
    """
    while True:
        name = input(prompt).strip()
        if name.isalpha():
            return name
        print("Invalid name! Use only letters. / Geçersiz isim! Sadece harf kullanın.")


def main():
    """
    Main function: Gets user input, solves knapsack problem, prints results.
    Ana fonksiyon: Kullanıcı girdisi alır, knapsack problemini çözer, sonuçları yazdırır.
    """

    print("0/1 Knapsack Problem / 0/1 Sırt Çantası Problemi")
    print("-" * 49)

    # Get bag capacity from user / Kullanıcıdan çanta kapasitesini al
    capacity = get_positive_float("Enter bag capacity (Kg) / Çanta kapasitesi (Kg): ")

    # Collect information for 5 items / 5 eşya için bilgi topla
    names = []
    values = []
    weights = []

    for i in range(5):
        print(f"\nItem {i + 1} / Eşya {i + 1}:")
        name = get_name("  Name / İsim: ")
        value = get_positive_float("  Value (TL) / Değer (TL): ")
        weight = get_positive_float("  Weight (Kg) / Ağırlık (Kg): ")

        names.append(name)
        values.append(value)
        weights.append(weight)

    # Solve the knapsack problem / Knapsack problemini çöz
    max_value, total_weight, selected_indices = knapsack(values, weights, capacity)

    # Calculate value/weight ratio for each item
    # Her eşya için değer/ağırlık oranını hesapla
    ratios = []
    for i in range(len(values)):
        ratio = values[i] / weights[i]
        ratios.append(ratio)

    # Print results / Sonuçları yazdır
    print("\n" + "=" * 50)
    print("RESULTS / SONUÇLAR")
    print("=" * 50)

    print("\nAll Items (Value/Weight Ratios) / Tüm Eşyalar (Değer/Ağırlık Oranları):")
    for i in range(len(names)):
        print(f"  - {names[i]} (Value/Değer: {values[i]} TL, Weight/Ağırlık: {weights[i]} Kg, Ratio/Oran: {ratios[i]:.2f})")

    print("\nSelected Items / Seçilen Eşyalar:")
    for i in selected_indices:
        print(f"  ✓ {names[i]} (Value/Değer: {values[i]} TL, Weight/Ağırlık: {weights[i]} Kg, Ratio/Oran: {ratios[i]:.2f})")

    print(f"\nTotal Value / Toplam Değer: {max_value:.2f} TL")
    print(f"Total Weight / Toplam Ağırlık: {total_weight:.2f} Kg")
    print(f"Remaining Capacity / Kalan Kapasite: {capacity - total_weight:.2f} Kg")


if __name__ == "__main__":
    main()
