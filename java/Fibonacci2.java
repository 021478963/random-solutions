import java.util.Arrays;

public class Fibonacci2 {
  
  static int[] memo = new int[100];
  public static void main(String[] args) {
    System.out.println(fib(40));
  }

  static int fib(int n) {
    int[] memo = new int[100];
    Arrays.fill(memo, -1);
    return fib(n, memo);
  }

  static int fib(int n, int[] memo) {
    if (memo[n] > 0) {
      return memo[n];
    }

    if (n < 3) {
      memo[n] = 1;
      return 1;
    } else {
      memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
      return memo[n]; 
    }
  }
}
