char = ["d","a","b","c","g","e","f",]
integer = [3,5,1,6,2,7,8,10,9]
floats = [2.1,3.5,1.1,5.6,2.6,1,0]
word = ["banana","apple","mango","cherry","date"]


def sorts(index , reverse=False):
    x = len(index) # the len will find the length of the index. 
    for i in range(x): 
        if not reverse: # it check to the user want ascending or descending order
            min_idx = i
            for j in range(i+1,x):
                if index[j] < index[min_idx]:
                    min_idx = j
            index[i],index[min_idx] = index[min_idx],index[i] # swaping the value of index[i] with index[min_idx] and index[min_idx] with index[i].
        else:
            max_idx = i
            for j in range(i+1,x):
                if index[j] > index[max_idx]:
                    max_idx = j
            index[i],index[max_idx] = index[max_idx],index[i]
    return index

    
print(sorts(char))
print(sorts(integer))
print(sorts(floats))
print(sorts(word))