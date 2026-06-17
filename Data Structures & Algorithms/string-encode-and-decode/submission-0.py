class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        sizes, result = [], []
        encoded_result = ""
        
        for word in strs:
            sizes.append(len(word))
        for size in sizes:
            result.append(str(size))
            result.append(',')
        result.append('#')
        result.extend(strs)

        return ''.join(result)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res


