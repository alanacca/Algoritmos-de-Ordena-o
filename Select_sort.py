def Select_sort(alist):
	for i in range (0,(len(alist)-1)):
		minus = i
		for j in range(i+1,len(alist)):
			if alist[j]<alist[minus]:
				minus = j
			
		temp = alist[minus]
		alist[minus] = alist[i]
		alist[i] = temp
