
from .models import AnomalyResult


class BubbleSort:

    def sort(
        self,
        results: list[AnomalyResult]
    ) -> list[AnomalyResult]:

        data = results.copy()
        n = len(data)

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                a = (
                    data[j].frequency,
                    data[j].line_numbers[0]
                    if data[j].line_numbers else float("inf")
                )

                b = (
                    data[j + 1].frequency,
                    data[j + 1].line_numbers[0]
                    if data[j + 1].line_numbers else float("inf")
                )

                if a > b:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True

            if not swapped:
                break

        return data


class MergeSort:

    def sort(
        self,
        results: list[AnomalyResult]
    ) -> list[AnomalyResult]:

        if len(results) <= 1:
            return results.copy()

        mid = len(results) // 2

        left = self.sort(results[:mid])
        right = self.sort(results[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            key_left = (
                left[i].frequency,
                left[i].line_numbers[0]
                if left[i].line_numbers else float("inf")
            )

            key_right = (
                right[j].frequency,
                right[j].line_numbers[0]
                if right[j].line_numbers else float("inf")
            )

            if key_left <= key_right:
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
