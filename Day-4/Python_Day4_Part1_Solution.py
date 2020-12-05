def find_valid_passports():
	potential_passports = open("passports.txt", "r")
	invalid_passports = 0
	total_passports = 0
	fields = {"byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid", "cid"}
	excludable = {"cid"}
	max_missing_fields = len(fields) - len(excludable)
	current_passport = set()
	for passport_line in potential_passports:
		passport_line = passport_line.strip()
		if passport_line:
			passport_chunks = passport_line.split(" ")
			for chunk in passport_chunks:
				key, value = chunk.split(":")
				if key not in current_passport:
					current_passport.add(key)
		else:
			# since this is a blank we know this is the end of the current passport data
			# clear out current_passport_data
			missing = fields.difference(current_passport) # find what fields we are missing
			missing = missing.difference(excludable) # get rid of cid field if we're missing cid
			total_passports += 1
			if missing:
				print("Passport #: {}".format(total_passports), "is missing:", missing)
				invalid_passports += 1
			current_passport.clear()
			
			# if differ_fields  or is exclude
		# if password line is blank we know that this is end of current passport data
	print(str(total_passports-invalid_passports) + "/" + str(total_passports), "were valid.")

find_valid_passports()