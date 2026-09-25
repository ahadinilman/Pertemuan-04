# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

**Nama:** Ahadin Ilman
**NIM:** 2225250220  
**Kelas:** 3A  

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai `if-elif-else`.

## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py

Tabel Keputusan
Kategori,Syarat Validasi / Rentang,Contoh Masukan
Validasi Tipe Data,Semua input harus numerik (float/int),"Ujian: 80, Tugas: 80, Kehadiran: abc (Ditolak)"
Validasi Rentang,"0≤Ujian,Tugas,Kehadiran≤100","Ujian: 105, Tugas: 80, Kehadiran: 90 (Ditolak)"
Syarat Kehadiran,Kehadiran <80%,"Ujian: 90, Tugas: 90, Kehadiran: 75"
Predikat A,Nilai≥85 dan Kehadiran ≥80%,"Ujian: 90, Tugas: 80, Kehadiran: 95"
Predikat B,70≤Nilai<85 dan Kehadiran ≥80%,"Ujian: 75, Tugas: 70, Kehadiran: 85"
Predikat C,60≤Nilai<70 dan Kehadiran ≥80%,"Ujian: 60, Tugas: 60, Kehadiran: 80"
Predikat D,50≤Nilai<60 dan Kehadiran ≥80%,"Ujian: 55, Tugas: 50, Kehadiran: 90"
Predikat E,Nilai<50 dan Kehadiran ≥80%,"Ujian: 40, Tugas: 30, Kehadiran: 100"

Hasil Pengujian
Ujian,Tugas,Kehadiran,Nilai Akhir,Keluaran yang Diharapkan,Keluaran Aktual,Status
Input:90,80,95,hasil yg diharapkan:86.00,"Predikat A, Lulus",hasil percobaan:"Predikat A, Lulus",Sesuai
Input:75,70,85,hasil yg diharapkan:73.00,"Predikat B, Lulus",hasil percobaan:"Predikat B, Lulus",Sesuai
Input:60,60,80,hasil yg diharapkan:60.00,"Predikat C, Lulus",hasil percobaan:"Predikat C, Lulus",Sesuai
Input:55,50,90,hasil yg diharapkan:53.00,"Predikat D, Belum lulus",hasil percobaan:"Predikat D, Belum lulus",Sesuai
Input:40,30,100,hasil yg diharapkan:36.00,"Predikat E, Belum lulus",hasil percobaan:"Predikat E, Belum lulus",Sesuai
Input:90,90,75,hasil yg diharapkan:90.00,"Nilai akhir tetap tampil,status Tidak memenuhi syarat kehadiran",hasil percobaan:"Nilai akhir: 90.00, Status: Tidak memenuhi syarat kehadiran",Sesuai
Input:105,80,90,hasil yg diharapkan-,:Pesan penolakan rentang nilai ujian,hasil percobaan:Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.,Sesuai
Input:80,-5,90,hasil yg diharapkan:-,Pesan penolakan rentang nilai tugas,hasil percobaan:Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.,Sesuai
Input:80,80,abc,hasil yg diharapkan:-,Pesan penolakan tipe,hasil percobaan:Masukan ditolak: seluruh data harus berupa angka.,Sesuai

Refleksi
Salah satu masukan tidak valid yang semula berpotensi terlewat adalah penanganan tipe data non-numerik (seperti huruf atau simbol)serta nilai
rentang di luar 0 hingga 100.Masalah ini ditangani dengan menggunakan blok try-except ValueError untuk menguji konversi tipe data sebelum pengolahan nilai.
Selain itu, pengecekan rentang dilakukan menggunakan rantai if-elif-else sebelum melakukan kalkulasi nilai akhir dan penentuan predikat,sehingga program 
tidak mengalami crash saat menerima masukan yang tidak valid.
