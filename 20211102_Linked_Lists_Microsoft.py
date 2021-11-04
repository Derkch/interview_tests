# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:08:33 2021

@author: alexd
"""
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    magnitud = 0
    val = l1.next.next.val + l2.next.next.val
    if (val - 10) >= 0:
        magnitud = int(val/10)
        val -= 10
    l3 = ListNode(val)
    val = l1.next.val + l2.next.val + magnitud
    magnitud = 0
    if (val - 10) >= 0:
        magnitud = int(val/10)
        val -= 10
    l3.next = ListNode(val)
    val = l1.next.next.val + l2.next.next.val + magnitud
    magnitud = 0
    if (val - 10) >= 0:
        magnitud = int(val/10)
        val -= 10
    l3.next.next = ListNode(val)
    return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
  print(result.val)
  result = result.next
# 7 0 8
