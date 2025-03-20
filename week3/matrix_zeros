def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        m = len(mat[0])

        c0 = 1
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:

                    # mark i-th row
                    mat[i][0] = 0

                    # mark j-th column
                    if j == 0:
                        c0 = 0
                    else:
                        mat[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        if mat[0][0] == 0:
            for j in range(m):
                mat[0][j] = 0

        if c0 == 0:
            for i in range(n):
                mat[i][0] = 0
            