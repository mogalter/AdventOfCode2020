from Python_Day3_Part1_Solution import find_trees

# import previous solution for reuse with new coordinates

def calculate_paths():
	directions = [[1,1], [3,1], [5,1], [7,1], [1,2]]
	result = 1
	for direction in directions:
		trees = find_trees(direction[0], direction[1])
		result *= trees
		print("Found", trees, "for this direction:", direction)
	return result

if __name__ == "__main__":
	print("Multiplied trees:", calculate_paths())