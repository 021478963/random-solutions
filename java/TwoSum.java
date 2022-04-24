import java.util.HashMap;
import java.util.Map;

public class TwoSum {
  public static void main(String[] args) {
    int[] result = twoSum(new int[] {3, 2, 4}, 6);
    for (int i : result) {
      System.out.println(i);
    }
  }

  
  public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<Integer, Integer>();

    for (int i = 0; i < nums.length; i++) {
      Integer needed = target - nums[i];
      if (seen.containsKey(needed)) {
        return new int[] {i, seen.get(needed)};
      }
      else {
        seen.put(nums[i], i);
      }
    }
    return null;
  }
}