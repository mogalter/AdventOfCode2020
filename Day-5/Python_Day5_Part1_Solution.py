def get_mid(start, end):
	return (start+end)//2

def find_seats():
	seat_ids = open("seating.txt", "r")
	highest_seat = float('-inf')
	rows = 128
	cols = 7
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
		col= max(cols_start, cols_end)
		print("Detected Seat - R:", row, "C:", col)
		highest_seat = max(row*8+col, highest_seat)
	return highest_seat

print("The highest seat ID is:", find_seats())