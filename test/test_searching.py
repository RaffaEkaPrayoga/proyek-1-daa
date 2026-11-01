
from log_analyzer.searching import LinearSearch, BinarySearch
from log_analyzer.models import LogEntry


def test_linear_search_found():
    logs = [
        LogEntry(1, "GET /index.html"),
        LogEntry(2, "POST /healthcheck"),
        LogEntry(3, "GET /login"),
    ]

    search = LinearSearch()
    results, comparisons = search.search(logs, "POST /healthcheck")

    assert results == [2]
    assert comparisons > 0


def test_linear_search_not_found():
    logs = [
        LogEntry(1, "DELETE /index.html"),
        LogEntry(2, "DELETE /login"),
    ]

    search = LinearSearch()
    results, comparisons = search.search(logs, "POST /healthcheck")

    assert results == []
    assert comparisons > 0


def test_linear_search_empty_pattern():
    logs = [LogEntry(1, "GET /index.html")]

    search = LinearSearch()
    results, comparisons = search.search(logs, "")

    assert results == []
    assert comparisons == 0


def test_binary_search_found():
    # Data harus diurutkan berdasarkan content.
    logs = [
        LogEntry(3, "GET /admin"),
        LogEntry(1, "GET /health"),
        LogEntry(2, "POST /login"),
        LogEntry(4, "POST /login"),
    ]

    search = BinarySearch()
    results, comparisons = search.search(logs, "POST /login")

    assert results == [2, 4]
    assert comparisons > 0


def test_binary_search_not_found():
    logs = [
        LogEntry(1, "GET /admin"),
        LogEntry(2, "GET /health"),
        LogEntry(3, "POST /login"),
    ]

    search = BinarySearch()
    results, comparisons = search.search(logs, "DELETE /data")

    assert results == []
    assert comparisons > 0


def test_binary_search_empty_pattern():
    logs = [LogEntry(1, "GET /index.html")]

    search = BinarySearch()
    results, comparisons = search.search(logs, "")

    assert results == []
    assert comparisons == 0

def test_binary_search_many_duplicate_logs():
    logs = [
        LogEntry(5, "GET /admin"),
        LogEntry(2, "POST /login"),
        LogEntry(8, "POST /login"),
        LogEntry(1, "POST /login"),
        LogEntry(9, "POST /logout"),
        LogEntry(4, "POST /login"),
    ]

    # Binary Search membutuhkan data terurut berdasarkan content.
    logs.sort(key=lambda log: log.content)

    search = BinarySearch()
    results, comparisons = search.search(logs, "POST /login")

    assert results == [1, 2, 4, 8]
    assert comparisons > 0


def test_linear_search_multiple_occurrences_in_one_line():
    logs = [
        LogEntry(
            7,
            "POST /healthcheck POST /healthcheck POST /healthcheck"
        )
    ]

    search = LinearSearch()
    results, comparisons = search.search(
        logs,
        "POST /healthcheck"
    )

    assert results == [7]
    assert comparisons > 0