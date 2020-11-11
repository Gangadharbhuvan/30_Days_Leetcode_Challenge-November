'''
	Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
 
	
'''

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        if p1 == p2 == p3 == p4: return False

        p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
        if p2[1] < p3[1]: p2,p3 = p3,p2

        return p3 == [p1[0] + (p2[1]-p1[1]), p1[1] - (p2[0]-p1[0])]\
           and p4 == [p2[0] + (p2[1]-p1[1]), p2[1] - (p2[0]-p1[0])]        