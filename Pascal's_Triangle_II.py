class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        t = [1]
        
        for _ in range(1, rowIndex + 1):
            s = [1]
            for y in range(len(t) - 1):
                s.append(t[y] + t[y + 1])
            s.append(1)
            t = s

        return t
