import time
from .string_matching import KMP


def benchmark_search(kmp, text, pattern, repetitions=10):
    total_time = 0
    total_comparisons = 0

    for _ in range(repetitions):
        start = time.perf_counter()

        _, comparisons = kmp.search(text, pattern)

        end = time.perf_counter()

        total_time += end - start
        total_comparisons += comparisons

    average_time = total_time / repetitions
    average_comparisons = total_comparisons / repetitions

    return average_time, average_comparisons


def run_benchmark():

    kmp = KMP()

    sizes = [100, 1000, 10000]

    pattern = "POST /healthcheck"

    print("\n=== SIMULASI DAN PENGUJIAN KMP ===")

    for size in sizes:

        # Membuat data log simulasi
        best_text = "POST /healthcheck\n" * size

        worst_text = "GET /index.html\n" * size

        # Menggabungkan seluruh baris menjadi satu teks
        best_text = best_text.replace("\n", "")
        worst_text = worst_text.replace("\n", "")

        # Pengujian pola ditemukan
        best_time, best_comparisons = benchmark_search(
            kmp, best_text, pattern
        )

        # Pengujian pola tidak ditemukan
        worst_time, worst_comparisons = benchmark_search(
            kmp, worst_text, pattern
        )

        print(f"\nUkuran data: {size} baris")
        print(
            f"Terbaik  - Waktu: {best_time:.8f} detik | "
            f"Perbandingan: {best_comparisons}"
        )
        print(
            f"Terburuk - Waktu: {worst_time:.8f} detik | "
            f"Perbandingan: {worst_comparisons}"
        )


if __name__ == "__main__":
    run_benchmark()