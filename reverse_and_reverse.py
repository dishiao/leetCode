class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        listA = []
        for a in A:
            #水平翻转
            a = a[::-1]
            #反转图片
            listB = []
            for b in a:
                if b == 1:
                    b=0
                elif b == 0:
                    b=1
                listB.append(b)
            listA.append(listB)
        return listA
            
