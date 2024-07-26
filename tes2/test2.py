def calculateShippingCost(destination, weight, priority):
    # Validasi input untuk destinasi
    if destination not in ["domestic", "international"]:
        return "Invalid destination"
    
    # Validasi input untuk berat
    if not isinstance(weight, (int, float)) or weight <= 0:
        return "Invalid weight"
    
    # Validasi input untuk prioritas
    if priority not in ["standard", "express", "priority"]:
        return "Invalid priority"
    
    # Menentukan biaya dasar berdasarkan destinasi dan prioritas
    if destination == "domestic":
        if priority == "standard":
            base_cost = 5
        elif priority == "express":
            base_cost = 10
        elif priority == "priority":
            base_cost = 20
        
        # Hitung total biaya berdasarkan berat
        total_cost = weight * base_cost
        
        # Tambahan biaya jika berat lebih dari 10 kg
        if weight > 10:
            total_cost += 10
    
    elif destination == "international":
        if priority == "standard":
            base_cost = 15
        elif priority == "express":
            base_cost = 25
        elif priority == "priority":
            base_cost = 50
        
        # Hitung total biaya berdasarkan berat
        total_cost = weight * base_cost
        
        # Tambahan biaya jika berat lebih dari 5 kg
        if weight > 5:
            total_cost += 50
    
    return total_cost

# Contoh penggunaan
print(calculateShippingCost("domestic", 12, "express"))  # Contoh kasus uji
print(calculateShippingCost("international", 6, "priority"))  # Contoh kasus uji
