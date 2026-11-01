# E. Deduplikasi Log Server & Anomali Siber

## Deskripsi Proyek

Program ini merupakan implementasi algoritma pencarian string dan pengurutan untuk mendeteksi pola anomali pada file log server.

Program membaca file log, mencari pola anomali yang dimasukkan pengguna, mencatat nomor baris tempat pola ditemukan, menghitung frekuensi berdasarkan jumlah baris yang mengandung pola, kemudian mengurutkan hasil dari frekuensi paling sedikit hingga paling banyak.

## Fitur

- Membaca data log dari file `server.log`.
- Mencari pola anomali menggunakan algoritma Knuth-Morris-Pratt (KMP).
- Mencatat nomor baris tempat pola ditemukan.
- Menghitung frekuensi setiap pola.
- Mengurutkan hasil menggunakan Merge Sort.
- Menampilkan jumlah perbandingan karakter pencarian KMP.
- Membandingkan pendekatan iteratif dan rekursif untuk perhitungan total frekuensi.

## Algoritma yang Digunakan

### Algoritma utama

| Algoritma | Fungsi |
|---|---|
| KMP | Mencari pola anomali dalam setiap baris log |
| Merge Sort | Mengurutkan hasil berdasarkan frekuensi terkecil |

### Algoritma pembanding

| Algoritma | Kegunaan |
|---|---|
| Linear Search | Pembanding pencarian substring secara naif |
| Binary Search | Pembanding pencarian kecocokan seluruh isi baris |
| Boyer-Moore | Pembanding pencocokan string menggunakan bad-character heuristic |
| Bubble Sort | Pembanding algoritma pengurutan |
| Selection Sort | Pembanding algoritma pengurutan |
| Insertion Sort | Pembanding algoritma pengurutan |

## Struktur Proyek

```text
proyek-1-daa/
├── data/
│   └── server.log
├── img/
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── models.py
│       ├── log_reader.py
│       ├── searching.py
│       ├── string_matching.py
│       ├── sorting.py
│       ├── analyzer.py
│       ├── benchmark.py
│       ├── benchmark_sorting.py
│       ├── benchmark_comparison.py
│       └── main.py
├── test/
│   ├── test_string_matching.py
│   ├── test_sorting.py
│   └── test_analyzer.py
├── pyproject.toml
└── README.md
```

## Persyaratan

- Python 3.12 atau lebih baru.
- Pytest untuk menjalankan unit test.

## Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama proyek:

```powershell
py -m log_analyzer.main
```

Program akan membaca file `data/server.log`, kemudian meminta pengguna memasukkan jumlah pola anomali dan pola yang ingin dicari.

## Menjalankan Pengujian

Untuk menjalankan seluruh unit test:

```powershell
py -m pytest -v
```

## Menjalankan Benchmark

### 1. Benchmark KMP

```powershell
py -m log_analyzer.benchmark
```

Pengujian dilakukan dengan variasi ukuran input dan kondisi pencarian terbaik serta terburuk yang disimulasikan.

### 2. Benchmark Merge Sort

```powershell
py -m log_analyzer.benchmark_sorting
```

Pengujian dilakukan pada data terurut, acak, dan terurut terbalik dengan ukuran 100, 1.000, dan 10.000 elemen.

### 3. Perbandingan Algoritma Sorting

```powershell
py -m log_analyzer.benchmark_comparison
```

Membandingkan Bubble Sort, Selection Sort, Insertion Sort, dan Merge Sort pada beberapa ukuran input.

## Kompleksitas Algoritma Utama

| Algoritma | Kompleksitas Waktu | Kompleksitas Ruang |
|---|---|---|
| KMP | O(N + m) per pola | O(m) |
| Merge Sort | O(k log k) | O(k) |

Keterangan:

- N adalah total karakter log.
- m adalah panjang pola.
- k adalah jumlah pola anomali.

Untuk seluruh proses pencarian terhadap k pola, kompleksitas waktunya adalah O(kN + P), dengan P sebagai total panjang seluruh pola.

## Ketentuan Implementasi

- Tidak menggunakan operator `in` untuk pencarian pola.
- Tidak menggunakan `str.find()` untuk pencarian pola.
- Tidak menggunakan `collections.Counter`.
- Pencarian pola utama dilakukan menggunakan implementasi KMP.
- Pengurutan laporan utama dilakukan menggunakan implementasi Merge Sort.

## Hasil yang Diharapkan

Program menghasilkan laporan yang berisi:

1. Pola anomali yang dicari.
2. Nomor baris pertama tempat pola ditemukan.
3. Frekuensi berdasarkan jumlah baris yang mengandung pola.
4. Hasil yang telah diurutkan dari frekuensi paling sedikit hingga paling banyak.
5. Metrik perbandingan karakter KMP.

## Pengembang

Proyek ini dibuat untuk memenuhi tugas Proyek 1 mata kuliah Desain dan Analisis Algoritma (DAA).

**Topik:** E. Deduplikasi Log Server & Anomali Siber

**Repository:** [Tambahkan tautan GitHub repository]
