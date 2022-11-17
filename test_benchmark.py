import random
import string
import rust_int


def count_doubles_once(val):
    total = 0
    chars = iter(val)
    c1 = next(chars)
    for c2 in chars:
        if c1 == c2:
            total += 1
        c1 = c2
    return total


def test_python_func(benchmark):
    val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

    benchmark(count_doubles_once, val)

    assert True


def test_rust_func(benchmark):
    val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

    benchmark(rust_int.count_doubles_once, val)

    assert True
