
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

    def search(self, text, pattern, lps=None):

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
