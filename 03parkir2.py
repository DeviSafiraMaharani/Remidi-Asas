# Fungsi untuk menghitung total biaya parkir
def tarif():
    # Jika durasi kurang dari atau sama dengan 2 jam
    if durasi <= 2:
        biaya = 3000  
    # Jika durasi lebih dari 2 jam dan kurang dari atau sama dengan 24 jam
    elif durasi <= 24:
        biaya = 3000 + (1500 * (durasi - 2)) 
    # Jika durasi lebih dari 24 jam
    else:
        biaya = 3000 + (1500 * (durasi - 2)) + 10000  
    return biaya  # Mengembalikan total biaya

# Loop untuk meminta input durasi parkir
while True:
    try:
        # Meminta input durasi parkir dari pengguna
        durasi = int(input("Masukkan durasi parkir Anda: "))
        
        # Memeriksa apakah durasi valid (harus lebih dari 0)
        if durasi <= 0:
            print("Angka yang dimasukkan tidak valid.")
        else:
            # Menghitung total biaya parkir
            total = tarif()
            # Menampilkan hasil total biaya parkir
            print(f"Durasi parkir Anda {durasi} jam. Total biayanya adalah Rp. {total:,}")
            break  # Keluar dari loop jika input valid
    except ValueError:
        # Jika input bukan angka, tampilkan pesan error
        print("Input yang dimasukkan tidak valid.")