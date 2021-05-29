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
