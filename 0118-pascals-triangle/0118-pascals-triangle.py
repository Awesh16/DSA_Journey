class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            # 1. Create a new row filled with 1s.
            # Row 0 has 1 element, Row 1 has 2 elements, Row 2 has 3, etc.
            row = [1] * (i + 1)

            # 2. Modify the "inner" numbers (everything between the first and last 1)
            # We start from index 1 and stop before the last index.
            for j in range(1, i):
                # The value is the sum of the two values in the PREVIOUS row
                # triangle[i-1] is the row above
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            # 3. Add the finished row to the big list
            triangle.append(row)

        return triangle
        