# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 例如：
# 输入：l1 = [2,4,3], -->  '342' + 
#      l2 = [5,6,4]  -->  '465'
# 输出：     [7,0,8]  --> ='807'
# 解释：342 + 465 = 807.


# ====================By Me====================
# 遍历了三次，一次链表l1,一次l2，加和的结果又遍历一次，添加了一个新的链表用于返回
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = 0
        l2_num = 0
        i=0
        while l1:
            l1_num += l1.val*(10**i)
            l1 = l1.next
            i += 1
        i=0
        while l2:
            l2_num += l2.val*(10**i)
            l2 = l2.next
            i += 1
        result_num = l1_num + l2_num
        result = ListNode()
        cur = result
        while result_num:
            cur.val = result_num % 10
            result_num = result_num // 10
            if result_num != 0:
                new_node = ListNode()
                cur.next = new_node
                cur = cur.next
        return result

# ========================================
# 本题出现本来是为了实现突破数据类型的位数限制，避免溢出，将每一位存成链表节点，能够实现任意大的数相加

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0 # 初始进位设置为0
        result = ListNode() # 构建结果链表的头节点
        cur = result # 设置游标
        while l1 or l2: # 当 l1 或 l2 还有节点未遍历过时
            if l1 and l2: # 当l1和l2都剩节点
                cur.val = (l1.val + l2.val + jinwei) % 10 # 当前结果节点应该是l1和l2的值加上进位值
                jinwei = (l1.val + l2.val + jinwei) // 10 # 算一下给下一位有没有进位
                l1 = l1.next # 游标向后挪
                l2 = l2.next
                if (l1 or l2): # 判断一下我后面还要不要加新的节点了（l1和l2都空了，且没有进位的时候不要加新节点了，如果l1或l2至少有一个还有节点，那就要加，然后游标后挪一位
                    new_node = ListNode()
                    cur.next = new_node
                    cur = cur.next
                else:
                    if not jinwei: # 如果l1和l2都空了，进位也没了，那就直接返回；如果节点空了，但是还有进位，那就直接建一个以进位为值的节点，挂到结果链表后面，返回结果即可
                        return result
                    else:
                        new_node = ListNode()
                        cur.next = new_node
                        cur = cur.next
                        cur.val = jinwei
                        return result
            if l1 and (not l2):
                cur.val = (l1.val + jinwei) % 10
                jinwei = (l1.val + jinwei) // 10
                l1 = l1.next
                if l1:
                    new_node = ListNode()
                    cur.next = new_node
                    cur = cur.next
                else:
                    if not jinwei:
                        return result
                    else:
                        new_node = ListNode()
                        cur.next = new_node
                        cur = cur.next
                        cur.val = jinwei
                        return result
            if l2 and (not l1):
                cur.val = (l2.val + jinwei) % 10
                jinwei = (l2.val + jinwei) // 10
                l2 = l2.next
                if l2:
                    new_node = ListNode()
                    cur.next = new_node
                    cur = cur.next
                else:
                    if not jinwei:
                        return result
                    else:
                        new_node = ListNode()
                        cur.next = new_node
                        cur = cur.next
                        cur.val = jinwei
                        return result
# ===========================================上述版本的简洁版=======================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = l1.val
        y = l2.val
        jinwei = 0

        result = ListNode()
        cur = result

        while (jinwei+x+y) or l1 or l2: # l1没走到none节点 或 l2没走到None节点 或他俩都没节点了，但是前俩节点加出一个进位 这三种情况，都需要再新建一个节点，追加到result这个链表的后面
            cur.next = ListNode((jinwei+x+y)%10)
            cur = cur.next
            jinwei = (jinwei+x+y) // 10 # 求出新的进位
            if l1: # l1没走到None，就让他继续走
                l1 = l1.next
            if l2: # l2没走到None，就让他继续走
                l2 = l2.next
            x = l1.val if l1 else 0 # 求出新的x：如果l1走到None节点了，那就让x=0，不然的话就让x=l1的值
            y = l2.val if l2 else 0 # 求出新的y 如果l2走到None节点了，那就让y=0 （但是注意，并非通过y=0就能推断l2已经没有后续的节点从而放弃添加新节点，只要l2还没走到头，就应该让循环继续）
        return result.next

    
# ===========================================列表逆序=======================================
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 建立一个节点值为0-9的链表
head = ListNode(0)
cur = head
for i in range(1, 10):
    cur.next = ListNode(i)
    cur = cur.next
# 开始逆序
next = head.next # 保存head的next节点，防止丢掉head链表
pre = None # 新的逆序链表的头节点
while head: # 当原链表head没走到None时
    next = head.next # 把头的next用next存一下
    head.next = pre # 把现在的头的下一个指向逆序链表的头（把现有的逆序链表挂在现在这个头的后面）
    pre = head # 把逆序链表的头指针移到当前的真正的头节点
    head = next # 把正序链表的头挪到上面保存好的next上
# 逆序链表输出一波
while pre:
    print(pre.val)
    pre = pre.next

      
