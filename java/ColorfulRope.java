class Solution {
  public int minCost(String colors, int[] neededTime) {
    int total = 0;
    char last = 'z';
    ArrayList<Integer> consecutive = new ArrayList<Integer>();
    boolean state = false;

    for (int i = 0; i < colors.length(); i++) {
      if (colors.charAt(i) == last) {
        consecutive.add(neededTime[i - 1]);
        state = true;
      } else if (state) {
        consecutive.add(neededTime[i - 1]);
        Collections.sort(consecutive);
        int count = 0;
          do {
            total += consecutive.get(count);
            count++;
          } while (count < consecutive.size() - 1);
            consecutive = new ArrayList<Integer>();
            state = false;
      } else {
        state = false;
      }
      last = colors.charAt(i);
    }

    if (state) {
      consecutive.add(neededTime[neededTime.length - 1]);
      Collections.sort(consecutive);
      int count = 0;
      do {
        System.out.println(total);
        total += consecutive.get(count);
        count++;
      } while (count < consecutive.size() - 1);
    }
    return total;
  }
}