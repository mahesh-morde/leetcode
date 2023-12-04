# 



class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        s=0
        
        for i in range(len(points)-1):
            a=points[i]
            b=points[i+1]
            max1=max(a[0],b[0])
            min1=min(a[0],b[0])
            max2=max(a[1],b[1])
            min2=min(a[1],b[1])
            c=max((max1-min1),(max2-min2))  
            s+=c 
        return (s)
