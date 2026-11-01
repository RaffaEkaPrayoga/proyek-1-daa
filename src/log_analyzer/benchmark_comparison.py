
import time
import random

from .models import AnomalyResult
from .sorting import (
    BubbleSort,
    SelectionSort,
    InsertionSort,
    MergeSort
)


def create_data(size):
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

    data.sort(
        key=lambda item: (
            item.frequency,
            item.line_numbers[0]
        )
    )

    return data


def measure_time(sorter, data, repetitions=3):
    total_time = 0

    for _ in range(repetitions):
        test_data = data.copy()

        start = time.perf_counter()
        sorter.sort(test_data)
        end = time.perf_counter()

        total_time += end - start

    return total_time / repetitions


def run_benchmark():
    algorithms = {
        "Bubble Sort": BubbleSort(),
        "Selection Sort": SelectionSort(),
        "Insertion Sort": InsertionSort(),
        "Merge Sort": MergeSort()
    }

    sizes = [100, 500, 1000]
    rng = random.Random(42)

    print("\n=== PERBANDINGAN ALGORITMA SORTING ===")

    for size in sizes:
        sorted_data = create_data(size)

        datasets = {
            "Best Case": sorted_data.copy(),
            "Average Case": sorted_data.copy(),
            "Worst Case": sorted_data[::-1]
        }

        rng.shuffle(datasets["Average Case"])

        print(f"\nUkuran data: {size} elemen")

        for algorithm_name, sorter in algorithms.items():
            print(f"\n{algorithm_name}:")

            for case_name, data in datasets.items():
                elapsed = measure_time(sorter, data)

                print(
                    f"  {case_name}: {elapsed:.8f} detik"
                )


if __name__ == "__main__":
    run_benchmark()
