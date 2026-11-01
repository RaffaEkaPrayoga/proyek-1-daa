

import pytest

from log_analyzer.models import AnomalyResult
from log_analyzer.sorting import (
    BubbleSort,
    SelectionSort,
    InsertionSort,
    MergeSort,
)


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_algorithms(algorithm):
    data = [
        AnomalyResult("/login", [2, 4, 6, 8, 10]),
        AnomalyResult("/admin", [3, 7]),
        AnomalyResult("/error", [1, 5, 9, 11, 13, 15, 17, 19]),
        AnomalyResult("/api", [1, 4]),
    ]

    result = algorithm.sort(data)

    expected = ["/api", "/admin", "/login", "/error"]
    actual = [item.pattern for item in result]

    assert actual == expected


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_empty_data(algorithm):
    result = algorithm.sort([])

    assert result == []


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_single_data(algorithm):
    data = [AnomalyResult("/login", [1])]

    result = algorithm.sort(data)

    assert len(result) == 1
    assert result[0].pattern == "/login"


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_already_sorted_data(algorithm):
    data = [
        AnomalyResult("/a", [1]),
        AnomalyResult("/b", [2, 3]),
        AnomalyResult("/c", [4, 5, 6]),
        AnomalyResult("/d", [7, 8, 9, 10]),
    ]

    result = algorithm.sort(data)

    expected = ["/a", "/b", "/c", "/d"]
    actual = [item.pattern for item in result]

    assert actual == expected


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_reverse_order_data(algorithm):
    data = [
        AnomalyResult("/d", [7, 8, 9, 10]),
        AnomalyResult("/c", [4, 5, 6]),
        AnomalyResult("/b", [2, 3]),
        AnomalyResult("/a", [1]),
    ]

    result = algorithm.sort(data)

    expected = ["/a", "/b", "/c", "/d"]
    actual = [item.pattern for item in result]

    assert actual == expected


@pytest.mark.parametrize(
    "algorithm",
    [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        MergeSort(),
    ],
)
def test_sorting_same_frequency_and_first_line(algorithm):
    data = [
        AnomalyResult("/alpha", [1, 5]),
        AnomalyResult("/beta", [1, 7]),
        AnomalyResult("/gamma", [3]),
        AnomalyResult("/delta", [1, 9]),
    ]

    result = algorithm.sort(data)

    # Gamma memiliki frekuensi lebih kecil.
    assert result[0].pattern == "/gamma"

    # Tiga pola lainnya memiliki frekuensi dan nomor baris
    # pertama yang sama.
    same_key_patterns = {
        item.pattern for item in result[1:]
    }

    assert same_key_patterns == {
        "/alpha",
        "/beta",
        "/delta",
    }

    # Memastikan seluruh data tetap dipertahankan.
    assert len(result) == len(data)