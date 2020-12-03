def find_trees(right=3, down=1):
	forest_map = open("forest.txt", 'r')
	trees = 0
	forest = []	
	for region in forest_map:
		forest.append(region.strip())
	forest_map.close()
	# we do not count 0,0 so we'll start with the first 3x1 path
	cur_col, cur_row = right, down
	end_of_forest = len(forest)
	end_of_region = len(forest[0])
	# while we're still within the map
	while cur_row < end_of_forest:
		if cur_col >= end_of_region:
			# reset the column since we are out of bounds.
			cur_col -= end_of_region
		# grab current value and check if it's a tree
		if forest[cur_row][cur_col] == '#':
			trees += 1
		cur_row += down
		cur_col += right
	return trees
	
if __name__ == "__main__":
	print("Found trees:", find_trees(3, 1))