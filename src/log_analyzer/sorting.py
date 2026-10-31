from .models import AnomalyResult


def _sort_key(item: AnomalyResult) -> tuple[int, float]:
    first_line = item.line_numbers[0] if item.line_numbers else float("inf")
    return item.frequency, first_line


class BubbleSort:
    def sort(self, results: list[AnomalyResult]) -> list[AnomalyResult]:
        data = results.copy()
        n = len(data)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if _sort_key(data[j]) > _sort_key(data[j + 1]):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break

        return data


class SelectionSort:
    def sort(self, results: list[AnomalyResult]) -> list[AnomalyResult]:
        data = results.copy()
        n = len(data)

        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if _sort_key(data[j]) < _sort_key(data[min_index]):
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

        return data


class InsertionSort:
    def sort(self, results: list[AnomalyResult]) -> list[AnomalyResult]:
        data = results.copy()

        for i in range(1, len(data)):
            current = data[i]
            current_key = _sort_key(current)
            j = i - 1

            while j >= 0 and _sort_key(data[j]) > current_key:
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = current

        return data


class MergeSort:
    def sort(self, results: list[AnomalyResult]) -> list[AnomalyResult]:
        if len(results) <= 1:
            return results.copy()

        mid = len(results) // 2
        left = self.sort(results[:mid])
        right = self.sort(results[mid:])
        return self.merge(left, right)

    def merge(
        self,
        left: list[AnomalyResult],
        right: list[AnomalyResult]
    ) -> list[AnomalyResult]:
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if _sort_key(left[i]) <= _sort_key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result
