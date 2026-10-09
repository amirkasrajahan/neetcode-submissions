class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if ("({[".indexOf(s.charAt(i)) != -1) {
                stack.push(s.charAt(i));
            }
            if (")}]".indexOf(s.charAt(i)) != -1) {
                if (stack.isEmpty()) {
                    return false;
                }
                if (s.charAt(i) == ')' && stack.getLast() == '(') {
                    stack.pop();
                } else if (s.charAt(i) == ']' && stack.getLast() == '[') {
                    stack.pop();
                } else if (s.charAt(i) == '}' && stack.getLast() == '{') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
