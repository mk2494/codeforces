'''

Problem Link : https://codeforces.com/contest/1407/problem/A

-  Let 𝑐𝑛𝑡0 be the count of zeroes in the array, 𝑐𝑛𝑡1 — count of ones. 

- Then if 𝑐𝑛𝑡1 ≤ 𝑛/2, we remove all ones and alternating sum, obliously, equals 0. 

- Otherwise, 𝑐𝑛𝑡0 < 𝑛/2, we remove all zeroes and if 𝑐𝑛𝑡1 is odd — plus another 1. 

- In this case, alternating sum equals 1−1+1−…−1=0 (because count of remaining ones if even) and we'll remove not more than 𝑐𝑛𝑡0 + 1 ≤ 𝑛/2

'''

def print_ans(N, lst):
	cnt0 = lst.count('0')
	cnt1  = lst.count('1')
	if cnt1 <= N//2:
		print(N//2)
		for _ in range((N//2)):
			print('0', end=' ')
	else:
		cnt = cnt1 if cnt1%2==0 else cnt1-1
		print(cnt)
		for _ in range(cnt):
			print('1', end=' ')

if __name__ == "__main__":

	T = int(input())
	for _ in range(T):
		N = int(input())
		lst = input().split(' ')
		print_ans(N, lst)
		print()