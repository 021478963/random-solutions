import java.util.Arrays;

public class ClimbingStairs {
  /*
    sum n - 2, n - 1 since we can climb either one or two stairs.
  */
  public static void main(String[] args) {
    System.out.println(climbStairs(45));
  }

  public static int climbStairs(int n) {
    if (n < 4) {
      return n;
    }

    int last = 2;
    int first = 3;

    for (int i = 3; i < n; i++) {
      int temp = first;
      first += last;
      last = temp;
    }

    return first;

    // int[] memo = new int[n + 1];
    // Arrays.fill(memo, -1);
    // return climbStairs(n, memo);
  }

  public static int climbStairs(int n, int[] memo) {
    if (n < 3) {
      return n;
    } else if (memo[n] != -1) {
      return memo[n];
    }
    int result = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);
    memo[n] = result;
    return result;
  }
}
