import unittest
from bingo import bingo_p1, bingo_p2

class TestBingo(unittest.TestCase):
    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            bingo_p1('no_file.txt')
        with self.assertRaises(FileNotFoundError):
            bingo_p2('no_file.txt')

    def test_empty_file(self):
        with self.assertRaises(IndexError):
            bingo_p1('empty.txt')

    def test_invalid_board_size(self):
        with self.assertRaises(IndexError):
            bingo_p1('invalid.txt')

    def test_bingo_p1(self):
        self.assertTrue(bingo_p1('input1.txt'))

    def test_bingo_p2(self):
        self.assertEqual(bingo_p2('input1.txt'), 0)
        self.assertEqual(bingo_p2('input2.txt'), 2) 

if __name__ == '__main__':
    unittest.main()
