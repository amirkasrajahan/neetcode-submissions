// import java.util.Stack;

class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;
    int min;
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if(minStack.isEmpty()){
            minStack.push(val);
            min = minStack.getLast();
        }
        else if(minStack.getLast() >= val){
            minStack.push(val);
            min = minStack.getLast();
        }

    }

    public void pop() {
        if(stack.getLast().equals(minStack.getLast())){
            stack.pop();
            minStack.pop();
        }
        else{
            stack.pop();
        }

    }

    public int top() {
        return stack.getLast();
    }

    public int getMin() {
        return minStack.getLast();
    }
}