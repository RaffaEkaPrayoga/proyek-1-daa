from pathlib import Path
from .log_reader import LogReader
from .analyzer import (
    LogAnalyzer,
    total_frequency_iterative,
    total_frequency_recursive
)


def get_patterns():
    print("\n=== INPUT POLA ANOMALI ===")

    while True:
        try:
            k = int(input("Masukkan jumlah pola (k): "))

            if k <= 0:
                print("Jumlah pola harus lebih dari 0!")
                continue

            break

        except ValueError:
            print("Input harus berupa angka!")

    patterns = []

    for i in range(k):
        while True:
            pattern = input(
                f"Masukkan pola ke-{i + 1}: "
            ).strip()

            if not pattern:
                print("Pola tidak boleh kosong!")
                continue

            patterns.append(pattern)
            break

    return patterns


def main():

    print("=== SERVER LOG ANOMALY DETECTION ===")

    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "server.log"

    # 1. Membaca dataset log
    reader = LogReader()
    logs = reader.read(file_path)

    print(f"\nTotal baris log: {len(logs)}")

    # 2. Memasukkan pola pencarian
    patterns = get_patterns()

    # 3. Melakukan analisis
    analyzer = LogAnalyzer()

    results, comparisons = analyzer.analyze(
        logs,
        patterns
    )

    # 4. Menampilkan laporan
    print(
        "\n=== LAPORAN ANOMALI LOG SERVER "
        "(TERURUT DARI PALING LANGKA) ==="
    )

    for index, result in enumerate(results, start=1):

        first_line = (
            result.line_numbers[0]
            if result.line_numbers
            else "-"
        )

        print(f'\n{index}. Pola: "{result.pattern}"')
        print(f"   Nomor Baris Pertama: {first_line}")
        print(f"   Frekuensi: {result.frequency}")

    # 5. Menampilkan metrik
    print("\nMetrik Eksekusi:")
    print(
        "- Total Operasi Dasar "
        f"(Perbandingan Karakter): {comparisons} operasi"
    )

    # 6. Membandingkan pendekatan iteratif dan rekursif
    iterative_total = total_frequency_iterative(results)
    recursive_total = total_frequency_recursive(results)

    print("\n=== PERBANDINGAN ITERASI DAN REKURSI ===")
    print(f"Total frekuensi (Iteratif): {iterative_total}")
    print(f"Total frekuensi (Rekursif): {recursive_total}")


if __name__ == "__main__":
    main()