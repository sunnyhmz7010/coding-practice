# 题目思路：
# 双指针 + 扫尾
#
# 核心逻辑：
# 可以把 word1 和 word2 想象成两个排队的队伍。
# 每次分别从 word1 和 word2 中取出一个字符，
# 按照 word1 -> word2 -> word1 -> word2 的顺序加入结果 res。
#
# 当其中一个字符串已经全部取完时，交替过程停止。
# 此时另一个字符串如果还有剩余字符，
# 就直接把剩下的部分追加到结果末尾。


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 准备一个空列表 res，用来存放拼接后的字符
        res = []

        # 获取两个字符串的长度
        m = len(word1)
        n = len(word2)

        # i 指向 word1 当前要处理的字符
        # j 指向 word2 当前要处理的字符
        # 字符串的索引从 0 开始，所以初始值都是 0
        i = 0
        j = 0

        # 只要 word1 和 word2 都还有字符没有处理，
        # 就继续交替取字符
        #
        # i < m 表示 word1 还有字符
        # j < n 表示 word2 还有字符
        while i < m and j < n:
            # 先加入 word1 当前的字符
            res.append(word1[i])

            # 再加入 word2 当前的字符
            res.append(word2[j])

            # 两个指针分别向后移动一位
            #
            # i += 1 等价于：
            # i = i + 1
            i += 1
            j += 1

        # while 循环结束后，
        # 说明至少有一个字符串已经全部处理完。
        #
        # 如果 word1 比较长，
        # word1[i:] 就表示从索引 i 开始一直取到字符串末尾。
        #
        # 例如：
        # word1 = "abcde"
        # i = 3
        # word1[i:] 就是 "de"
        #
        # 如果 word1 已经全部处理完，
        # 那么 word1[i:] 就是空字符串 ""，
        # append 空字符串不会影响最终拼接结果。
        res.append(word1[i:])

        # 同理，把 word2 剩余的字符追加进去
        res.append(word2[j:])

        # join() 用于把列表中的字符串拼接起来。
        #
        # "".join(res)
        #
        # "" 表示使用“空字符串”作为连接符，
        # 也就是各个字符之间不添加任何东西。
        #
        # 例如：
        # res = ["a", "b", "c"]
        #
        # "".join(res)  -> "abc"
        # "-".join(res) -> "a-b-c"
        # " ".join(res) -> "a b c"
        #
        # 因此这里最终会得到完整的交替合并字符串。
        return "".join(res)