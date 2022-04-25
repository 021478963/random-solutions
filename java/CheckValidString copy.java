import java.util.Stack;

public class CheckValidString {

  public static void main(String[] args) {
    String s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())";
    System.out.println(checkValidString(s));
  }

  public static boolean checkValidString(String s) {
    int safety = 0;
    Stack<Character> stack = new Stack<Character>();

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c == '(') {
        stack.add(c);
      } else if (c == ')') {
        if (stack.size() > 0 && stack.peek() == '(') {
          stack.pop();
        } else if (safety > 0) {
          safety--;
        } else {
          System.out.println("hi");
          return false;
        }
      } else {
        safety++;
      }
    }

    if (stack.size() == 0) {
      return true;
    } else {
      System.out.println(safety);
      int n = stack.size();
      for (int i = 0; i < n; i++) {
        System.out.println(stack.pop());
      }
      return false;
    }
  }
}