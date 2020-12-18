from collections import defaultdict

def load_exps(filename):
	# load all expressions
	with open(filename, "r") as exps: 
		return [exp.strip().replace(" ", "") for exp in exps]

def eval_stack_top(nums, ops):
	left, right = nums.pop(), nums.pop()
	total = str(eval(left + ops.pop() + right))
	nums.append(total)

def solve_exp(exp, ops_weights):
	nums, ops = [], []
	for part in exp:
		if part.isdigit():
			nums.append(part)
		elif part == "(":
			# opening parens, simply add
			ops.append("(")
		elif part == ")":
			# perform stack evaulation until "("
			while len(ops) > 0 and ops[-1] != "(":
				eval_stack_top(nums, ops)
			ops.pop()
		elif part in ops_weights:
			if len(ops) > 0 and ops_weights[part] <= ops_weights[ops[-1]]:
				eval_stack_top(nums, ops)
			ops.append(part)
	while ops:
		# finish evaluating for leftover numbers
		eval_stack_top(nums, ops)
	return int(nums.pop())

if __name__ == "__main__":
	exps = load_exps("homework.txt")
	ops_weights = defaultdict(lambda: 0)
	ops_weights["+"], ops_weights["*"] = 1, 1
	total = 0 
	# part 1
	print("Here's to part 1:")
	for exp in exps:
		ans = solve_exp(exp, ops_weights)
		total += ans
		print("Evaluating", exp, "yielded", ans)
	print("Computed total for addition and multiplication equally weighted:", total)

	# part 2
	print("Moving onto part 2:")
	ops_weights["+"], ops_weights["*"] = 2, 1
	p2_total = 0 
	for exp in exps:
		ans = solve_exp(exp, ops_weights)
		p2_total += ans
		print("Evaluating", exp, "yielded", ans)
	print("Computed total for addition weighted more than multiplication:", p2_total)