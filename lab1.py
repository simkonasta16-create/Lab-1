class MatrixProcessor:
    def execute(self):
        try:
            matrix_a = [
                [1.5, 2.0, 3.2, 5.6, 7.7, 8.9],
                [4.0, 5.5, 6.1, 3.2, 6.7, 9.1],
                [6.0, 1.5, 4.1, 8.2, 9.7, 7.5],
                [9.4, 5.7, 6.6, 3.1, 8.7, 6.1]
            ]

            matrix_b = [
                [7.0, 8.2, 9.0, 5.5],
                [9.1, 1.0, 3.2, 6.3],
                [2.5, 4.6, 5.5, 7.8],
                [1.5, 6.6, 9.6, 3.8],
                [6.5, 8.8, 9.9, 7.9],
                [8.5, 7.6, 4.5, 3.3]
            ]

            print("Матриця A:")
            self._print_matrix(matrix_a)
            print("\nМатриця B:")
            self._print_matrix(matrix_b)


            matrix_c = self._multiply_matrices(matrix_a, matrix_b)
            print("\nМатриця C = A × B")
            self._print_matrix(matrix_c)

            averages = self._calculate_column_averages(matrix_c)
            print("\nСереднє значення кожного стовпчика")
            for i, avg in enumerate(averages):
                print(f"Стовпчик {i + 1}: {avg:.1f}")


        except ValueError as ve:
            print(f"Помилка значень: {ve}")
        except TypeError as te:
            print(f"Помилка типу даних: {te}")
        except IndexError:
            print("Помилка: Матриця має некоректну структуру (неоднакова довжина рядків).")
        except Exception as e:
            print(f"Виникла непередбачена помилка: {e}")

    def _multiply_matrices(self, a, b):
        rows_a = len(a)
        cols_a = len(a[0])
        rows_b = len(b)
        cols_b = len(b[0])

        if cols_a != rows_b:
            raise ValueError(f"Неможливо перемножити: кількість стовпців A ({cols_a}) "
                             f"не дорівнює кількості рядків B ({rows_b}).")

        result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    if not isinstance(a[i][k], float) or not isinstance(b[k][j], float):
                        raise TypeError("Елементи матриці повинні бути числами (double/float).")
                    result[i][j] += a[i][k] * b[k][j]

        return result

    def _calculate_column_averages(self, matrix):

        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        averages = []

        for j in range(cols):
            col_sum = sum(matrix[i][j] for i in range(rows))
            averages.append(col_sum / rows)

        return averages

    def _print_matrix(self, matrix):

        for row in matrix:
            print([f"{val:.1f}" for val in row])

if __name__ == "__main__":
    processor = MatrixProcessor()
    processor.execute()
    