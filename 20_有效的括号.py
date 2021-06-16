# 当只有一种括号时，可以遇到左括号就+1，遇到右括号就-1，在保证sum始终>=0的情况下，当最终把s遍历完，sum应为0，此时返回True；若不为0，则为False
# 当有三种括号混起来用时，就可以利用栈。从左到右遍历s，遇到左括号就入栈，遇到右括号，就看栈顶元素是否为其对应的左括号，是则pop。遍历完成后看栈是否为空，空则True否则为False
class Solution:
    def isValid(self, s: str) -> bool:
        map_dic = {'{':'}', '[':']', '(':')'}
        stack_s = []
        for i in range(len(s)-1, -1, -1):
            if s[i] in [']',')','}']:
                stack_s.append(s[i])
            else:
                if len(stack_s) != 0 and map_dic[s[i]] == stack_s[-1]:
                    stack_s.pop()
                else:
                    return False
        if stack_s:
            return False
        else:
            return True
