# this program is meant to add two reverse ordered linked lists representing numbers to calculate their sum

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def add(self, l1, l2):

        # create the reverse linked list
        tempsum = l1.val + l2.val
        sum = ListNode(tempsum % 10)
        carry = tempsum // 10
        sum = sum.next
        one = l1.next
        two = l2.next
        while not((one and two) != None):
            tempsum = one.val + two.val
            sum.val = tempsum % 10 + carry
            sum = sum.next
            one = one.next
            two = two.next
        if carry != 0:
            sum.next = ListNode(carry)

        # reverse the created list
        temp = sum
        old = ListNode(temp.val)
        new = ListNode(None)
        new.next = old
        old = new
        temp = temp.next
        while temp != None:
            old.val = temp.val
            new = ListNode(None)
            new.next = old
            old = new
            temp = temp.next
        return old

    def test(self):
        x = ListNode(2)
        x.next = ListNode(5)
        y = ListNode(8)
        y.next = ListNode(6)
        z = self.add(x, y)
        while z.next != 0:
            print(z.val)


test = Solution
test.test(self)