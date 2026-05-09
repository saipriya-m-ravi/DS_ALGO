import sys
sys.setrecursionlimit(10**6)


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def merge(self,A,B):
	    dh=ListNode(0)
	    ptr=dh

	    while (A!=None and B!=None):
	        if A.val<=B.val:
	            ptr.next=A
	            A=A.next
	            ptr.next.next=None
	            ptr=ptr.next
	        else:
	            ptr.next=B
	            B=B.next
	            ptr.next.next=None
	            ptr=ptr.next
	    
	    if A!=None:
	        ptr.next=A
	    
	    if B!=None:
	        ptr.next=B

	    return dh.next
	    
	def sortList(self, A):
	    if A==None or A.next==None:
	        return A
	        
	    slow,fast=A,A
	    
	    while(fast.next and fast.next.next):
	        fast=fast.next.next
	        slow=slow.next
	        
	    B=slow.next
	    slow.next=None

	    left=self.sortList(A)
	    right=self.sortList(B)
	    
	    A=self.merge(left,right)
	    return A
