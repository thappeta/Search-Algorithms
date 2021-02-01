'''

Binary Search algorithm by Surya Prathap Reddy


'''
def binarysearch(array,element):
	start=0
	end=len(array)-1
	
	while (start<=end):
		
		mid=(start+end)//2
		
		midvlaue=array[mid]
		
		if(array[mid]==element):
			
			return mid
		
		elif element<midvlaue:
			
			end=mid-1
		
		else:
			start=mid+1
		
		return None
		
a=[1,2,3,4,5,6,7,8]
n=9

print(binarysearch(a,n))	
