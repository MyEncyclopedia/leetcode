/**
 * Result: AC
 * Method: Matrix Power Multiplication
 * Time Complexity: O(log(N))
 */
class Solution_509 {
    public int fib(int N) {
        if (N <= 1) {
            return N;
        }
        int[][] M = {{1, 1}, {1, 0}};
        // powers = M^(N-1)
        N--;
        int[][] powerDouble = M;
        int[][] powers = {{1, 0}, {0, 1}};
        while (N > 0) {
            if (N % 2 == 1) {
                powers = matrixProd(powers, powerDouble);
            }
            powerDouble = matrixProd(powerDouble, powerDouble);
            N = N / 2;
        }

        return powers[0][0];
    }

    public int[][] matrixProd(int[][] A, int[][] B) {
        int R = A.length;
        int C = B[0].length;
        int P = A[0].length;
        int[][] ret = new int[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                for (int p = 0; p < P; p++) {
                    ret[r][c] += A[r][p] * B[p][c];
                }
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        Solution_509 s = new Solution_509();
        System.out.println(s.fib(4));
    }
}
