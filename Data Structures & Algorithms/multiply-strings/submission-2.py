class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                total = result[i + j] + product
                result[i + j] = total % 10
                result[i + j + 1] += total // 10
        print(result)
        result = result[::-1]
        beg = 0
        while beg < len(result) and result[beg] == 0:
            beg += 1

        answer = ""
        for num in result[beg:]:
            answer += str(num)
        return answer
