import unittest
from src.modular_arithmetic import modexp
from src.padding_scheme import add_padding, remove_padding
from src.key_pair_generation import generate_key_pair

class all_tests(unittest.TestCase):
    def test_add_then_remove_padding(self):
        data = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        padded_data = add_padding(data)
        self.assertEqual(data, remove_padding(padded_data))

    def test_keypairs_are_exponential_inverses(self):
        secret = 10
        p = 47658357278109465265176598193
        q = 94654050923946523659138659165509634204093
        pub, priv = generate_key_pair(p,q)
        hidden_secret = modexp(secret,pub.exponent,p*q)
        self.assertEqual(secret, modexp(hidden_secret,priv.exponent,p*q))


if __name__ == "__main__":
    unittest.main()
