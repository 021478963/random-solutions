public class MaxProfit {
  public int maxProfit(int[] prices) {
    int smallest = -1;
    int biggest = -1;
    int profit = 0;
    int buy = -1;
    int sell = -1;

    for (int i = 0; i < prices.length; i++) {
      if (prices[i] > smallest) {
        if (biggest - smallest > profit) {
          profit = biggest - smallest;
        }
        smallest = prices[i];
      } else if (prices[i] > biggest) {
        if (biggest - smallest > profit) {
          profit = biggest - smallest;
        }
        biggest = prices[i];
      }
    }

    return profit;
  }
}
