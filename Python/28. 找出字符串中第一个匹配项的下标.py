# 方法一：暴力双重循环

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        在 haystack 中寻找 needle 第一次出现的位置，找不到返回 -1。
        题目保证 1 <= len(haystack), len(needle) <= 10^4
        """

        # n: 主串长度，m: 模式串长度
        n = len(haystack)
        m = len(needle)

        # 如果 needle 比 haystack 还长，必不可能匹配
        if m > n:
            return -1

        # 外层循环：枚举“匹配起点” i
        # i 最大只能到 n - m（含），因为再往后剩余长度不足 m
        # 所以 range(n - m + 1)
        for i in range(n - m + 1):
            # 内层指针 j：表示 needle 当前匹配到的位置
            j = 0

            # 逐个字符比较：
            # haystack 的第 i+j 个字符 与 needle 的第 j 个字符
            # 只要相同就继续推进 j
            while j < m and haystack[i + j] == needle[j]:
                j += 1

            # 如果 j 走到了 m，说明 needle[0..m-1] 全部匹配成功
            # 当前起点 i 就是第一个匹配下标（因为 i 是从小到大枚举的）
            if j == m:
                return i

            # 否则当前 i 匹配失败，外层 for 会自动尝试下一个 i

        # 所有起点都试过仍未匹配
        return -1


# 方法二：Python内置方法

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


# 方法三：KMP算法

# 见 [https://sunnyhmz.top/archives/kmp-algorithm](https://sunnyhmz.top/archives/kmp-algorithm)