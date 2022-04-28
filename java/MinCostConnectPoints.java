import java.util.Comparator;
import java.util.HashMap;
import java.util.Arrays;
import java.math.*;

public class MinCostConnectPoints {
  
  public static int minCostConnectPoints(int[][] points) {
    int total = 0;
    int lastX, lastY;
    int closestX, closestY;

    class sortByX implements Comparator<int[]> {
      public int compare(int[] a1, int[] a2) {
        return a1[0] - a2[0];
      } 
    }

    Arrays.sort(points, new sortByX());

    HashMap<String, Integer> closest = new HashMap<String, Integer>();
    closestX = points[0][0];
    closestY = points[0][1];
    lastX = closestX;
    lastY = closestY;

    for (int i = 1; i < points.length; i++) {
      String code = points[i][0] + " " + points[i][1];
      if (closest.containsKey(code)) {
        String[] temp = code.split(" ");
        closestX = Integer.parseInt(temp[0]);
        closestY = Integer.parseInt(temp[1]);
      }

      for (int i = Math.max(0, points[i][0] - closestX); i < Math.min())
    }
  }
}
