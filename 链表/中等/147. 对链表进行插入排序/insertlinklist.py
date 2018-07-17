# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        res = ListNode(head.val)
        head = head.next
        while head:
            last_node = None
            node = res
            has_inserted = False
            while node:
                if head.val <= node.val:
                    # 插入链表
                    tmp = ListNode(head.val)
                    if last_node:
                        last_node.next = tmp
                        tmp.next = node
                    else:
                        tmp.next = node
                        res = tmp
                    has_inserted = True
                    break
                last_node = node
                node = node.next

            # 在尾部插入
            if not has_inserted:
                tmp = ListNode(head.val)
                last_node.next = tmp
            head = head.next
        return res




if __name__ == '__main__':
    s = Solution()
    x = ListNode(3)
    x.next = ListNode(2)
    x.next.next = ListNode(1)
    y0 = s.insertionSortList(x)
    print ''
