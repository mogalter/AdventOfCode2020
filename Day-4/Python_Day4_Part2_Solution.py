def check_fields(fields):
	byr = int(fields['byr'])
	iyr = int(fields['iyr'])
	eyr = int(fields['eyr'])
	hgt_denom_i = len(fields['hgt'])-2
	hgt, hgt_denom = int(fields['hgt'][:hgt_denom_i]), fields['hgt'][hgt_denom_i:]
	hcl = fields['hcl']
	ecl = fields['ecl']
	pid = fields['pid']
	if not (1920 <= byr <= 2002):
		print("BYR:", byr, "is invalid")
		return False
	elif not (2010 <= iyr <= 2020):
		print("IYR:", iyr, "is invalid")
		return False
	elif not( 2020 <= eyr <= 2030):
		print("EYR:", eyr, "is invalid")
		return False
	elif len(pid) != 9:
		print("PID:", pid, "is not the required length of 9. Detected len:", len(pid))
		return False
	elif ecl not in {'amb', 'blu', 'brn',  'gry', 'grn', 'hzl', 'oth'}:
		print("ECL:", ecl, "is invalid because it is not a recognized color")
		return False
	if hgt_denom in {'cm', 'in'}:
		if hgt_denom == 'cm' and not (150 <= hgt <= 193):
			print("HGY in cm", hgt, "is not valid")
			return False
		elif hgt_denom == 'in' and not (59 <= hgt <= 76):
			print("HGY in inches", hgt, "is not valid")
			return False
	else:
		return False
	if hcl[0] == '#' and len(hcl)-1 == 6:
		# use ascii conversions
		for hcl_i in range(1, len(hcl)):
			ascii_val = ord(hcl[hcl_i])
			if not ((61 <= ascii_val <= 146) or (48 <= ascii_val <= 57)):
				print("HCL", hcl, "has an invalid character")
				return False
		return True
	return False



def find_valid_passports():
	potential_passports = open("passports.txt", "r")
	valid_passports = 0
	total_passports = 0
	fields = {"byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid", "cid"}
	excludable = {"cid"}
	max_missing_fields = len(fields) - len(excludable)
	current_passport = {}
	for passport_line in potential_passports:
		passport_line = passport_line.strip()
		if passport_line:
			passport_chunks = passport_line.split(" ")
			for chunk in passport_chunks:
				key, value = chunk.split(":")
				if key not in current_passport:
					current_passport[key] = value
		else:
			# since this is a blank we know this is the end of the current passport data
			# clear out current_passport_data
			missing = fields.difference(current_passport) # find what fields we are missing
			missing = missing.difference(excludable) # get rid of cid field if we're missing cid
			total_passports += 1
			if not missing and check_fields(current_passport):
				valid_passports += 1
			current_passport.clear()
			
			# if differ_fields  or is exclude
		# if password line is blank we know that this is end of current passport data
	print(str(valid_passports) + "/" + str(total_passports), "were valid.")

find_valid_passports()