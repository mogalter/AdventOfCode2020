from Python_Day11_Solution_Part1 import load_seats

def is_flippable(occupied_seats, cur_seat):
	# Also, people seem to be more tolerant than you expected: 
	# it now takes five or more visible occupied seats for an occupied seat to become empty 
	occupied_all_seats = occupied_seats.count('#')
	# check for adjacent seats
	# if there are 4 or more adjacent seats, empty it
	if occupied_all_seats >= 5 and cur_seat == "#":
		return True
	# if there are no adj seats, flip!
	elif occupied_all_seats == 0 and cur_seat == "L":
		return True
	# if all cases fail, we will not flip.
	return False

# instead of adjacent seat, we want to search until we find a seat
def find_occupied_seats(seating_placements, cur_seat_row, cur_seat_col):
	occupied_seats = []
	row_len = len(seating_placements)
	col_len = len(seating_placements[cur_seat_row])
	adj_adjustments = [(row_adj, col_adj) for row_adj in [-1, 0, 1] for col_adj in [-1, 0, 1]]
	for adjustment in adj_adjustments:
		row_adj, col_adj = adjustment
		row, col = cur_seat_row + row_adj, cur_seat_col + col_adj
		while 0 <= row < row_len and 0 <= col < col_len:
			if row_adj == 0 and col_adj == 0:
				# don't want an inf loop, break
				break
			cur_seat = seating_placements[row][col]
			# print(cur_seat, row, col)
			if cur_seat != ".":
				# hey look, it's an available seat!
				occupied_seats.append(cur_seat)
				break
			row += row_adj
			col += col_adj
	return occupied_seats

def do_shuffle(seating_placements):
	to_flip = []
	flip_map = {
		"#" : "L",
		"L" : "#"
	}
	# keep a track of occupied seats
	occupied = 0
	for row, seat_row in enumerate(seating_placements):
		for col, seat in enumerate(seat_row):
			# generate seats to check
			cur_seat = seating_placements[row][col]
			if cur_seat == "#":
				occupied += 1
			occupied_seats = find_occupied_seats(seating_placements, row, col)
			if seat != "." and is_flippable(occupied_seats, cur_seat):
				to_flip.append((row,col))

	for coord in to_flip:
		row, col = coord
		cur_val = seating_placements[row][col]
		if cur_val == "#":
			occupied -= 1
		else:
			occupied += 1
		seating_placements[row][col] = flip_map[cur_val]
	if to_flip:
		return occupied, True
	return occupied, False

if __name__ == "__main__":
	seating_placements = load_seats("seating.txt")
	occupied, continue_shuffle = do_shuffle(seating_placements)
	while continue_shuffle:
		occupied, continue_shuffle = do_shuffle(seating_placements)
	print(occupied, "seats are occupied on the last run.")
