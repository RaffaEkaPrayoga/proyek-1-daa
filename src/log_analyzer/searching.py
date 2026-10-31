
class LinearSearch:

    def search(
        self,
        logs: list,
        pattern: str
    ) -> list[int]:

        results = []
        comparisons = 0

        for log in logs:
            if pattern == "":
                break

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
