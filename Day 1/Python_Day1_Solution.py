def find_nums_in_ledger(target):
	ledger = open("inputs.txt", 'r')
	seen = set()
	for line in ledger:
		cur_num = int(line.strip())
		missing_num = target-cur_num
		if missing_num in seen:
			return missing_num*cur_num
		if cur_num not in seen:
			seen.add(cur_num)
	return -1

mult = find_nums_in_ledger(2020)
print(mult)