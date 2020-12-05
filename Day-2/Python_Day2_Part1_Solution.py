def find_valid_passwords():
	valid_count = 0
	corrupted_passwords = open("inputs.txt", "r")
	for line in corrupted_passwords:
		components = line.strip().split(" ")
		low_range, high_range = map(lambda x: int(x), components[0].split("-"))
		letter = components[1][0]
		corrupted = components[-1]
		letter_count = 0
		for char in corrupted:
			if char == letter:
				letter_count += 1
			if letter_count > high_range: # we break because this password is not valid
				break
		if low_range <= letter_count <= high_range: # in range of valid password
			valid_count += 1 
	return valid_count

print("Valid passwords:", find_valid_passwords())