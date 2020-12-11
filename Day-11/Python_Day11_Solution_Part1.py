def load_seats(filename):
	seats_input = open(filename, "r")
	seating_placements = []
	# preemptively fill the seats
	for seat_row in seats_input:
		seat_row = seat_row.strip()
		seating_placements.append(list(seat_row))
	return seating_placements

def is_flippable(adj_seats, cur_seat):
	occupied_adj_seats = len(adj_seats)
	# check for adjacent seats
	# if there are 4 or more adjacent seats, empty it
	if occupied_adj_seats >= 4 and cur_seat == "#":
		return True
	# if there are no adj seats, flip!
	elif occupied_adj_seats == 0 and cur_seat == "L":
		return True
	# if all cases fail, we will not flip.
	return False

def find_adj_seats(seating_placements, cur_seat_row, cur_seat_col):
	adj_seats = []
	row_len = len(seating_placements)
	col_len = len(seating_placements[cur_seat_row])
	for row in range(cur_seat_row-1, cur_seat_row+2):
		if 0 <= row < row_len:
			for col in range(cur_seat_col-1, cur_seat_col+2):
				if 0 <= col < col_len:
					cur_seat = seating_placements[row][col]
					if  (cur_seat_row, cur_seat_col) != (row, col) and cur_seat == "#" :
						adj_seats.append(cur_seat)
	return adj_seats

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
			adj_seats = find_adj_seats(seating_placements, row, col)
			if seat != "." and is_flippable(adj_seats, cur_seat):
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
