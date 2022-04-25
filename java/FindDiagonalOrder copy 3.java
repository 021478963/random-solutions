import java.lang.Math;

public class FindDiagonalOrder {

  public static void main(String[] args) {
    // int[][] mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    // int[][] mat = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
    int[][] mat = {{1, 2, 3, 4, 5, 6}, {6, 7, 8, 9, 10, 6}, {11, 12, 13, 14, 15, 6}, {16, 17, 18, 19, 20, 6}};
    int[] result = findDiagonalOrder(mat);
    for (int i : result) {
      // System.out.println(i);
    }
  }

  public static int[] findDiagonalOrder(int[][] mat) {
    int iterations = mat.length + mat[0].length - 1;
    int counter = 0;
    int[] result = new int[mat.length * mat[0].length];
    int top0, top1, bot0, bot1;

    for (int i = 0; i < iterations; i++) {
      if (i < mat[0].length - 1) {
        top0 = i;
        top1 = 0;
      } else {
        top1 = i - mat[0].length + 1;
        top0 = mat[0].length - 1;
      }

      if (i < mat.length - 1) {
        bot0 = 0;
        bot1 = i;
      } else {
        bot0 = i - mat.length + 1;
        bot1 = mat.length -1;
      }

      // System.out.println(bot0 + " " + bot1);
      // System.out.println(top0 + " " + top1);
      // System.out.println();

      System.out.println("iteration " + (i + 1));
      if (i % 2 == 0) {
        for (int n = bot1; n >= 0; n--) {
          for (int m = 0; m <= top0; m++) {
            System.out.println(n + ", " + m);
            // System.out.println(mat[n][m]);
            result[counter] = mat[n][m];
            counter++;
            n--;
          }
        }
      } else {
        for (int n = 0; n <= bot1; n++) {
          for (int m = top0; m >= 0; m--) {
            System.out.println(n + ", " + m);
            // System.out.println(mat[n][m]);
            result[counter] = mat[n][m];
            counter++;
            n++;
          }
        }
      }
    }

    return result;
  }
  
}
