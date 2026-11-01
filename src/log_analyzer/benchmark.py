import time
from .string_matching import KMP


def benchmark_search(kmp, text, pattern, lps, repetitions=10):
    total_time = 0
    total_comparisons = 0

    for _ in range(repetitions):
        start = time.perf_counter()

        _, comparisons = kmp.search(text, pattern, lps)

        end = time.perf_counter()

        total_time += end - start
        total_comparisons += comparisons

    average_time = total_time / repetitions
    average_comparisons = total_comparisons / repetitions

    return average_time, average_comparisons


def run_benchmark():
    kmp = KMP()

    sizes = [100, 1000, 10000]

    # Pola dengan prefiks berulang
    pattern = "A" * 16 + "B"

    # Membuat LPS satu kali seperti pada LogAnalyzer
    lps = kmp.build_lps(pattern)

    print("\n=== SIMULASI DAN PENGUJIAN KMP ===")

    for size in sizes:

        # Worst Case: banyak prefiks cocok, tetapi pola tidak ditemukan
        worst_block = "A" * 16 + "C"
        worst_text = worst_block * size

        # Best Case: pola langsung ditemukan di awal teks
        best_text = pattern + "C" * (
            len(worst_text) - len(pattern)
        )

        best_time, best_comparisons = benchmark_search(
            kmp, best_text, pattern, lps
        )

        worst_time, worst_comparisons = benchmark_search(
            kmp, worst_text, pattern, lps
        )

        print(f"\nUkuran data: {size} blok")
        print(f"Panjang teks: {len(worst_text)} karakter")

        print(
            f"Best Case  - Waktu: {best_time:.8f} detik | "
            f"Perbandingan: {best_comparisons:.0f}"
        )

        print(
            f"Worst Case - Waktu: {worst_time:.8f} detik | "
            f"Perbandingan: {worst_comparisons:.0f}"
        )


if __name__ == "__main__":
    run_benchmark()