def get_mid(start, end):
	return (start+end)//2

def find_seats():
	seat_ids = open("seating.txt", "r")
	rows = 128
	cols = 7
	boarded = []
	for seating_instruct in seat_ids:
		seating_instruct = seating_instruct.strip()
		rows_end = rows
		rows_start = 0
		cols_end = cols
		cols_start = 0
		for step in seating_instruct:
			if step == "F":
				# take lower half
				rows_end = get_mid(rows_start, rows_end)
			elif step == 'B':
				# take upper half
				rows_start = get_mid(rows_start, rows_end)
			elif step == 'R':
				# take upper half
				cols_start = get_mid(cols_start, cols_end)
			elif step =='L':
				cols_end = get_mid(cols_start, cols_end)
		row = min(rows_start, rows_end)
		col = max(cols_start, cols_end)
		# add seat ID to records
		boarded.append(row*8+col)
	# start search for my seat, first sort to make finding consecs easier!
	boarded = sorted(boarded)
	seat_index = 1
	while seat_index < len(boarded):
		prev_seat = boarded[seat_index-1]
		cur_seat = boarded[seat_index]
		if cur_seat  == prev_seat+2:
			print("The previous seat on the pass was", prev_seat)
			print("The current seat on the pass is", cur_seat)
			return get_mid(cur_seat, prev_seat)
		seat_index += 1
	

print("My seat ID is:", find_seats())

# looking for what seats were not taken