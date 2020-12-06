def extract_answers_groups(answers_group_fs):
    cur_group = []
    all_groups = []
    for answer in answers_group_fs:
        answer = answer.strip()
        if answer:
            cur_group.append(answer)
        else:
            all_groups.append(cur_group)
            cur_group = []
    if cur_group: # if values still exist in cur_group :)
        all_groups.append(cur_group)
    return all_groups

def find_all_qa_sum():
    question_answers = open("question_answers.txt", "r")
    answers_groups = extract_answers_groups(question_answers)
    total = 0
    for answer_group in answers_groups:
        agreed_answers = set()
        for index, answer in enumerate(answer_group):
            person_answer = set(answer)
            if not agreed_answers and index == 0: 
                # only set empty agreed set if first iteration
                # we want to keep post-intersection sets even if they are empty!
                agreed_answers = person_answer
            else:
                agreed_answers = agreed_answers.intersection(person_answer)
        total += len(agreed_answers)
    return total

print("We picked up a total of", find_all_qa_sum(), "yes answers!")