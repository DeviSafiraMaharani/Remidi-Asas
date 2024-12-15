def biaya_kirim(): 
    # Input lokasi pengiriman
    lokasi = input("Masukkan lokasi pengiriman (Kota/Kabupaten Pasuruan): ").strip().lower() # Strip digunakan utk menghilangkan space kosong, lower utk mengubah huruf menjadi kecil
    if lokasi not in ["kota pasuruan", "kabupaten pasuruan"]:
        print("Maaf, layanan hanya tersedia untuk area Kota dan Kabupaten Pasuruan.")
        return
    
    # Input dimensi paket dalam satuannya
    # Semuanya menggunakan float untuk menampung angka desimal
    panjang = float(input("Masukkan panjang paket (cm): ")) 
    lebar = float(input("Masukkan lebar paket (cm): "))
    tinggi = float(input("Masukkan tinggi paket (cm): "))
    berat = float(input("Masukkan berat paket (kg): "))
    
    # Pastikan berat minimal adalah 1 kg
    if berat < 1:
        berat = 1
        print("Berat paket dianggap minimal 1 kg.")
    
    # Hitung volume paket
    volume = panjang * lebar * tinggi
    
    # Kondisi menghitung biaya
    if panjang <= 50 and lebar <= 50 and tinggi <= 50:
        biaya = 5000
        total = max(8000, berat * biaya)  # Minimal biaya 8000
    else:
        biaya = 7000
        total = max(8000, berat * biaya + 50000)  # Tambahan 50.000
    
    # Menampilkan hasil
    print(f"Lokasi pengiriman: {lokasi.capitalize()}")
    print(f"Dimensi paket: {panjang}cm x {lebar}cm x {tinggi}cm")
    print(f"Berat paket: {berat} kg")
    print(f"Biaya pengiriman: Rp {total:,}")
    
# Jalankan program
biaya_kirim()