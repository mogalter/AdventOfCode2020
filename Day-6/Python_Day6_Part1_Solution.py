def find_qa_sum():
	question_answers = open("question_answers.txt", "r")
	group_ans_set = set()
	total_yes = 0
	for answers in question_answers:
		answers = answers.strip()
		if answers:
			# case in which line has a value
			# we add each distinct yes into a group
			for answer in answers:
				if answer not in group_ans_set:
					group_ans_set.add(answer)
		else:
			# add len(group_ans_set to total_yes) and
			# clear out the current group_ans_set 
			total_yes += len(group_ans_set)
			group_ans_set.clear()
	return total_yes

print("We picked up a total of", find_qa_sum(), "yes answers!")