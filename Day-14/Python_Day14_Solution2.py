from Python_Day14_Solution import load_mask_mem

# creates the binary number post-masking
def mask_num(mask, num):
	num_bin = str(bin(num))[2:]
	new_num = []
	match_start = len(mask) - len(num_bin)
	num_bin_idx = 0
	for index, bit in enumerate(mask):
		if bit == 'X':
			if index >= match_start:
				num_bin_idx += 1
			new_num.append('X')
		elif index >= match_start:
			if bit == "0":
				# simply bring down the bin
				new_num.append(num_bin[num_bin_idx])
			else:
				new_num.append('1')
			num_bin_idx += 1
		else:
			new_num.append(bit)
	# converts binary string to integer.
	return new_num

# recursive function generates all possible "X" replacements!
def mem_gen(mem_address, index):
	outputs = []
	if index >= len(mem_address):
		# we've reached the end.
		return [mem_address]
	elif mem_address[index] != 'X':
		# if not "X", continue going through the mem address
		return mem_gen(mem_address, index+1)
	else:
		# if X, start flipping
		for bit in ('0', '1'):
			for result in mem_gen(mem_address[:index] + [bit] + mem_address[index+1:], index+1):
				outputs.append(result)
	return outputs

def parse_masking(mask_mems):
	mem = {}
	for mask in mask_mems:
		for mem_of_mask in mask_mems[mask]:
			mem_location, mem_value = mem_of_mask
			mem_address = mask_num(mask, mem_location)
			# takes all possible mem addresses and converts it to decimal!
			possible_addresses = [int("".join(mem_addr),2) for mem_addr in mem_gen(mem_address, 0)]
			for address in possible_addresses:
				if mem_location not in mem:
					mem[mem_location] = 0
				mem[address] = mem_value
	return sum([mem[loc] for loc in mem])


if __name__ == "__main__":
	mask_mems = load_mask_mem('masks.txt')
	total = parse_masking(mask_mems)
	print("Sum of all memory addresses for part II:", total)