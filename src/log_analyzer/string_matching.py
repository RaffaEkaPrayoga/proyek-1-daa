class KMP:
    def build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                i += 1

        return lps

    def search(
        self,
        text: str,
        pattern: str,
        lps: list[int] | None = None
    ) -> tuple[bool, int]:
        if not pattern:
            return False, 0

        if lps is None:
            lps = self.build_lps(pattern)

        i = 0
        j = 0
        comparisons = 0

        while i < len(text):
            comparisons += 1

            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    return True, comparisons
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1

        return False, comparisons


class BoyerMoore:
    """
    Boyer-Moore dengan aturan bad-character.

    Mengembalikan True jika pattern ditemukan, False jika tidak,
    beserta jumlah perbandingan karakter.
    """

    def build_last_occurrence(self, pattern: str) -> dict[str, int]:
        last = {}
        for index, char in enumerate(pattern):
            last[char] = index
        return last

    def search(self, text: str, pattern: str) -> tuple[bool, int]:
        if not pattern:
            return False, 0

        last = self.build_last_occurrence(pattern)
        n = len(text)
        m = len(pattern)
        shift = 0
        comparisons = 0

        while shift <= n - m:
            j = m - 1

            # Boyer-Moore membandingkan karakter dari kanan ke kiri.
            while j >= 0:
                comparisons += 1
                if pattern[j] != text[shift + j]:
                    break
                j -= 1

            if j < 0:
                return True, comparisons

            mismatched_char = text[shift + j]
            last_index = last.get(mismatched_char, -1)
            shift += max(1, j - last_index)

        return False, comparisons
