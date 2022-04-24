public class AddTwoNumbers {
  public static void main(String[] args) {

  }

  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int sum = l1.val + l2.val;
    ListNode result;
    ListNode answer;

    if (sum > 9) {
      sum -= 10;
      if (l1.next != null) {
        l1.next.val++;
      } else if (l2.next != null) {
        l2.next.val++;
      } else {
        return new ListNode(sum, new ListNode(1));
      }
    }
    result = new ListNode(sum);
    answer = result;
    l1 = l1.next;
    l2 = l2.next;


    while (l1 != null || l2 != null) {
      if (l1 == null) {
        sum = 0 + l2.val;
        l2 = l2.next;
      } else if (l2 == null) {
        sum = l1.val + 0;
        l1 = l1.next;
      } else {
        sum = l1.val + l2.val;
        l1 = l1.next;
        l2 = l2.next;
      }
      if (sum > 9) {
        sum -= 10;
        if (l1 != null) {
          l1.val++;
        } else if (l2 != null) {
          l2.val++;
        } else {
          result.next = new ListNode(sum, new ListNode(1));
          continue;
        }
      }
      result.next = new ListNode(sum);
      result = result.next;
    }
    return answer;
  }
}