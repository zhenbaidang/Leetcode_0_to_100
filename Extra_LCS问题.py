# 最长公共子序列“长度”的递归解法
def lcs(a_str, b_str):
    m = len(a_str)
    n = len(b_str)
    
    if m == 0 or n == 0:
        return 0
    if a_str[-1] == b_str[-1]:
        return lcs(a_str[:-1], b_str[:-1]) + 1
    else:
        return max(lcs(a_str[:-1], b_str), lcs(a_str, b_str[:-1]))

# 最长公共子序列“长度”的动态规划解法
def lcs_dp(a_str, b_str):
    m = len(a_str)
    n = len(b_str)
    # 初始化一个(m+1)*(n+1)的动态规划表
    dp_result = [[-1]*(n + 1)] * (m + 1)
    # 将第一行第一列全部初始化为0
    for j in range(n + 1):
        dp_result[0][j] = 0
    for i in range(m + 1):
        dp_result[i][0] = 0
    # 开始填表
    # 注意此时因为多了一行一列，有一些下标的变化，就是所有dp_result表中应该操作的元素都应该是下标整体右挪一位下挪一位
    for i in range(m):
        for j in range(n):
            if a_str[i] == b_str[j]:
                dp_result[i+1][j+1] = dp_result[i][j] + 1
            else:
                dp_result[i+1][j+1] = max(dp_result[i][j+1], dp_result[i+1][j])
    # 动态规划表中右下角最大的值就是两个字符串的最长公共子序列的长度
    return dp_result[-1][-1]


# 最长公共子串的“长度”的动态规划解法
def lcs_dp(a_str, b_str):
    m = len(a_str)
    n = len(b_str)
    # 初始化一个(m+1)*(n+1)的动态规划表
    dp_result = [[-1]*(n + 1)] * (m + 1)
    # 将第一行第一列全部初始化为0
    for j in range(n + 1):
        dp_result[0][j] = 0
    for i in range(m + 1):
        dp_result[i][0] = 0
    
    max_value = -1
    
    # 开始填表
    # 注意此时因为多了一行一列，有一些下标的变化，就是所有dp_result表中应该操作的元素都应该是下标整体右挪一位下挪一位
    
    for i in range(m):
        for j in range(n):
            if a_str[i] == b_str[j]:
                dp_result[i+1][j+1] = dp_result[i][j] + 1
            else:
                dp_result[i+1][j+1] = 0 # 只有此处不同，当两个序列值不同时，不向前累计，而是直接记0，重新开始计算
            # 一轮循环过后，比较当前值与max_value的大小，更新保存最大的
            max_value = (max_value, dp_result[i+1][j+1])
    # 最终要返回的是整个dp表中的最大值
    return max_value

# 如何找到LCS问题的那个最大公共子序列或子串的具体字符串？

# 最长公共子串的串：dp表中的最大值就是最长公共子串的长度，在更新最大值时顺便保存dp表的游标值，并在拿到最终的游标后，向前对任意输入字符串取max_value个字符即可
def lcs_dp(a_str, b_str):
    m = len(a_str)
    n = len(b_str)
    # 初始化一个(m+1)*(n+1)的动态规划表
    dp_result = [[-1]*(n + 1)] * (m + 1)
    # 将第一行第一列全部初始化为0
    for j in range(n + 1):
        dp_result[0][j] = 0
    for i in range(m + 1):
        dp_result[i][0] = 0
    
    max_value = -1
    cur = -1
    # 开始填表
    # 注意此时因为多了一行一列，有一些下标的变化，就是所有dp_result表中应该操作的元素都应该是下标整体右挪一位下挪一位
    
    for i in range(m):
        for j in range(n):
            if a_str[i] == b_str[j]:
                dp_result[i+1][j+1] = dp_result[i][j] + 1
            else:
                dp_result[i+1][j+1] = 0 # 只有此处不同，当两个序列值不同时，不向前累计，而是直接记0，重新开始计算
            # 一轮循环过后，比较当前值与max_value的大小，更新保存最大的
            # max_value = (max_value, dp_result[i+1][j+1])
            # 在判断要保存最大的值时，如果更新了最大值，那就顺便存一下下标
            if dp_result[i+1][j+1] > max_value:
                max_value = dp_result[i+1][j+1]
                cur = i # 此处保存i，而非i+1，因为i，j的游标对应着a_str和b_str，取i，j均可，就看用哪个回溯
    for k in range(cur-max_value, cur+1):
        result_str += a_str[k]
    # 最终要返回的是整个dp表中的最大值
    return max_value，result_str













    
