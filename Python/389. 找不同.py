# 方法一：异或运算

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0  # 初始化异或结果为 0

        # 1. 拿 s 里的每个字母去“碰撞”异或
        for ch in s:
            ans = ans ^ ord(ch)  # 也可以简写成 ans ^= ord(ch)

        # 2. 拿 t 里的每个字母继续去“碰撞”异或
        for ch in t:
            ans = ans ^ ord(ch)

        # 3. 剩下的数字转回字符
        return chr(ans)


# 方法二：求和作差法

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = 0  # 用来记录 s 中所有字母的数字总和
        sum_t = 0  # 用来记录 t 中所有字母的数字总和

        # 1. 累加 s 里面所有字母的 ASCII 数字
        for ch in s:
            sum_s = sum_s + ord(ch)

        # 2. 累加 t 里面所有字母的 ASCII 数字
        for ch in t:
            sum_t = sum_t + ord(ch)

        # 3. 计算差值，并转回字符
        diff = sum_t - sum_s
        return chr(diff)