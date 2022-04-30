import java.util.Arrays;

public class Fibonacci3 {
  public static void main(String[] args) {
    System.out.println(fib(20));
  }

  // static int fib(int n) {
  //   int[] memo = new int[100];
  //   Arrays.fill(memo, -1);
  //   return fib(n, memo);
  // }

  // static int fib(int n, int[] memo) {
  //   if (memo[n] > 0) {
  //     return memo[n];
  //   }

  //   if (n < 3) {
  //     memo[n] = 1;
  //     return 1;
  //   } else {
  //     memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
  //     return memo[n]; 
  //   }
  // }

  static int fib(int n) {
    if (n == 0) {
      return 0;
    }
    
    int last = 1;
    int current = 1;
    for (int i = 2; i < n; i++) {
      int temp = current;
      current = current + last;
      last = temp;
    }

    return current;
  }
}
