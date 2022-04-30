import java.util.Arrays;

public class UniquePathsTabulated {
  
  public int uniquePaths(int m, int n) {
    int[][] result = new int[m + 1][n + 1];
    for (int[] i : result) {
      Arrays.fill(i, 0);
    }
    result[1][1] = 1;
    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        result[i][j] = result[i - 1][j] + result[i][j - 1];
      }
    }
    return result[m][n];
  }
}
