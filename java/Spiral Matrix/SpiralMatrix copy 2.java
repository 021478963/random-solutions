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

    for (int i = 0; i < xLength; i++) {
      result.add(matrix[0][i]);
    }
    int currentX = xLength;
    int currentY = 0;

    while (true) {

      System.out.println("yLength is: " + yLength);

      if (yLength != 0) {
        int finalY = currentY + yLength;
        for (int i = currentY; i < finalY; i++) {
          System.out.println("direction: y down current int: " + matrix[i][currentX]);
          result.add(matrix[i][currentX]);
        }
        currentY = finalY;
        yLength = yLength - 1;
      } else {
        break;
      }

      System.out.println("xLength is : " + xLength);

      if (xLength != 0) {
        int finalX = currentX - xLength;
        for (int i = currentX; i > finalX; i--) {
          System.out.println("direction: x left current int: " + matrix[currentY][i]);
          result.add(matrix[currentY][i]);
        }
        currentX = finalX;
        xLength = xLength - 1;
      } else {
        break;
      }

      System.out.println("yLength is : " + yLength);

      if (yLength != 0) {
        int finalY = currentY - yLength;
        for (int i = currentY; i > finalY; i--) {
          System.out.println("direction: y up current int: " + matrix[i][currentX]);
          result.add(matrix[i][currentX]);
        }
        currentY = finalY;
        yLength = yLength - 1;
      } else {
        break;
      }

      System.out.println("xLength is : " + xLength);

      if (xLength != 0) {
        int finalX = currentX + xLength;
        for (int i = currentX; i < finalX; i++) {
          System.out.println("direction: x right current int: " + matrix[currentY][i]);
          result.add(matrix[currentY][i]);
        }
        currentX = finalX;
        xLength = xLength - 1;
      } else {
        break;
      }

    }
    return result;
  }
}