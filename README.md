# 2026 PROYEK 1 DAA 3A

## E. Deduplikasi Log Server & Anomali Siber

### 1. Identitas Proyek

Proyek ini merupakan bagian dari tugas **Proyek 1 mata kuliah Desain dan Analisis Algoritma (DAA) kelas 3A tahun 2026**.

Pada proyek ini, kami memilih **Studi Kasus E: Deduplikasi Log Server & Anomali Siber** sebagai topik yang akan dianalisis dan diimplementasikan.

### 2. Deskripsi Proyek

Server menghasilkan banyak baris log aktivitas setiap detiknya. Sebagian besar log merupakan aktivitas normal, sedangkan sebagian lainnya mengandung indikasi serangan siber, seperti SQL Injection dan Buffer Overflow.

Permasalahan yang diangkat dalam proyek ini adalah bagaimana memindai kumpulan log server untuk menemukan baris yang mengandung pola anomali tertentu, mencatat nomor baris tempat pola ditemukan, menghitung frekuensi kemunculannya, serta mengurutkan hasil berdasarkan tingkat kelangkaan serangan.

Program akan mengolah file log dan pola anomali yang diberikan sebagai input, kemudian menghasilkan laporan deteksi anomali yang terurut dari frekuensi paling sedikit hingga paling banyak.

### 3. Tujuan Proyek

Tujuan dari proyek ini adalah:

- Mengidentifikasi baris log yang mengandung pola anomali atau signature serangan siber.
- Menampilkan nomor baris tempat setiap pola anomali ditemukan.
- Menghitung frekuensi kemunculan setiap pola berdasarkan jumlah baris yang mengandung pola tersebut.
- Mengurutkan hasil deteksi dari frekuensi terkecil hingga terbesar.
- Menganalisis dan membandingkan kompleksitas algoritma berdasarkan teori dan hasil eksperimen.

### 4. Algoritma yang Digunakan

Dalam menyelesaikan permasalahan ini, algoritma yang dipilih adalah:

| Algoritma | Kegunaan |
|---|---|
| KMP (Knuth-Morris-Pratt) | Mencari pola anomali di dalam setiap baris log secara efisien menggunakan tabel LPS (*Longest Prefix Suffix*). |
| Merge Sort | Mengurutkan hasil deteksi berdasarkan frekuensi kemunculan, dari yang paling sedikit hingga paling banyak. |
| Naive String Matching | Digunakan sebagai algoritma pembanding untuk mengevaluasi kinerja pencarian pola. |

### 5. Gambaran Alur Program

Secara umum, program akan menjalankan tahapan berikut:

1. Menerima lokasi file log dan pola anomali yang ingin dicari.
2. Membaca file log serta menyimpan setiap baris beserta nomor barisnya.
3. Membangun tabel LPS untuk setiap pola menggunakan algoritma KMP.
4. Melakukan pencarian pola terhadap seluruh baris log.
5. Mengumpulkan nomor baris yang mengandung pola dan menghitung frekuensinya.
6. Mengelompokkan hasil pencarian berdasarkan pola anomali.
7. Mengurutkan hasil menggunakan Merge Sort berdasarkan frekuensi terkecil hingga terbesar.
8. Menampilkan laporan hasil deteksi beserta metrik perbandingan karakter.

### 6. Ketentuan Implementasi

Implementasi proyek mengikuti ketentuan studi kasus, yaitu:

- Input menggunakan karakter ASCII yang dapat dicetak (*printable characters*).
- Karakter newline (`\n`) digunakan sebagai pemisah antarbaris log.
- Program mengembalikan nomor baris yang mengandung pola anomali beserta frekuensinya.
- Menggunakan KMP sebagai algoritma pencocokan pola.
- Menggunakan Merge Sort untuk pengurutan hasil deteksi.
- Tidak menggunakan operator/fungsi `in` untuk pencarian pola, `str.find()`, maupun `collections.Counter` bawaan Python.

### 7. Analisis dan Pengujian

Proyek ini juga mencakup analisis terhadap algoritma yang digunakan, meliputi:

- Analisis kompleksitas waktu dan ruang.
- Pembuktian *correctness* dan *termination*.
- Pengujian menggunakan beberapa ukuran data.
- Simulasi skenario terbaik dan terburuk.
- Pengukuran waktu eksekusi dan penggunaan memori.
- Analisis *time-space trade-off* berdasarkan hasil pengujian.

### 8. Hasil yang Diharapkan

Program diharapkan dapat menghasilkan laporan anomali server yang berisi pola serangan, nomor baris pertama tempat pola ditemukan, dan frekuensi kemunculannya.

Hasil laporan diurutkan mulai dari pola dengan frekuensi paling rendah hingga paling tinggi sehingga pola anomali yang lebih jarang dapat lebih mudah diidentifikasi.

---

**Proyek 1 - Desain dan Analisis Algoritma (DAA) 3A**  
**Tahun Akademik 2026**