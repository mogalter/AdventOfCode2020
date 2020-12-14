def load_bus_times(filename):
	with open(filename, "r") as bus_schedule:
		depart_time = bus_schedule.readline().strip()
		return int(depart_time), bus_schedule.readline().split(",")

def calc_earliest_time(depart_time, buses):
	min_time = float("inf")
	wanted_bus = float("inf")
	for bus in buses:
		if bus != "x":
			bus = int(bus)
			time_diff = bus-(depart_time%bus)
			min_time = min(min_time, time_diff)
			if min_time == time_diff:
				wanted_bus = bus
			print("Last departure for", bus, "was", time_diff, "minutes ago")
	return min_time*wanted_bus


if __name__ == "__main__":
	depart_time, bus_schedule = load_bus_times("sample.txt")
	print(calc_earliest_time(depart_time, bus_schedule))