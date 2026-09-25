teks = input("Jumlah soal benar dari 20: ").strip()

try:
    benar = int(teks)
except ValueError:
    print("Masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("Masukan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = (benar / 20) * 100
        if persen >= 75:
            print(f"{persen:.2f} persen dan Tuntas")
        else:
            print(f"{persen:.2f} persen dan Belum tuntas")