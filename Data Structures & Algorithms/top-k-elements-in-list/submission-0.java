class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }
        List<Integer>[] buckets = new ArrayList[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }
        for (Integer key : map.keySet()) {
            buckets[map.get(key)].add(key);
        }
        int[] arr = new int[k];
        int idx = 0;
        for (int i = nums.length; i >= 0 && idx < k; i--) {
            for (Integer num : buckets[i]) {
                arr[idx] = num;
                idx++;
            }
        }
        return arr;
    }
}
