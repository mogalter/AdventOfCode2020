def load_mask_mem(filename):
	mask_mems  = {}
	cur_mask = ""
	with open(filename, "r") as mask_mem:
		for line in mask_mem:
			identifier, value = line.strip().split(" = ")
			if identifier == "mask":
				if identifier not in mask_mems :
					# set cur_mask to value of mask!
					cur_mask = value
					mask_mems[cur_mask] = []
			else:
				identifier_len = len(identifier)
				mem_address = identifier[4:identifier_len-1]
				mask_mems[cur_mask].append((int(mem_address), int(value)))
				# regular memory! mem[value] = numerical
	return mask_mems

def mask_num(mask, num):
	num_bin = str(bin(num))[2:]
	new_num = ""
	match_start = len(mask) - len(num_bin)
	num_bin_idx = 0
	for index, bit in enumerate(mask):
		if index >= match_start:
			if bit != 'X': 
				new_num += bit
			else:
				new_num += num_bin[num_bin_idx]
			num_bin_idx += 1
		elif index < match_start:
			if bit != 'X':
				new_num += bit
			else:
				new_num += '0'
	# converts binary string to integer.
	return int(new_num, 2)

def parse_masking(mask_mems, converter):
	mem = {}
	for mask in mask_mems:
		for mem_of_mask in mask_mems[mask]:
			mem_location, mem_value = mem_of_mask
			if mem_location not in mem:
				mem[mem_location] = 0
			mem[mem_location] = converter(mask, mem_value)
			print("Pre-mask", mem_value, "--> Post-mask", mem[mem_location])
	return sum([mem[loc] for loc in mem])

if __name__ == "__main__":
	mask_mems = load_mask_mem('masks.txt')
	# print(mask_mems)
	print("Sum of all memories:", parse_masking(mask_mems, mask_num))