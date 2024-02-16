from random import randint

from .keys import Key
from .modular_arithmetic import gcd, modinv

def generate_key_pair(prime_1, prime_2):

    modulus = prime_1 * prime_2
    totient = (prime_1 - 1) * (prime_2 - 1)

    public_exponent = 0
    while gcd(public_exponent,totient) != 1:
        public_exponent = randint(1,totient)

    public_key = Key(exponent=public_exponent,modulus=modulus)
    private_key = Key(exponent=modinv(public_exponent,totient), modulus=modulus)

    return public_key, private_key

