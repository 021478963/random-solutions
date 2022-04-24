import java.util.LinkedList;
import java.util.List;

public class SpiralMatrix {

  public static void main(String[] args) {
    int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    List<Integer> result = spiralOrder(matrix);

    for (Integer i : result) {
      System.out.println(i);
    }
  }

  public static List<Integer> spiralOrder(int[][] matrix) {
    int yLength = matrix.length - 1;
    int xLength = matrix[0].length - 1;
    List<Integer> result = new LinkedList<Integer>();

    for (int i = 0; i <= xLength; i++) {
      result.add(matrix[0][i]);
    }
    int currentX = xLength;
    int currentY = 0;

    while (true) {

      if (yLength != 0) {
        int finalY = currentY + yLength;
        for (int i = currentY + 1; i <= finalY; i++) {
          result.add(matrix[i][currentX]);
        }
        currentY = finalY;
        yLength--;
      } else {
        break;
      }

      if (xLength != 0) {
        int finalX = currentX - xLength;
        for (int i = currentX - 1; i >= finalX; i--) {
          result.add(matrix[currentY][i]);
        }
        currentX = finalX;
        xLength--;
      } else {
        break;
      }

      if (yLength != 0) {
        int finalY = currentY - yLength;
        for (int i = currentY - 1; i >= finalY; i--) {
          result.add(matrix[i][currentX]);
        }
        currentY = finalY;
        yLength--;
      } else {
        break;
      }

      if (xLength != 0) {
        int finalX = currentX + xLength;
        for (int i = currentX + 1; i <= finalX; i++) {
          result.add(matrix[currentY][i]);
        }
        currentX = finalX;
        xLength--;
      } else {
        break;
      }

    }
    return result;
  }
}