# 合并数组（两个有序数组合并，是归并排序里的一个步骤），然后返回最中间的数（合并后数组有奇数个数字）或返回最中间两个数的均值（合并后数组中有偶数个数字），复杂度在O（m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        point1 = point2 = 0 # 初始化两个指针为0
        nums_list = [] # 定义一个空列表，用来存放合并后的数组
        while point1 < len(nums1) and point2 < len(nums2): # 当指针合法时
            if nums1[point1] < nums2[point2]: # 比较指针位置的数值大小，把小的那个的值并入nums_list，并把这个指针往后挪一位（总有一个指针先行到达边界，然后就会跳出循环）
                nums_list.append(nums1[point1])
                point1 += 1
            else:
                nums_list.append(nums2[point2])
                point2 += 1
        # 不管是nums1还是nums2，一次while循环之后，指针只有：指向空值和指向未添加到nums_list中的值（未使用过的值）两种情况
        # 列表的切片操作容错很好，无论索引是否指空，都不会报错，而是会返回未加入到nums_list中的所有值，或者一个空列表[]
        nums_list += nums1[point1:]
        nums_list += nums2[point2:]
        # 拿到合并数组之后，判断一下奇数个还是偶数个，返回中位数
        if len(nums_list)%2:
            return nums_list[len(nums_list)//2]
        else:
            return (nums_list[len(nums_list)//2-1]+nums_list[len(nums_list)//2])/2


# 抛开合并数组重新sort然后直接找中位数的方法不谈，这是第一个版本，复杂度为O(m+n）
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 首先拿到两个数组的长度
        n1 = len(nums1)
        n2 = len(nums2)
        # 对特例进行判断，如果是两个空数组，直接返回0
        if n1==0 and n2==0:
            return 0
        # 定义一个全局变量，用来往里面追加元素
        result = []
        def find_result(nums1, nums2, num): # 传两个数组nums1、nums2和需要计算几个数字num进去
            # 对于
            if len(nums1)==0 and len(nums2)==0:
                return
            if num==0:
                return
            else:
                if len(nums1)==0:
                    result.append(nums2.pop(0))
                    find_result(nums1, nums2, num-1)
                elif len(nums2)==0:
                    result.append(nums1.pop(0))
                    find_result(nums1, nums2, num-1)
                else:
                    if nums1[0] < nums2[0]:
                        result.append(nums1.pop(0))
                    else:
                        result.append(nums2.pop(0))
                    find_result(nums1, nums2, num-1)
        
        
        num = ((n1+n2)//2)+1
        find_result(nums1, nums2, num)
        print(result)
        if (n1+n2)%2==0:
            return (result[-1]+result[-2])/2
        else:
            return result[-1]

# 事实上不需要把整个合并数组都找到，找到中间的一个值或两个值即可
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a_len = len(nums1)
        b_len = len(nums2)
        sum_len = a_len + b_len
        a_cur = b_cur = 0 # 两个游标负责取nums1和nums2的值
        left = right = -1 # 定义两个槽位用来保存两个要做平均的中位数或者用right来保存中位数，left弃之不用
        if sum_len == 0:
            return 0
        for i in range(sum_len//2+1): # 不管合并数组最终是奇数还是偶数，我都要计算到下标为sum_len//2这个值（这个值是要保留的），故range(sum_len//2+1)
            left = right # 把右边的值赋给左边保存，下面对right进行更新
            # 什么时候新的值是用nums1中取得值？1. nums1还没取到末尾（a_cur < a_len） 2. 同时nums2取完了（b_cur >= b_len） 3. 又或者nums2没取完，但是nums1在a_cur游标处的值比nums2在b_cur处的值小
            if (a_cur < a_len) and ((b_cur >= b_len) or (nums1[a_cur] < nums2[b_cur])): 
                right = nums1[a_cur]
                a_cur += 1
            else:
                right = nums2[b_cur]
                b_cur += 1
        # 循环最后一次执行时，应该是要处理合并数组的下标为sum_len//2处的值，即此时right就是sum_len//2的对应值，而left 是他前一个值sum_len//2-1
        
        # 判断一下奇数还是偶数，决定返回right不用left还是返回right和left的均值
        if sum_len % 2:
            return right
        else:
            return (left+right)/2

        
