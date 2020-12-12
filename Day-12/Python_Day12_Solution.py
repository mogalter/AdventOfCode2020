def load_instructions(filename):
	with open(filename, "r") as instructions:
		return [instruction.strip() for instruction in instructions]


def gen_ship_state(north=0, south=0, east=0, west=0, rotation=0, direction="E"):
	return {
		"N" : north,
		"S" : south,
		"E" : east,
		"W" : west,
		"rotation" : rotation,
		"direction" : direction,
	}

def steer_ship(ship_state, rotations, instructions):
	for instruction in instructions:
		direction, distance = instruction[0], int(instruction[1:])
		# right +90. left = -90
		ship_direction, ship_rotation = ship_state["direction"], ship_state["rotation"]
		if direction == "F":
			# move forward in our direction
			ship_state[ship_direction] += distance
		elif direction in ("R", "L"):
			if direction == "R":
				ship_state["rotation"] = (ship_rotation+distance)%360
			else:
				ship_state["rotation"] = (360+ship_rotation-distance)%360
			ship_state["direction"] = rotations[ship_state["rotation"]]
		else:
			# simply add to the value of ship if it's a simply NWES direction.
			ship_state[direction] += distance
	return abs(ship_state["N"] - ship_state["S"]) + abs(ship_state["E"] - ship_state["W"])

if __name__ == "__main__":
	instructions = load_instructions("instructions.txt")
	ship_state = gen_ship_state()
	rotations = {
		0 : "E",
		90 : "S",
		180 : "W",
		270 : "N",
	}
	man_dist = steer_ship(ship_state, rotations, instructions)
	print("Based on a non-waypoint calculation, the manhattan distance is: {}.".format(man_dist))