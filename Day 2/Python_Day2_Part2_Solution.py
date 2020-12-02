# in the second part of the problem, low range and high range now desribe a problem position
# Note: corporate has no concept of 0 index so we need to adjust the indexes ourselves!
# Only one position can contain the letter. if both or no positions contain the letter, it's a bust!

def find_valid_passwords():
	valid_count = 0
	corrupted_passwords = open("inputs.txt", "r")
	for line in corrupted_passwords:
		components = line.strip().split(" ")
		first_pos, second_pos = map(lambda x: int(x)-1, components[0].split("-"))
		letter = components[1][0]
		corrupted = components[-1]
		first_letter = corrupted[first_pos]
		second_letter = corrupted[second_pos]
		single_letter_match = (first_letter == letter or second_letter == letter)
		if first_letter != second_letter and single_letter_match: # first letter matches
			valid_count += 1
			print(corrupted, "is valid")
	return valid_count

print("Valid passwords:", find_valid_passwords())

