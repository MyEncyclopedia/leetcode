
/**
 * Result: AC
 * Method: Markov Chain, Power Matrix Multiplication
 * Time Complexity: O(10*log(N))
 * Space Complexity: O(1)
 */

import java.util.Arrays;

class Solution_935_MatrixPowerProduct {
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
        // countState * transMatrix ^ (N-1)
        long[][] countStates = new long[1][10];
        Arrays.fill(countStates[0], 1);

        N--;
        // transMatrix^(N-1)
        long[][] powerDouble = transMatrix;
        long[][] powers = {
                {1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
        };
        while (N > 0) {
            if (N % 2 == 1) {
                powers = matrixProd(powers, powerDouble, MOD);
            }
            powerDouble = matrixProd(powerDouble, powerDouble, MOD);
            N = N / 2;
        }
        countStates = matrixProd(countStates, powers, MOD);

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
        Solution_935_MatrixPowerProduct s = new Solution_935_MatrixPowerProduct();
        System.out.println(s.knightDialer(3));
    }
}