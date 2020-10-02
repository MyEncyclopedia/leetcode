// AC
// Runtime: 1 ms, faster than 42.98% of Java online submissions for Pow(x, n).
// Memory Usage: 38.7 MB, less than 48.31% of Java online submissions for Pow(x, n).

class Solution {
    public double myPow(double x, int n) {
        double ret = 1.0;
        long i = Math.abs((long) n);
        while (i != 0) {
            if ((i & 1) > 0) {
                ret *= x;
            }
            x *= x;
            i = i >> 1;
        }

        return n < 0 ? 1.0 / ret : ret;
    }
}