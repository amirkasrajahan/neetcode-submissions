class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                if (token.equals("+")) {
                    int b = stack.pop(); // right operand
                    int a = stack.pop(); // left operand
                    int var = a + b;
                    stack.push(var);
                } else if (token.equals("-")) {
                    int b = stack.pop(); // right operand
                    int a = stack.pop(); // left operand
                    int var = a - b;
                    stack.push(var);
                } else if (token.equals("*")) {
                    int b = stack.pop(); // right operand
                    int a = stack.pop(); // left operand
                    int var = a * b;
                    stack.push(var);
                } else if (token.equals("/")) {
                    int b = stack.pop(); // right operand
                    int a = stack.pop(); // left operand
                    int var = a / b;
                    stack.push(var);
                }
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.getLast();
    }
}