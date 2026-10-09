class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int number : nums) {
            if (map.containsKey(number)) {
                return true;
            } else {
                map.put(number, 1);
            }
        }
        return false;
    }
}