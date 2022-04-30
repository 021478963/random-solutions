public class MaxProfitII {
  
  public int maxProfit(int[] prices) {
    int profit = 0;
    int start = 0;

    for (int i = 0; i < prices.length - 1; i++) {
      if (prices[i] > prices[i + 1]) {
        profit += prices[i] - prices[start];
        start = i + 1;
      }
    }
    if (start != prices.length - 1) {
      profit += prices[prices.length - 1] - prices[start];
    }
    return profit;
  }
}
