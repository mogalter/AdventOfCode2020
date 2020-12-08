def load_instructions(filename):
	instruct_input = open(filename, "r")
	instructions = [instruction.strip() for instruction in instruct_input]
	return instructions

# guaranteed to infinite loop, so we break once we reached a visited instruct
def exec_game(instructions, cur, acc, seen):
	if cur in seen:
		return acc
	else:
		cmd, ops =  instructions[cur].split(" ")
		seen.add(cur)
		if cmd == "nop":
			# simply increment cur if no operations are required.
			cur += 1
		elif cmd == "acc":
			# add to accumulator and increment
			acc += int(ops)
			cur += 1
		elif cmd == "jmp":
			cur += int(ops)
		return exec_game(instructions, cur, acc, seen)

def test_game():
	acc = 0
	instructions = load_instructions("instructions.txt")
	seen = set()
	return exec_game(instructions, 0, acc, seen)

if __name__ == "__main__":
	print("Value of accumulator on loop #2:", test_game())