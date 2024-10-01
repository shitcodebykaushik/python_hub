
def findLongestConseqSubseq(arr, n):

	S = set();
	for i in range(n):
		S.add(arr[i]);


	ans = 0;
	for i in range(n):
		
		
		if S.__contains__(arr[i]):
			
			
			j = arr[i];
			
			
			while(S.__contains__(j)):
				j += 1;

		
			ans = max(ans, j - arr[i]);
	return ans;


if __name__ == '__main__':
	arr = [ 1, 94, 93, 1000, 5, 92, 78 ];
	n = len(arr);
	print(findLongestConseqSubseq(arr, n));
