class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, A):
        candies = [1]*len(A)
        for i in range(1,len(A)):
            if A[i-1]<A[i]:
                candies[i] = candies[i-1]+1
        
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)

            