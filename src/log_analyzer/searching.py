class LinearSearch:

    def search(self, logs: list, pattern: str) -> tuple[list[int], int]:
        results = []
        comparisons = 0

        if pattern == "":
            return results, comparisons

        for log in logs:
            found = False
            for i in range(len(log.content) - len(pattern) + 1):
                match = True
                for j in range(len(pattern)):
                    comparisons += 1
                    if log.content[i + j] != pattern[j]:
                        match = False
                        break
                if match:
                    found = True
                    break

            if found:
                results.append(log.line_number)

        return results, comparisons

class BinarySearch:
    def search(self, logs: list, pattern: str) -> tuple[list[int], int]:
        if pattern == "":
            return [], 0

        low = 0
        high = len(logs) - 1
        comparisons = 0
        found_index = -1

        # Temukan salah satu posisi yang berisi baris sama persis.
        while low <= high:
            mid = (low + high) // 2
            comparisons += 1

            if logs[mid].content == pattern:
                found_index = mid
                break
            elif logs[mid].content < pattern:
                low = mid + 1
            else:
                high = mid - 1

        if found_index == -1:
            return [], comparisons

        # Kumpulkan duplikat yang bersebelahan di sekitar posisi ditemukan.
        first = found_index
        while first > 0:
            comparisons += 1
            if logs[first - 1].content == pattern:
                first -= 1
            else:
                break

        last = found_index
        while last + 1 < len(logs):
            comparisons += 1
            if logs[last + 1].content == pattern:
                last += 1
            else:
                break

        line_numbers = [logs[i].line_number for i in range(first, last + 1)]
        line_numbers.sort()
        return line_numbers, comparisons
