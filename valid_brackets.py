class Solution:
    def isValid(self, s: str) -> bool:
    # 利用栈的思想 list.append 和 list.pop可以帮助你
    # 整体思路 遇见 左括号 入栈 栈非空出栈 判断匹配 第一个 符号是右括号则false 最后栈有值则false 没值则 true
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) != 0:
                    char_ =stack.pop()
                    if (char_ == '(' and char != ')') or (char_ == '[' and char != ']') or (char_ == '{' and char != '}'):
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

            
            
        
