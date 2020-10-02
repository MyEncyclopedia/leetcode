
/**
AC
Runtime: 0 ms, faster than 100.00% of Java online submissions for Number of Ways to Paint N × 3 Grid.
Memory Usage: 35.7 MB, less than 97.21% of Java online submissions for Number of Ways to Paint N × 3 Grid.
**/

class Solution {
    public int numOfWays(int n) {
        long MOD = (long) (1e9 + 7);
        long[][] ret = {{6, 6}};
        long[][] m = {{3, 2}, {2, 2}};
        n -= 1;
        while(n > 0) {
            if ((n & 1) > 0) {
                ret = matrixProd(ret, m, MOD);
            }
            m = matrixProd(m, m, MOD);
            n >>= 1;
        }
        return (int) ((ret[0][0] + ret[0][1]) % MOD);

    }

    public long[][] matrixProd(long[][] A, long[][] B, long MOD) {
        int R = A.length;
        int C = B[0].length;
        int P = A[0].length;
        long[][] ret = new long[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                for (int p = 0; p < P; p++) {
                    ret[r][c] += A[r][p] * B[p][c];
                    ret[r][c] = ret[r][c] % MOD;
                }
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.numOfWays(3));
    }
}