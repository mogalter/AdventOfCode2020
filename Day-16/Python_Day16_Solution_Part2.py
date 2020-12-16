def load_tickets(filename):
	criterias = {}
	ticket_collection = {}
	# keeping it all seperated just in case.
	with open(filename, "r") as tickets:
		for information in tickets:
			information = information.strip()
			if not information:
				break
			descriptor_bundle = information.split(":")
			descriptor, req_value = descriptor_bundle
			ranges_string = req_value.split("or")
			if descriptor not in criterias:
				criterias[descriptor] = []
			for raw_ranges in ranges_string:
				raw_ranges = raw_ranges.strip().split("-")
				actual_range = map(lambda x: int(x), raw_ranges)
				criterias[descriptor].append(list(actual_range))
		# now process your tickets
		tag = tickets.readline().strip()
		raw_tickets = tickets.readline().strip()
		while raw_tickets:
			if tag not in ticket_collection:
				ticket_collection[tag] = []
			ticket_collection[tag].append(list(map(lambda x: int(x), raw_tickets.split(","))))
			raw_tickets = tickets.readline().strip()

		# process nearby tickets
		nearby_tag = tickets.readline().strip()
		raw_tickets = tickets.readline().strip()
		while raw_tickets:
			if nearby_tag not in ticket_collection:
				ticket_collection[nearby_tag] = []
			ticket_collection[nearby_tag].append(list(map(lambda x: int(x), raw_tickets.split(","))))
			raw_tickets = tickets.readline().strip()
	return criterias, ticket_collection

if __name__ == "__main__":
	criterias, ticket_collection = load_tickets("sample.txt")
	print(criterias, ticket_collection)