import unittest
from lab1 import MatrixProcessor

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.processor = MatrixProcessor()

    def test_multiplication_success(self):
        a = [[1.0, 2.0], [3.0, 4.0]]
        b = [[2.0, 0.0], [1.0, 2.0]]
        expected = [[4.0, 4.0], [10.0, 8.0]]
        result = self.processor._multiply_matrices(a, b)
        self.assertEqual(result, expected)

    def test_dimension_mismatch(self):
        a = [[1.0, 2.0]]
        b = [[1.0], [2.0], [3.0]]
        with self.assertRaises(ValueError):
            self.processor._multiply_matrices(a, b)

    def test_column_averages(self):
        matrix = [
            [10.0, 20.0],
            [30.0, 40.0]
        ]
        expected = [20.0, 30.0]
        result = self.processor._calculate_column_averages(matrix)
        self.assertEqual(result, expected)

    def test_invalid_data_type(self):
        a = [["string", 2.0]]
        b = [[1.0], [2.0]]
        with self.assertRaises(TypeError):
            self.processor._multiply_matrices(a, b)

if __name__ == "__main__":
    unittest.main()