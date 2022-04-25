import java.util.HashSet;
import java.util.Set;

public class Matrix01 {
  public static void main(String[] args) {

  }

  public int[][] updateMatrix(int[][] mat) {
    Set<int[]> current = new HashSet<int[]>();
    Set<int[]> next = new HashSet<int[]>();

    for (int i = 0; i < mat.length; i++) {
      for (int j = 0; j < mat.length; j++) {
        if (mat[i][j] == 0) {
          current.add(new int[] {i, j});
        }
      }
    }

    int found = current.size();
    int toFind = mat.length * mat[0].length;
    while (found < toFind) {
      for (int[] i : current) {
        
      }
    }
  }
}