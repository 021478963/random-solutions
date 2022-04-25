import java.util.Stack;

public class CheckValidString {

  public static void main(String[] args) {
    String s = "(";
    System.out.println(checkValidString(s));
  }

  public static boolean checkValidString(String s) {
    int safety = 0;
    Stack<Character> stack = new Stack<Character>();

    int depth = 0;

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c == '(') {
        stack.add(c);
        depth++;
      } else if (c == ')') {
        if (stack.size() > 0 && stack.peek() == '(') {
          stack.pop();
          if (depth > 0)
            depth--;
        } else if (safety > 0) {
          if (depth > 0)
            depth--;
          safety--;
        } else {
          System.out.println("hi");
          return false;
        }
      } else {
        safety++;
        if (depth > 0) {
          depth--;
        }
      }
      System.out.println(depth);
    }

    // int n = stack.size();
    // for (int i = 0; i < n; i++) {
    //   System.out.println(stack.pop());
    // }
    // System.out.println(safety);
    // System.out.println(depth);

    if (stack.size() == 0) {
      return true;
    } else if (depth == 0 && safety >= stack.size()) {
      return true;
    }
    else {
      return false;
    }
  }
}