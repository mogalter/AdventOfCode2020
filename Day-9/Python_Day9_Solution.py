def load_input(filename):
	xmas_input = open(filename, "r")
	nums = [int(num.strip()) for num in xmas_input]
	return nums

def contains_sum(container, target):
	seen = set()
	for num in container:
		want = target-num
		if want in seen:
			return True
		else:
			seen.add(num)
	return False

def find_weakness(container, target):
	# we can do a sliding window to find this - need to figure out how
	# brute force approach
	for index, val in enumerate(container):
		total = 0
		minimum = maximum= container[index]
		while index < len(container):
			minimum = min(minimum, container[index])
			maximum = max(maximum, container[index])
			total += container[index]
			if total == target:
				return maximum + minimum
			elif total > target:
				break
			index += 1
	return float('-inf')

def parse_xmas(preamble_len=5):
	nums = load_input("puzzle.txt")
	index = 0
	while index < len(nums): 
		# we want to search index -> index + preamble_len and find index + preamble len
		if preamble_len > len(nums)-index:
			# if theres less indexes left to check than preamble
			target = len(nums)-1
		else:
			target = index + preamble_len
		if not contains_sum(nums[index:target], nums[target]):
			print(nums[target], "is not the sum of the previous", preamble_len, "numbers.")
			weakness = find_weakness(nums, nums[target])
			print("Found a weakness of", weakness)
			return weakness
		index += 1

	return float('-inf')

if __name__ == "__main__":
	violator = parse_xmas(25)
	pass
