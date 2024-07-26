def calculateTax(income, age, dependents):
    # Validasi input
    if not isinstance(income, (int, float)) or income < 0:
        return "Invalid income"
    if not isinstance(age, (int, float)) or age < 0:
        return "Invalid age"
    if not isinstance(dependents, (int, float)) or dependents < 0:
        return "Invalid dependents"
    
    # Jika usia kurang dari 18 tahun, tidak wajib pajak
    if age < 18:
        return "Not eligible for tax"
    
    # Menentukan pajak dasar berdasarkan pendapatan
    if income <= 10000:
        base_tax = income * 0.1
    elif income <= 50000:
        base_tax = income * 0.2
    else:
        base_tax = income * 0.3
    
    # Hitung diskon pajak untuk usia 65 tahun atau lebih
    if age >= 65:
        base_tax *= 0.8
    
    # Hitung pengurangan pajak untuk tanggungan
    deduction = dependents * 500
    
    # Hitung pajak akhir
    final_tax = base_tax - deduction
    
    # Pastikan pajak minimum adalah $0
    if final_tax < 0:
        final_tax = 0
    
    return final_tax

# Contoh penggunaan
print(calculateTax(60000, 70, 2))  # Contoh kasus uji
