'''
    Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is less than or equal to k.
    
Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105


'''

class Solution:
    def longestSubstring(self, s, k):
        result = 0
        for T in range(1, len(Counter(s))+1):
            beg, end, Found, freq, MoreEqK = 0, 0, 0, [0]*26, 0
            while end < len(s):
                if MoreEqK <= T:
                    s_new = ord(s[end]) - 97
                    freq[s_new] += 1
                    if freq[s_new] == 1:
                        MoreEqK += 1
                    if freq[s_new] == k:
                        Found += 1
                    end += 1
                else:
                    symb = ord(s[beg]) - 97
                    beg += 1
                    if freq[symb] == k:
                        Found -= 1
                    freq[symb] -= 1
                    if freq[symb] == 0:
                        MoreEqK -= 1
                            
                if MoreEqK == T and Found == T:
                    result = max(result, end - beg)
                    
        return result