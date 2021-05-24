# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那两个整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 你可以按任意顺序返回答案。


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        # hash表是一个大字典，普通的数组是通过下标访问元素，hash则构建了通过元素查找下标的渠道
        for index, item in enumerate(nums):
            hashmap[item] = index # hash表构建好之后确实不存在重复的元素，对于重复的item，只会保留原list中最后一次出现该元素的下标
        for index, item in enumerate(nums): # 按照下标从前往后遍历列表，取到一个值item，就看看（目标值target-item）是否存在于hash表中，如果能拿到，拿到的下标不是我现在item的这个，那就可以（从左往右遍历，但是hash保留最右边的重复元素下标，比较的时候对一下两个下标不一致就可以覆盖【3，3】-》6这种情况）
            if hashmap.get(target-item) and hashmap.get(target-item) != index:
                return [index, hashmap.get(target-item)]
