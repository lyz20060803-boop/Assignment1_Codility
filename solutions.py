def solution (A, K): 
    
    if not A:  #return the original if array is empty
        return A
    
    n = len(A) 
    
  
    steps = K % n #if times K is greater than the array, just have to switch K % n times
    

    for _ in range(steps):  #pick up the last element each time
      
        last_element = A[-1]
        
       
        for i in range(n - 1, 0, -1):  #move every element back by one position except the last one 
            A[i] = A[i - 1]
            
      
        A[0] = last_element #set last element to the first one
        
    return A





def solution(A):
    bag = set() #create empty set to collect the onr that alone

    for i in A: 
        if i in bag: #if there is same one, remove that
            bag.remove(i)
        else:
            bag.add(i) #if there isn't same one, add
    return bag.pop() #take out the integer in set and return it


def solution(X, Y, D): 
    N = (Y - X) // D  
    if (Y - X) % D != 0: #if there still have distance less than one step
        N = N + 1 #Add one step because can not go half step
    return N  



def solution(A):
    if not A: #if list is empty, it means missed integer 1
        return 1
    N = len(A) #get the lenth of A
    total = (N + 1) * (N + 2) // 2 #the sum if nothing missed
    for i in A: #minus each integer in the list to get which missed
        total = total - i 
    return total



def solution(A): 
    N = len(A)
    left_sum = 0
    right_sum = sum(A) #move all the value to the one side
    min_diff = float('inf') 

    for i in A[:N-1]: #move each number to the left one by one(except last one)
        left_sum += i
        right_sum -= i
        mid_diff = abs(left_sum - right_sum) #calculate the absolute difference
        if mid_diff < min_diff: #when absolute difference get smaller, upload
            min_diff = mid_diff

    return min_diff
