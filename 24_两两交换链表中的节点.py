# 迭代法
# 要交换左右两个节点，免不了需要对这左节点的前一个节点进行操作。它的下一个不指向left而是指向right。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 为避免对头节点单独讨论，创建一个空节点，指向头节点
        help_node = ListNode()
        help_node.next = head
        cur = help_node # 游标就从新建的这个节点开始
        # 在确保上一个节点（cur）以及左右节点都存在的情况下，开始循环
        while cur and cur.next and cur.next.next:
            # 用left和right标定原顺序中的左边和右边节点
            left = cur.next
            right = cur.next.next
            # 上一个节点（cur）的下一个指向从left节点脱开，指向right
            cur.next = right
            # 左节点的下一个指向从right节点脱开，指向right的下一个
            left.next = right.next
            # 右节点的下一个指向从right的下一个节点脱开，指向left
            right.next = left
            # 最终把游标cur更新成下一组要交换的左右节点的（上一个节点-->left）
            cur = left
        # 返回新建的help节点的下一个节点（即新链表的头节点）
        return help_node.next


# 
