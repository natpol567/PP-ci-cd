import pytest
from src.utils import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
        (4, 5, 9),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, -1),
        (2, 3, -1),
        (3, 4, -1),
        (4, 5, -1),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (2, 3, 6),
        (3, 4, 12),
        (4, 5, 20),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 0.5),
        (3, 4, 0.75),
        (4, 5, 0.8),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)
