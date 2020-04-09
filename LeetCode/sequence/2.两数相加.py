# -*- coding: utf-8 -*-
# @Time : 2020/4/9 23:16
# @Author : zdqzyx
# @File : 2.两数相加.py
# @Software: PyCharm

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        phead = plast = ListNode(-1)
        carry = 0
        while l1 and l2:
            p = ListNode(l1.val + l2.val + carry)
            if p.val>=10:
                p.val = p.val%10
                carry = 1
            else:
                carry = 0
            plast.next = p
            plast = plast.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            plast.next = l1
            if carry:
                while l1:
                    plast = l1
                    l1.val += carry
                    if l1.val>=10:
                        l1.val = l1.val%10
                        carry=1
                    else:
                        carry = 0
                        break
                    l1 = l1.next
        elif l2:
            plast.next = l2
            if carry:
                while l2:
                    plast = l2
                    l2.val += carry
                    if l2.val>=10:
                        l2.val = l2.val%10
                        carry=1
                    else:
                        carry = 0
                        break
                    l2 = l2.next
        if carry:
            plast.next = ListNode(carry)
        return phead.next