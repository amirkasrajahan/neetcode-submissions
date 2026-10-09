class Solution {
    public boolean isPalindrome(String s) {
        String str1 = "";
        String str2 = "";
        for (int i = 0; i < s.length(); i++) {
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                continue;
            }
            str1 += s.toLowerCase().charAt(i);
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                continue;
            }
            str2 += s.toLowerCase().charAt(i);
        }
        return str1.equals(str2);
    }
}
