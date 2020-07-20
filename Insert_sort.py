def Insert_sort(alist):
	for i in range (1,len(alist)):
		elem = alist[i]
		j = i-1
		while(j>=0 and (elem<alist[j])):
			alist[j+1] = alist[j]
			j = j - 1
		alist[j+1] = elem