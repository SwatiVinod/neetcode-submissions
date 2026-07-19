class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a
        
        l = 0
        r = len(a) - 1

        while True:
            midA = (l + r) // 2
            midB = half - midA - 2

            aleft = a[midA] if midA >= 0 else float('-inf')
            bleft = b[midB] if midB >= 0 else float('-inf')
            aright = a[midA + 1] if midA + 1 < len(a) else float('inf')
            bright = b[midB + 1] if midB + 1 < len(b) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = midA - 1
            else:
                l = midA + 1
            

