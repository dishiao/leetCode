class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 判断是否为空或者空列表
        if strs is None or strs == []:
            return ''
        # 计算列表中的最长字符串长度、计算列表长度
        strs_len_list = []
        for s in strs:
            strs_len_list.append(len(s))
        max_len_str = min(strs_len_list)
        max_len_list = len (strs)
        # 判断特殊情况
        if max_len_str == 1 and max_len_list == 1:
            return  strs[0]
        final = []
        for i in range(0,max_len_str):
            for j in range(0,max_len_list):
                str_p = strs[j][i]
                
                if (j > 0) and (str_s != str_p):
                    # 必须开头就匹配，开头不匹配直接就return 
                    if i == 0:
                        return ''
                    else:
                        break
                str_s = strs[j][i]
                # 判断完全完成之后才append进入list
                if j == max_len_list-1:
                    final.append(str_s)
        # 转换格式
        final_str = "".join(final)
        return final_str
    
