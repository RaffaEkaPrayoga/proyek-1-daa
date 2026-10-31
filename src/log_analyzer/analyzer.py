from .models import AnomalyResult
from .string_matching import KMP
from .sorting import MergeSort


class LogAnalyzer:
    def __init__(self):
        self.matcher = KMP()
        self.sorter = MergeSort()

    def analyze(self, logs, patterns):
        results = []
        total_comparisons = 0

        for pattern in patterns:
            anomaly = AnomalyResult(pattern=pattern)
            lps = self.matcher.build_lps(pattern)

            for log in logs:
                found, comparisons = self.matcher.search(
                    log.content, pattern, lps
                )

                total_comparisons += comparisons

                if found:
                    anomaly.line_numbers.append(log.line_number)

            results.append(anomaly)

        sorted_results = self.sorter.sort(results)

        return sorted_results, total_comparisons


def total_frequency_iterative(results):
    total = 0

    for result in results:
        total += result.frequency

    return total


def total_frequency_recursive(results, index=0):
    if index >= len(results):
        return 0

    return (
        results[index].frequency
        + total_frequency_recursive(results, index + 1)
    )