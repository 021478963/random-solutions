import java.util.List;
import java.util.ArrayList;

public class PascalsTriangle {
  public static void main(String[] args) {
    System.out.println(generate(5));
  }

  public static List<List<Integer>> generate(int numRows) {
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    List<Integer> temp = new ArrayList<Integer>();
    temp.add(1);
    result.add(temp);
    if (numRows == 1) {
      return result;
    }
    temp = new ArrayList<Integer>();
    temp.add(1);
    temp.add(1);
    result.add(temp);
    if (numRows == 2) {
      return result;
    }

    for (int i = 2; i < numRows; i++) {
      temp = result.get(i - 1);
      List<Integer> next = new ArrayList<Integer>();
      next.add(1);
      for (int j = 0; j < temp.size() - 1; j++) {
        next.add(temp.get(j) + temp.get(j + 1));
      }
      next.add(1);
      result.add(next);
    }
    return result;
  }
}
