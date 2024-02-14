from collections.abc import Iterable


def gcd(n: int, m: int) -> int:
    """ The greatest common divisor

    Args:
        n (int): any integer 
        m (int): any integer

    Returns:
        int: the greatest common divisor of n and m

    Raises:
        ValueError: if both n and m are zero
    """

    if m == 0:
        if n == 0:
            raise ValueError('There is no greatest divisor of zero.')
        return abs(n)
    return gcd(m, n % m)

def eea_backtrack_handler(x: int, y: int) -> Iterable[int]:
    """ A helper function for implementing the extended euclidean algorithm

    Args:
        x (int): any non-zero integer
        y (int): any integer such that x and y are coprime

    Returns:
        int, int: a pair of values a, b, such that ax + by = 1
    """
    q = x // y
    r = x % y
    assert x == y * q + r
    if r == 1:
        a = 1
        b = -q
    else:
        a_, b_ = eea_backtrack_handler(y, r)
        assert 1 == a_ * y + b_ * r 
        a, b = b_, a_ - b_ * q


    assert 1 == a * x + b * y
    return a, b


def modinv(r: int, m: int) -> int:
    if gcd(r, m) != 1:
        raise ValueError('The first and second arguments are not coprime.')
    _, b = eea_backtrack_handler(m, r)
    return b % m

def modexp(x, p, m):
    if p is 0:
        return 1
    if p % 2:
        return x * modexp(x, p - 1, m) % m
    return modexp(x, p >> 1, m) ** 2 % m
        
