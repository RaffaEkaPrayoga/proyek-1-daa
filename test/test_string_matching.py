from log_analyzer.string_matching import KMP


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


def test_empty_pattern():
    kmp = KMP()

    found, comparisons = kmp.search(
        "GET /index.html",
        ""
    )

    assert found is False
    assert comparisons == 0