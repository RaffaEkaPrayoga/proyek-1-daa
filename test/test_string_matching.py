from log_analyzer.string_matching import KMP
from log_analyzer.string_matching import BoyerMoore

def test_pattern_found():
    kmp = KMP()

    found, comparisons = kmp.search(
        "GET /index.html POST /healthcheck",
        "POST /healthcheck"
    )

    assert found is True
    assert comparisons > 0


def test_pattern_not_found():
    kmp = KMP()

    found, comparisons = kmp.search(
        "GET /index.html",
        "POST /healthcheck"
    )

    assert found is False
    assert comparisons > 0

def test_kmp_multiple_occurrences_in_one_line():
    kmp = KMP()

    found, comparisons = kmp.search(
        "POST /healthcheck POST /healthcheck POST /healthcheck",
        "POST /healthcheck"
    )

    assert found is True
    assert comparisons > 0

def test_boyer_moore_pattern_found():
    bm = BoyerMoore()

    found, comparisons = bm.search(
        "GET /index.html POST /healthcheck",
        "POST /healthcheck"
    )

    assert found is True
    assert comparisons > 0


def test_boyer_moore_pattern_not_found():
    bm = BoyerMoore()

    found, comparisons = bm.search(
        "DELETE /index.html",
        "POST /healthcheck"
    )

    assert found is False
    assert comparisons > 0


def test_boyer_moore_empty_pattern():
    bm = BoyerMoore()

    found, comparisons = bm.search(
        "GET /index.html",
        ""
    )

    assert found is False
    assert comparisons == 0


def test_boyer_moore_pattern_longer_than_text():
    bm = BoyerMoore()

    found, comparisons = bm.search(
        "GET",
        "POST /healthcheck"
    )

    assert found is False
    assert comparisons == 0

def test_empty_pattern():
    kmp = KMP()

    found, comparisons = kmp.search(
        "GET /index.html",
        ""
    )

    assert found is False
    assert comparisons == 0

def test_boyer_moore_multiple_occurrences_in_one_line():
    bm = BoyerMoore()

    found, comparisons = bm.search(
        "POST /healthcheck POST /healthcheck POST /healthcheck",
        "POST /healthcheck"
    )

    assert found is True
    assert comparisons > 0