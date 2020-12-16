def load_init_nums(filename):
	init_order =  {}
	with open(filename, "r") as init_nums:
		nums = init_nums.readline().strip().split(",")
		for turn, num in enumerate(nums):
			turn = int(turn) + 1
			num = int(num)
			init_order[num] = turn
		# return next number
		return num, init_order

def chant_numbers(prev_num: int, chanted: dict, limit: int):
	turn = chanted[prev_num] + 1
	next_to_chant = 0
	# 4th turn, chanted 0
	while turn < limit:
		if next_to_chant in chanted:
			# case in which we've seen this
			last_announced = chanted[next_to_chant]
			chanted[next_to_chant] = turn
			next_to_chant = turn - last_announced
		else:
			chanted[next_to_chant] = turn
			next_to_chant= 0
		turn += 1
	return next_to_chant

if __name__ == "__main__":
	prev_num, init_nums = load_init_nums("sample.txt")
	limit = 30000000
	last_to_chant = chant_numbers(prev_num, init_nums, limit)
	print("The last number to chant is", last_to_chant)

