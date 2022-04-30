import java.lang.Math;

public class CountBitsOptimized {

  public int[] countBits(int n) {
    int[] result = new int[n + 1];
    int power = 0;
    int currentBase = 1;
    int current = 0;

    for (int i = 1; i < result.length; i++) {
      current = i;
      if (current >= currentBase * 2) {
        currentBase *= 2;
      }
      current -= currentBase;
      System.out.println(i + ", " + current + ", " + power);
      result[i] = 1 + result[current];
    }

    return result;
  }
}
