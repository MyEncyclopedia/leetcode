
/**
 * Result: AC
 * Method: DP
 * Time Complexity: O(10*N)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

class Solution_935 {
    public int knightDialer(int N) {
        long MOD = 1000000007;
        int[][] transitions = new int[][]{
                {4, 6}, // 0 => 4, 6
                {6, 8}, // 1 => 6, 8
                {7, 9}, // 2
                {4, 8}, // 3
                {3, 9, 0}, // 4
                {},    // 5
                {1, 7, 0}, // 6
                {2, 6}, // 7
                {1, 3}, // 8
                {2, 4}  // 9
        };
        long dp[] = new long[10];
        Arrays.fill(dp, 1);

        long[] temp = new long[10];
        for (int i = 1; i < N; i++) {
            Arrays.fill(temp, 0);
            for (int s = 0; s < 10; s++) {  // s => t
                for (int t : transitions[s]) {
                    temp[t] += dp[s];
                }
            }
            for (int s = 0; s < 10; s++) {
                dp[s] = temp[s] % MOD;
            }
        }

        long ret = 0;
        for (int i = 0; i < 10; i++) {
            ret += dp[i];
        }
        return (int) (ret % MOD);
    }

    public static void main(String[] args) {
        Solution_935 s = new Solution_935();
        System.out.println(s.knightDialer(161));
    }
}