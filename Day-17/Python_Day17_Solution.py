    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
    # Otherwise, the cube becomes inactive.
    # If a cube is inactive but exactly 3 of its neighbors are active, 
    # the cube becomes active. Otherwise, the cube remains inactive.

def load_cubes(filename):
	# this is our center slice! Generating cubes for z_coord = 0
	with open(filename, "r") as cubes: 
		return [line.strip() for line in cubes]

def gen_init_state(init_cubes, dimensions):
	# all dimensions start with 0.
	on_cubes = set()
	for x, cube_row in enumerate(init_cubes):
		for y, cube in enumerate(cube_row):
			if cube == "#":
				coord = tuple([x,y] + [0]*(dimensions-2))
				# if it's 3D, we get 3 coord, 4D 4 coords etc... all starts at 0
				on_cubes.add(coord)
	return on_cubes

def get_displacements():
	displacements = []
	displacement_values = [-1,0,1]
	for x_displace in displacement_values:
		for y_displace in displacement_values:
			for z_displace in displacement_values:
				displacements.append((x_displace, y_displace, z_displace))
	return displacements

def get_displacements_4D():
	displacements = []
	displacement_values = [-1,0,1]
	for x_displace in displacement_values:
		for y_displace in displacement_values:
			for z_displace in displacement_values:
				for w_displace in displacement_values:
					displacements.append((x_displace, y_displace, z_displace, w_displace))
	return displacements

def unfold_via_cycle(on_cubes, displacements, cycles):
	# we want to unfold a cycle amount of times!
	for cycle_count in range(cycles):
		surrounding = {}
		for coord in on_cubes:
			for displace_val in displacements:
				new_coord = tuple(map(sum, (zip(coord, displace_val))))
				# zip creates seperate tuples with each coord bundled with it's displacement
				if new_coord != coord:
					if new_coord not in surrounding:
						# new coordinate has not been seen yet.
						surrounding[new_coord] = 1
					else:
						# we've seen this again, since we're displacing on, 
						# on is a neighbor of this. :)
						surrounding[new_coord] += 1
		# we want: stuff that stays on, and stuff we need to turn on
		# Surrounding keeps a track of how many ons are nearby.
		# we want all 2-3 repetitions from surroundings
		keep_on = set()
		for cube in on_cubes:
			if cube in surrounding and surrounding[cube] in [2,3]:
				keep_on.add(cube)
		flip = set()
		for cube in surrounding:
			if surrounding[cube] == 3:
				flip.add(cube)
		# combine everything that needs to be kept on.
		keep_on.update(flip)
		on_cubes = keep_on
	return len(on_cubes)

if __name__ == "__main__":
	init_cubes = load_cubes("input.txt")
	# part 1. we will keep a track of all cubes that stay on.
	on_cubes = gen_init_state(init_cubes, 3)
	print("At the end of 6 cycles for a 3D run... we have", unfold_via_cycle(on_cubes, get_displacements(), 6), "cubes")
	fourD_on = gen_init_state(init_cubes, 4)
	fourD_displacement = get_displacements_4D()
	fourD_on_count = unfold_via_cycle(fourD_on, fourD_displacement, 6)
	print("At the end of 6 cycles for a 4D run... we have", fourD_on_count, "cubes")