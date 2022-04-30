import java.util.ArrayList;
import java.util.Collections;

public class MaxProfitIII {
  
  public int maxProfit(int[] prices) {
    ArrayList<Integer> profit = new ArrayList<Integer>();
    int start = 0;

    for (int i = 0; i < prices.length - 1; i++) {
      if (prices[i] > prices[i + 1]) {
        profit.add(prices[i] - prices[start]);
        start = i + 1;
      }
    }
    if (start != prices.length - 1) {
      profit.add(prices[prices.length - 1] - prices[start]);
    }

    Collections.sort(profit);

    return profit.get(profit.size() - 2) + profit.get(profit.size() - 3);
  }
}
