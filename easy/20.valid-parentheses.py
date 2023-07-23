#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

# 方針
# ・スタックを用いてopenとcloseが同じかを判断

class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        for c in s:
            if c in ['(', '{', '[']:
                open.append(c)
            elif c == ')' and len(open) != 0 and open[-1] == '(':
                open.pop()
            elif c == '}' and len(open) != 0 and open[-1] == '{':
                open.pop()
            elif c == ']' and len(open) != 0 and open[-1] == '[':
                open.pop()
            # 上記以外はfalesを返す
            else:
                return False
        # 一文字のopen記号の際にfalseを返す必要がある
        # ループが終了して要素残ってたらfalse
        if open:
            return False
        else:
            return True
# @lc code=end

print(Solution().isValid("()[]{}"))