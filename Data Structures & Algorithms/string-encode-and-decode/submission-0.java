class Solution {
    public String encode(List<String> strs) {
        String encodedString = "";
        for (String word : strs) {
            encodedString += (word.length() + "#" + word);
        }
        return encodedString;
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = str.indexOf('#', i); // find # starting from i
            int len = Integer.parseInt(str.substring(i, j)); // "5" → 5
            String word = str.substring(j + 1, j + 1 + len);
            list.add(word);
            i = j + 1 + len;
        }
        return list;
    }
}
