from .log_reader import LogReader
from .analyzer import (
    LogAnalyzer,
    total_frequency_iterative,
    total_frequency_recursive
)


def get_patterns():

    print("\n=== INPUT POLA ANOMALI ===")

    k = int(input("Masukkan jumlah pola (k): "))

    patterns = []

    for i in range(k):
        pattern = input(f'Masukkan pola ke-{i + 1}: ').strip()

        if not pattern:
            print("Pola tidak boleh kosong!")
            return get_patterns()

        patterns.append(pattern)

    return patterns


def main():

    print("=== SERVER LOG ANOMALY DETECTION ===")

    file_path = "data/server.log"

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
        print(f"   Indeks Pertama: {first_line}")
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