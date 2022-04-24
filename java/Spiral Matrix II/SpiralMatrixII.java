public class SpiralMatrixII {
  
  public static void main(String[] args) {
    int[][] result = generateMatrix(3);

    for (int i = 0; i < result.length; i++) {
      for (int j = 0; j < result[0].length; j++) {
        System.out.print(result[i][j] + "\t");
      }
      System.out.println();
    }
  }

  public static int[][] generateMatrix(int n) {
    int[][] result = new int[n][n];
    int count = 1;
    int length = n - 1;
    int currentX = length;
    int currentY = 0;

    int temp;

    for (int i = 0; i < n; i++) {
      result[0][i] = count;
      count++;
    }

    while (length >= 1) {
      temp = currentY + length;
      for (int i = currentY + 1; i <= temp; i++) {
        result[i][currentX] = count;
        count++;
      }
      currentY = temp;

      temp = currentX - length;
      for (int i = currentX - 1; i >= temp; i--) {
        result[currentY][i] = count;
        count++;
      }
      currentX = temp;

      length--;

      temp = currentY - length;
      for (int i = currentY - 1;  i >= temp; i--) {
        result[i][currentX] = count;
        count++;
      }
      currentY = temp;

      temp = currentX + length;
      for (int i = currentX + 1; i <= temp; i++) {
        result[currentY][i] = count;
        count++;
      }
      currentX = temp;

      length--;
    }

    return result;
  }
}
