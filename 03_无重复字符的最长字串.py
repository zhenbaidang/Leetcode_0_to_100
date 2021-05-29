# 此版本为两遍循环版，时间复杂度为n^2，用了hash表，在两轮for之后判断right节点是否在left~right的子串中重复出现
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        ans = 0
        if n <= 1: # 特例判断
            return n
        else:
            for left in range(n): # 左边游标一个一个点卡过去，每次换点，都新建一个空白的hash表
                hashmap = set()
                for right in range(left, n): # 右指针从左指针处出发，到字符串末尾开始遍历
                    if s[right] not in hashmap: # 只要当前所指位置的字符没有在left~right的字串中出现
                        hashmap.add(s[right]) # 就把这个字符加入hash表
                        if right == n-1: # 如果真的是从left出发到末尾，没找见重复字符，此时判断是不是到末尾（right走到n-1）
                            ans = max(ans, right - left + 1)  # 要是到头儿了，也得统计一下子串长度（right - left + 1）
                    else: # 只要发现right处的字符重复了，那就不用往后走了，直接开始计算right和left的距离（由于right现在站的位置就是重复字符的位置，所以子串的长度应该是前一个位置 （right-1）-left + 1）
                        ans = max(ans, right - left)
                        break
        return ans

# 上述版本走了哪些冤枉路？
# 1. 每次发现有重复字符后，left只递增1，事实上应该把left挪到子串中被发现重复的字符的后面，前提是这个字符后面的位置比现有的left靠右
# 2. 可以不需要做两次循环，拿着右指针从左往右走，并且把右指针所指的字符加入hash表（如果以前不存在，就新建一个，键为字符，值为右指针的位置），左边指针不动。一旦右指针
#    挪到了hash表中重复字符的位置，就把这个位置取出，判断left和（该位置+1）哪个更靠右，如果（该位置+1）更靠右，那就把left挪到这儿，并且把右指针现在的位置替换到该字符在hash表中的值

# 改进版本
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        hashmap = {}
        left = 0
        ans = 0
        for right in range(n):
            right_not_in_hash = (not hashmap.get(s[right])) and hashmap.get(s[right]) != 0
            if right_not_in_hash: # right点没撞到重复的
                hashmap[s[right]] = right # 把当前点位塞到hash表里
                ans = max(ans, right - left + 1)
            else: # right点撞到重复的了（只有‘真正’撞到重复点（即撞到了，并且这个点在left右边）或者right到达末尾节点时，才更新一波ans）
                if right != n-1: # right点没走到末尾节点时
                    if left < (hashmap.get(s[right]) + 1): # 撞到的点在left右侧
                        ans = max(ans, (right - 1) - left + 1) # 先把right往左一个点位的位置（此时还没撞重复点）和现有left的位置求一下子串长度
                        left = hashmap.get(s[right]) + 1 # 然后把left挪到重复点的右侧
                        hashmap[s[right]] = right # 更新hash中重复点位的位置为right的位置
                        continue
                    else: # 撞到的点在left左侧，像没事儿人一样，那不叫重复对吧，也不需要更新ans。但是需要更新hash表
                        hashmap[s[right]] = right
                else: # right点现在就是最后一个点，ans肯定会被更新
                    if left < (hashmap.get(s[right]) + 1): # 撞到的点在left右侧
                        ans = max(ans, (right - 1) - left + 1) # 不管到没到末尾，都应该保持现有left，把right往前挪一个，这是上一个没撞到的子串的情况，算一下长度
                        left = hashmap.get(s[right]) + 1 # left挪到重复点的右侧
                        hashmap[s[right]] = right
                    #     # left挪完了，现在肯定不重了，但问题是right已经到最后一个点了，是不是还应该再算一次ans，并且此次的right应该保留，不应该往前挪，因为right点位还没人和他重复
                    #     ans = max(ans, right - left + 1)
                    # else: # 撞到的点在left左侧，相当于没撞到，right节点保留，不用往前变成right-1
                    #     ans = max(ans, right-left+1)
                    ## 合并一下两种情况
                    ans = max(ans, right-left+1)
        return ans
