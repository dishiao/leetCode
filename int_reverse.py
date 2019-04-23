class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10:
            return x
        str_x = str (x)
        if str_x[0] == '-':
            str_new = str_x[1:][::-1]
            str_new = - int(str_new)
        else:
            str_new = str_x[::-1]
            str_new = int (str_new)
        
        # 溢出
        #if -2147483648<str_new<2147483647:
        #    str_new = str_new
        #else:
        #    str_new = 0
        #
        #return str_new
        
        return str_new if  -2147483648<str_new<2147483647 else 0
