class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<String, Integer> map = new HashMap<>();

        String[] arr1 = s.split("");
        String[] arr2 = t.split("");

        for (String ch : arr1) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (String ch : arr2) {
            if (!map.containsKey(ch)) {
                return false;
            }
            map.put(ch, map.get(ch) - 1);
        }

        for (int val : map.values()) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
}
