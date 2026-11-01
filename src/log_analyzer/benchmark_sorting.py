
import time
import random

from .models import AnomalyResult
from .sorting import MergeSort


def create_data(size):
    """Membuat data hasil deteksi anomali."""
    data = []

    for i in range(size):
        frequency = (i % 100) + 1

        data.append(
            AnomalyResult(
                pattern=f"/pattern/{i}",
                line_numbers=list(
                    range(i + 1, i + frequency + 1)
                )
            )
        )

    # Urutkan berdasarkan kunci yang digunakan Merge Sort
    data.sort(
        key=lambda item: (
            item.frequency,
            item.line_numbers[0]
        )
    )

    return data


def benchmark_sorting(sorter, data, repetitions=5):
    total_time = 0

    for _ in range(repetitions):
        # Salinan dibuat sebelum pengukuran
        test_data = data.copy()

        start = time.perf_counter()
        sorter.sort(test_data)
        end = time.perf_counter()

        total_time += end - start

    return total_time / repetitions


def run_benchmark():
    sorter = MergeSort()
    sizes = [100, 1000, 10000]

    random_generator = random.Random(42)

    print("\n=== SIMULASI DAN PENGUJIAN MERGE SORT ===")

    for size in sizes:

        # Data dasar sudah terurut
        sorted_data = create_data(size)

        # Best Case: data sudah terurut
        best_data = sorted_data.copy()

        # Worst Case simulasi: data terurut terbalik
        worst_data = sorted_data[::-1]

        # Average Case simulasi: data diacak
        average_data = sorted_data.copy()
        random_generator.shuffle(average_data)

        best_time = benchmark_sorting(
            sorter, best_data
        )

        worst_time = benchmark_sorting(
            sorter, worst_data
        )

        average_time = benchmark_sorting(
            sorter, average_data
        )

        print(f"\nUkuran data: {size} elemen")

        print(
            f"Best Case    - Waktu: {best_time:.8f} detik"
        )

        print(
            f"Average Case - Waktu: {average_time:.8f} detik"
        )

        print(
            f"Worst Case   - Waktu: {worst_time:.8f} detik"
        )


if __name__ == "__main__":
    run_benchmark()
