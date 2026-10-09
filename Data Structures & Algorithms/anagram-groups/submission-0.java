class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> list = new ArrayList<>();
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        for (String str : strs) {
            int[] arr = new int[26];
            for (int i = 0; i < str.length(); i++) {
                arr[str.charAt(i) - 'a']++;
            }
            String key = Arrays.toString(arr);
            if (map.containsKey(key)) {
                map.get(key).add(str);
            } else {
                map.put(key, new ArrayList<>(Arrays.asList(str)));
            }
        }
        for (ArrayList<String> li : map.values()) {
            list.add(li);
        }
        return list;
    }
}
