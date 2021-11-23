def Horspool(P,T):
	m = len(P)
	n = len(T)

	Shift = [m] * 256

	for j in range(m-1):
		Shift[ord(P[j])] = m - j - 1

	i = m - 1
	while i < n:
		k = 0
		while T[i - k] == P[m - 1 - k] and k < m:
			k += 1
		if k == m:
			return i - m + 1
		else:
			i = i + Shift[ord(T[i])]
	return -1

if __name__ == "__main__":
	P = "feel"
	T = "I am a programmer, and I am feeling good."
	print(Horspool(P,T))