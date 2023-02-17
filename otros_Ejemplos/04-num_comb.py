import itertools

if __name__ == '__main__':

	nums = [1, 2, 3, 4]

	permutations = list(itertools.permutations(nums))
	print(permutations)
