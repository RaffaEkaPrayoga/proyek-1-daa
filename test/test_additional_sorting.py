

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
