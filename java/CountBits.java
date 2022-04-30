public class CountBits {

  public int[] countBits(int n) {
    return countBits(n, new int[n + 1]);
  }

  public int[] countBits(int n, int[] memo) {
    if (n < 3) {
      memo[n] = n;
      return memo;
    } else {
      int[] result = countBits(n - 1, memo);
      int numZeros = 0;
      int number = n;
      while (number > 0) {
        numZeros += number % 2;
        number /= 2;
      }
      memo[n] = numZeros;
      return result;
    }a
  }
}
