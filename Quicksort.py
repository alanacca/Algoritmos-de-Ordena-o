def Quicksort(alist,comeco,fim):
	posPivo = 0
	if(comeco<fim):
		posPivo = partir(alist,comeco,fim)

		Quicksort(alist,comeco,posPivo-1)
		Quicksort(alist,posPivo+1,fim)


def partir(alist,comeco,fim):
	pivo = alist[comeco]
	c = comeco+1
	f = fim

	while(c <= f):
		if (alist[c] <= pivo):
			c += 1
		elif (pivo < alist[f]):
			f -= 1
		else:
			troca = alist[c]
			alist[c] = alist[f]
			alist[f] = troca
			++c
			--f
	alist[comeco] = alist[f]
	alist[f] = pivo
	return f

alist = [2,6,1,4,3,5]
#print(len(alist))
Quicksort(alist,0,len(alist)-1)
print("alista:",alist)