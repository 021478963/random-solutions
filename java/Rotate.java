public class Rotate {
  
  public void rotate(int[][] matrix) {
    int length = matrix.length - 1;

    for (int n = 0; n < length / 2; n++) {
      int currentLength = length - 2 * n;
      for (int i = 0; i < currentLength; i++) {
        int temp = matrix[n][n + i];

        matrix[n][n + i] = matrix[currentLength - i + n][n];
        matrix[currentLength - i + n][n] = matrix[n + currentLength][currentLength + n - i];
        matrix[n + currentLength][currentLength + n - i] = matrix[n + i][n + currentLength];
        matrix[n + i][n + currentLength] = temp;
      }
    }
  }
}
