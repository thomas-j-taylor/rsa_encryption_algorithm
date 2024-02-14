import unittest
from src.padding_scheme import add_padding, remove_padding

class TestPadding(unittest.TestCase):
    def test_add_then_remove_padding(self):
        data = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        padded_data = add_padding(data)
        self.assertEqual(data, remove_padding(padded_data))

if __name__ == "__main__":
    unittest.main()
