/**
 * Result: AC
 * Method: Markov Chain, Matrix Multiplication
 * Time Complexity: O(10*N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

class Solution_935_MatrixProduct {
    public int knightDialer(int N) {
        long MOD = 1000000007;

        long[][] transMatrix = {
                {0, 0, 0, 0, 1, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 1, 0},
                {0, 0, 0, 0, 0, 0, 0, 1, 0, 1},
                {0, 0, 0, 0, 1, 0, 0, 0, 1, 0},
                {1, 0, 0, 1, 0, 0, 0, 0, 0, 1},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {1, 1, 0, 0, 0, 0, 0, 1, 0, 0},
                {0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 1, 0, 0, 0, 0, 0},
        };
        long[][] countStates = new long[1][10];
        Arrays.fill(countStates[0], 1);
        for (int i = 1; i < N; i++) {
            countStates = matrixProd(countStates, transMatrix, MOD);
        }

        long ret = 0;
        for (int i = 0; i < 10; i++) {
            ret += countStates[0][i];
        }
        return (int) (ret % MOD);
    }

    public long[][] matrixProd(long[][] A, long[][] B, long MOD) {
        long[][] ret = new long[A.length][10];
        for (int r = 0; r < A.length; r++) {
            for (int c = 0; c < 10; c++) {
                for (int k = 0; k < 10; k++) {
                    ret[r][c] += A[r][k] * B[k][c];
                    ret[r][c] = ret[r][c] % MOD;
                }
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        Solution_935_MatrixProduct s = new Solution_935_MatrixProduct();
        System.out.println(s.knightDialer(3));
    }
}