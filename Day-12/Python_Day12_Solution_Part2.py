from Python_Day12_Solution import load_instructions, gen_ship_state

def waypoint_steer(ship_state, waypoints, rotations, instructions):
	direction_to_degree = {rotations[k]: k for k,v in rotations.items()}
	for instruction in instructions:
		direction, distance = instruction[0], int(instruction[1:])
		if direction == "F":
			for waypoint in waypoints:
				ship_state[waypoint] += waypoints[waypoint]*distance
		elif direction in ("R", "L"):
			# get all non-0 values for flipping and track what's been flipped.
			flippables = {waypoint:waypoints[waypoint] for waypoint in waypoints if waypoints[waypoint]} 
			already_flipped = set()
			# if we've already flipped the value we're trying to flip we want to retain it's value
			for flippable in flippables:
				if direction == "R":
					flipped_degrees = (direction_to_degree[flippable]+distance)%360
				else:
					flipped_degrees = (360+direction_to_degree[flippable]-distance)%360
				flipped = rotations[flipped_degrees]

				flippable_val = waypoints[flippable] if flippable in already_flipped else 0
				waypoints[flippable], waypoints[flipped] = flippable_val, flippables[flippable]
				already_flipped.add(flipped)
		else:
			waypoints[direction] += distance
	return abs(ship_state["N"] - ship_state["S"]) + abs(ship_state["E"] - ship_state["W"])


if __name__ == "__main__":
	instructions = load_instructions("instructions.txt")
	ship_state = gen_ship_state()
	waypoint_ship_state = gen_ship_state()
	waypoints = {
		"N" : 1,
		"S" : 0,
		"E" : 10,
		"W" : 0,
	}
	rotations = {
		0 : "E",
		90 : "S",
		180 : "W",
		270 : "N",
	}
	wp_man_dist = waypoint_steer(waypoint_ship_state, waypoints, rotations, instructions)
	print("For a waypoint calculation, the manhattan distance is: {}.".format(wp_man_dist))