class Solution {
  public int integerBreak(int n) {
      if (n == 3) {
          return 2;
      }
      int[] memo = new int[n + 1];
      return integerBreak(n, memo);
  }
  
  public int integerBreak(int n, int[] memo) {
      if (memo[n] != 0) {
          return memo[n];
      } else if (n <= 2) {
          memo[n] = 1;
          return 1;
      } else {
          int max = 0;
          for (int i = 1; i <= n; i++) {
              int result = integerBreak(n - i, memo) * i;
              if (memo[n - i] == 0) {
                  memo[n - i] = result / i;
              }
              System.out.println(i + " " + result);
              max = Math.max(max, result);
          }
          memo[n] = max;
          return max;
      }
  }
}