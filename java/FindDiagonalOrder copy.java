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
    int start0, end0, start1, end1;
    // System.out.println();
    for (int i = 0; i < iterations; i++) {
      // System.out.println();
      // System.out.println(i);
      // System.out.println();
      // System.out.println(counter);

      if (i < ((iterations / 2 + iterations % 2))) {
        start0 = 0;
        end0 = i;
        start1 = 0;
        end1 = i;
      } else {
        start0 = i - (iterations / 2 + iterations % 2) + 1;
        end0 = mat[0].length - 1;

        start1 = mat.length - 1;
        end1 = i - (iterations / 2 + iterations % 2) + 1;

        System.out.println(start0);
        System.out.println(end0);
        System.out.println();
        System.out.println(start1);
        System.out.println(end1);
        System.out.println();
        System.out.println();
      }


      // if (i % 2 == 0) {
      //   for (int n = i; n >= 0; n--) {
      //     for (int m = 0; m <= i; m++) {
      //       // System.out.println(n + ", " + m);
      //       System.out.println(mat[n][m]);
      //       result[counter] = mat[n][m];
      //       counter++;
      //       n--;
      //     }
      //   }
      // } else {
      //   for (int n = 0; n <= i; n++) {
      //     for (int m = i; m >= 0; m--) {
      //       // System.out.println(n + ", " + m);
      //       System.out.println(mat[n][m]);
      //       result[counter] = mat[n][m];
      //       counter++;
      //       n++;
      //     }
      //   }
      // }
    }

    return result;
  }
  
}
