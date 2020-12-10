from collections import defaultdict# max adaptor jolts is what we want to build towards

def load_jolts(filename):
	jolts = open(filename, "r")
	nums = set()
	for num in jolts:
		nums.add(int(num))
	return nums

def search_adaptor(adaptors, max_jolts):
	three_diff = one_diff = 0
	cur_jolts = 0
	while cur_jolts < max_jolts:
		for potential_jolts in range(cur_jolts+1, cur_jolts+4):
			if potential_jolts in adaptors:
				diff = potential_jolts - cur_jolts
				if diff == 3:
					three_diff += 1
				elif diff == 1:
					one_diff += 1
				cur_jolts = potential_jolts
				break 
	three_diff += 1
	# this is +1 on 3 diff to account for the built-in adaptor
	print("We found", one_diff, "adaptors with a difference of 1-jolt and", 
		three_diff, "adaptors with a difference of 3-jolt")
	return one_diff*three_diff

def search_combinations(adaptors, cur_jolts, max_jolts, seen):
	combos = 0
	if cur_jolts > max_jolts:
		# no way this could work
		return 0
	elif cur_jolts == max_jolts:
		# this is a good combinations
		return 1
	else:
		for potential_jolts in range(cur_jolts+1, cur_jolts+4):
			if potential_jolts in adaptors and potential_jolts not in seen: 
				# we can try this since we've never seen this solution before.
				# cache results so we don't need to recompute potential jolts paths
				seen[potential_jolts] = search_combinations(adaptors, potential_jolts, max_jolts, seen)
				combos += seen[potential_jolts]
			elif potential_jolts in seen:
				# we've already calculated this
				combos += seen[potential_jolts]
	return combos

	 # get it in numerical order!

if __name__ == "__main__":
	# cast to set for quicker access
	adaptors = load_jolts('jolts.txt')
	max_jolts = max(adaptors)
	print("Computed Answer for Part 1:", search_adaptor(adaptors, max_jolts))
	print("Computed number of good combinations for Part 2:", search_combinations(adaptors, 0, max_jolts, {}))
