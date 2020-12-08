def load_instructions(filename):
	instruct_input = open(filename, "r")
	instructions = [instruction.strip() for instruction in instruct_input]
	return instructions

# modified  from part 1 so now we have an exit condition for game
def exec_game(instructions, cur, acc, seen):
	if cur in seen:
		return False, acc
	elif cur >= len(instructions):
		return True, acc
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
	instructions = load_instructions("instructions.txt")
	flippables = { "nop" : "jmp",
				 "jmp" : "nop"
				}
	for index, instruction in instructions:
		cmd, ops = instruction.split(" ")
		# we know we only need to flip if its a cmd/jmp
		# no point in flipping ops since it'll cause an infinite loop...
		if cmd in flippables  and ops != 0:
			instructions[index] = flippables [cmd] + " " + ops
			ends, acc = exec_game(instructions, 0, 0, set())
			if ends:
				print("Flipped", instruction, "at index", index, "to end game.")
				return acc
			# reset it
			instructions[index] = cmd + " " + ops
	# nothing is flippable
	return float('-inf')


if __name__ == "__main__":
	print("Value of accumulator on a successfully ended game:", test_game())

