#Sort module   
#David Torpey
          
def quickSort(arr, flag):
    
    less = [];
    equal = [];
    greater = [];
    
    if arr == []: 
        return [];

    if len(arr) > 1:
        pivot = arr[0]
        
	if (flag == "ASC") or (flag == "asc"):
		for i in arr:
            		if i < pivot:
                		less.append(i);
            		if i == pivot:
                		equal.append(i);
            		if i > pivot:
                		greater.append(i);

	if (flag == "DESC") or (flag == "desc"):
        	for i in arr:
            		if i > pivot:
                		less.append(i)
            		if i == pivot:
                		equal.append(i)
            		if i < pivot:
                		greater.append(i)

	return quickSort(less, flag) + equal + quickSort(greater, flag);
    
    else:
        return arr
