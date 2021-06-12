import unittest
import os

from enkryptor.enkryptor import Enkryptor


class TestingSuite(unittest.TestCase):
    def setUp(self):
        self.enc = Enkryptor()

        self.test_set = {"list": ['a', 'b', 'c', 2, 5, 1, ['hello', 'world']],
                         "number": 3.14159265359,
                         "string": "The big brown fox jumps over the lazy dog",
                         "dict": {"hello": "world",
                                  "foo": "bar"}}

        self.fail_set = ("this is prob not gonna work", "haha")

        self.password = "javasucks"

    def test_all(self):
        # I wanted to make separate tests but all depend on each other
        self.assertIsNone(self.enc.password(self.password))
        self.enc.enkrypt(self.test_set)
        self.assertEqual(self.enc.dekrypt(), self.test_set)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertIsNone(self.enc.password(self.password))
        self.enc.enkrypt(self.fail_set)
        self.assertEqual(self.enc.dekrypt(), self.fail_set)

    def test_reload(self):
        # Simulates saving, ending program, then attempting to read contents in another session
        self.assertIsNone(self.enc.password(self.password))
        self.enc.enkrypt(self.test_set)

        self.enc2 = Enkryptor()
        self.assertTrue(self.enc2.password(self.password))
        self.assertEqual(self.enc2.dekrypt(), self.test_set)

    def tearDown(self):
        os.remove("enc.e")
        os.remove("salt.salt")


if __name__ == '__main__':
    unittest.main()
