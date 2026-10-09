class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int counter = 0;
        for (int num : nums) {
            set.add(num);
        }
        for (int number : set) {
            int c = 0;
            while (set.contains(number)) {
                c++;
                number++;
            }
            if (c > counter) {
                counter = c;
            }
        }
        return counter;
    }
}