def load_bus_times(filename):
	with open(filename, "r") as bus_schedule:
		depart_time = bus_schedule.readline().strip()
		return int(depart_time), bus_schedule.readline().split(",")

def get_earliest_bus(depart_time, buses):
	min_time = float('inf')
	min_bus = float('inf')
	for bus in buses:
		if bus != "x":
			bus = int(bus)
			bus_rounds = (depart_time//bus)+1
			time_for_bus = bus_rounds*bus-depart_time
			min_time = min(time_for_bus, min_time)
			if min_time == time_for_bus:
				min_bus = int(bus)
	return min_time * min_bus

# Brute Force
# def get_subsequent_departures(buses):
# 	counter, base_bus = 7*(100000000000000//7+1), int(buses[0])
# 	continue_loop, has_answer = True, True
# 	while continue_loop:
# 		counter += base_bus
# 		for offset, bus in enumerate(buses[1:]):
# 			if bus != "x":
# 				bus = int(bus)
# 				if (counter + offset + 1) % bus != 0:
# 					# not an answer
# 					# print("Break at", counter)
# 					has_answer = False
# 					break
# 		if has_answer:
# 			print(counter)
# 			return counter
# 		has_answer = True
# 		# increment offset

def get_subsequent_departures(buses, start_time):
	base_time = start_time
	lcm = 1
	for offset, bus in enumerate(buses):
		if bus != "x":
			bus = int(bus)
			while (base_time  + offset) % bus != 0:
				base_time += lcm
			lcm *= bus
	return base_time

if __name__ == "__main__":
	print("Executing...")
	depart_time, buses = load_bus_times("inputs.txt")
	# part_one_answer = get_earliest_bus(depart_time, buses[:2])
	print(get_subsequent_departures(buses, 100000000000000))