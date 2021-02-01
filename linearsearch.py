'''
Linear Searching algorithm by Surya Prathap Reddy
Time Complexity:O(N)
Space Complexity:O(1)
'''


def search(arr, x): 

	for i in range(len(arr)): 

		if arr[i] == x: 
			return i 

	return -1

	
a=[12,20,30,50,40,64]
n=64

print(search(a,n))
  
