def find_triples_in_ledger(target):
	ledger = open("inputs.txt", 'r')
	nums = [int(x.strip()) for x in ledger]
	nums.sort()
	for index, num in enumerate(nums):
		# next we want to find any pairs within the threshold that can sum up to target
		left = index+1
		right = len(nums)-1
		missing_sum = target-num
		while left < right:
			if nums[left] + nums[right] == missing_sum:
				print("Found a triplet", nums[left], nums[right], num)
				return nums[left] * nums[right] * num
			elif nums[left] + nums[right] > missing_sum:
				# if we're bigger
				right -= 1
			elif nums[left] + nums[right] < missing_sum:
				# if we're smaller
				left += 1
	return -1


print(find_triples_in_ledger(2020))