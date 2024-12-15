def biaya(durasi, kendaraan):
    # Tarif dasar untuk dua jam pertama
    awal = 3000
    # Tarif per jam setelah dua jam pertama untuk masing-masing jenis kendaraan
    motor = 1000
    mobil = 1500
    # Biaya tambahan jika parkir melebihi 24 jam
    lebih = 10000

    # Menentukan tarif per jam berdasarkan jenis kendaraan
    if kendaraan == "sepeda motor":
        tarif = motor
    elif kendaraan == "mobil":
        tarif = mobil
    else:
        # Jika jenis kendaraan tidak valid, kembalikan pesan kesalahan
        return "Jenis kendaraan tidak valid."

    # Menghitung biaya parkir berdasarkan durasi
    if durasi <= 2:
        # Untuk durasi 2 jam atau kurang, hanya dikenakan tarif awal
        biaya = awal
    elif durasi <= 24:
        # Untuk durasi lebih dari 2 jam tetapi kurang atau sama dengan 24 jam
        biaya = awal + tarif * (durasi - 2)
    else:
        # Untuk durasi lebih dari 24 jam, tambahkan biaya tambahan
        biaya = awal + tarif * (durasi - 2) + lebih

    # Mengembalikan hasil perhitungan biaya parkir
    return biaya

# Input dari pengguna
try:
    # Meminta input durasi parkir dari pengguna
    durasi = int(input("Masukkan durasi parkir (dalam jam): "))
    # Meminta input jenis kendaraan dari pengguna
    kendaraan = input("Masukkan jenis kendaraan (sepeda motor/mobil): ").lower()

    # Validasi untuk durasi negatif
    if durasi < 0:
        print("Durasi yang Anda masukkan tidak valid.")
    else:
        # Memanggil fungsi untuk menghitung biaya parkir
        total = biaya(durasi, kendaraan)
        # Jika fungsi mengembalikan pesan kesalahan, tampilkan pesan tersebut
        if isinstance(total, str):
            print(total)
        else:
            # Jika berhasil, tampilkan total biaya parkir
            print(f"Biaya parkir untuk {durasi} jam dengan {kendaraan} adalah Rp: {total:,}")
except ValueError:
    # Menangkap kesalahan jika input durasi bukan angka
    print("Input durasi harus berupa angka.")