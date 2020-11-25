'''
    Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''

class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        pre = cur = res = 0
        for c in s+'+':
            if c.isdigit():
                cur = 10*cur + int(c)
            elif c != ' ':
                if op == '+' or op == '-': 
                    res += pre
                    pre = cur if op == '+' else -cur
                else:
                    pre = pre*cur if op == '*' else int(pre/cur)
                cur, op = 0, c
        return res+pre