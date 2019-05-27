class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s_list = list(S)    # 转化为list
        final_list = []     # 最终被返回的list
        final_str = ""      # 最终被返回的list转成str
        left = 0    # 左括号计数
        right = 0   # 右括号计数
        first = 0   # 判断现在的括号该不该留下
        for s in s_list:
            if s == '(':
                left = left + 1
            if s == ')':
                right = right + 1
            if left != right:
                first = first + 1
                if first == 1:
                    continue
                final_list.append(s)
            if left == right:
                first = 0
        final_str = "".join(final_list)
        return final_str
