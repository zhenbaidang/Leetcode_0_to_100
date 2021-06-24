# z字形排列，但是最后读取的时候是按行来读，并且是忽略中间的空格。那我们可以搞一个numRows行的列表，每行都是一个列表，用append方法往某行追加元素即可
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = min(len(s), numRows) # 覆盖对于字符串长度还不如numRows长的情况，选二者最小的记为row行，一会儿就要构造一个row行的二维数组
        # 如果最终只有一行，或者干脆一行都没有（空字符串），可以直接返回原始字符串了
        if row < 2:
            return s
        # 搞一个temp来记录一下行数，然后构造一个row行的列表
        temp = row
        result = []
        while temp:
            result.append([])
            temp -= 1
        # i用来表示当前操作的result数组的行标；cur是字符串s的游标；huanhang是个bool值，表示是否到了要换行的地方（哪些地方要换行呢，cur走到能被row-1整除的地方时，就应该要切换huanhang这个值）
        i = 0
        huanhang = 1
        cur = 0
        # 当字符串游标还没走到头时进入循环
        while cur < len(s):
            # 该往第i行追加cur下标的字符了
            result[i].append(s[cur])
            # 判断一下，当cur走到边界时，（也就是result的最上面一行和最下面一行时）并且此时cur不能是0（第一次刚进循环，不切换）切换huanhang的值，将其与1异或
            if cur % (row-1) == 0 and cur != 0:
                huanhang = huanhang ^ 1
            # 计算下一次循环应该往第几行追加，（也就是+1往下挪一行还是-1往上挪一行）
            i += 1 if huanhang else -1
            # cur字符串游标往后挪
            cur += 1
        # 构造一个空字符串，按从上到下从左到右的顺序遍历result，把拿到的值追加到result_str中
        result_str = ''
        for i in range(row):
            for j in range(len(result[i])):
                result_str += str(result[i][j])

