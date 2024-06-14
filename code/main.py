# link to ex https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        ans, i, j = 0, 0, 0
        while i < n and j < n:
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                char_set.remove(s[i])
                i += 1
        return ans            

if __name__ == "__main__":
    s = ""
    answer = Solution.lengthOfLongestSubstring(Solution, s)
    print(answer)