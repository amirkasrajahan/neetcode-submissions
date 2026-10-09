class Solution {
    public int maxProfit(int[] prices) {
        int min = 1000;
        int max = 0;
        for (int i = 0; i < prices.length; i++) {
            if (min > prices[i]) {
                min = prices[i];
            }
            int curr = prices[i] - min;
            if (max < curr) {
                max = curr;
            }
        }
        return max;
    }
}
