from queue import PriorityQueue

def load_tickets(filename):
	criterias = {}
	ticket_collection = {}
	# keeping it all seperated just in case.
	with open(filename, "r") as tickets:
		for row, information in enumerate(tickets):
			information = information.strip()
			if not information:
				break
			descriptor_bundle = information.split(":")
			descriptor, req_value = descriptor_bundle
			ranges_string = req_value.split("or")
			if descriptor not in criterias:
				criterias[(descriptor, row)] = set()
			for raw_ranges in ranges_string:
				raw_ranges = raw_ranges.strip().split("-")
				actual_range = map(lambda x: int(x), raw_ranges)
				criterias[(descriptor, row)].add(tuple(actual_range))

		# now process your tickets
		tag = tickets.readline().strip()
		raw_tickets = tickets.readline().strip()
		while raw_tickets:
			ticket_collection[tag] = tuple(map(lambda x: int(x), raw_tickets.split(",")))
			raw_tickets = tickets.readline().strip()

		# process nearby tickets
		nearby_tag = tickets.readline().strip()
		raw_tickets = tickets.readline().strip()
		while raw_tickets:
			if nearby_tag not in ticket_collection:
				ticket_collection[nearby_tag] = set()
			ticket_collection[nearby_tag].add(tuple(map(lambda x: int(x), raw_tickets.split(","))))
			raw_tickets = tickets.readline().strip()
	return criterias, ticket_collection

def remove_invalid_values(criterias, ticket_collection):
	good_values = set()
	invalid_total = 0
	# generate all valid values
	for criteria in criterias:
		for ranges in criterias[criteria]:
			start, end = ranges
			good_values.update(set([x for x in range(start, end+1)]))
	# now check all tickets
	bad_values = set()
	ticket_type = "nearby tickets:"
	for ticket_bundle in ticket_collection[ticket_type]:
		bad_ticket = tuple([ticket for ticket in ticket_bundle if ticket not in good_values])
		bad_sum = sum(bad_ticket)
		if bad_sum != 0:
			bad_values.add(ticket_bundle)
		invalid_total += bad_sum
	ticket_collection[ticket_type] = ticket_collection[ticket_type].difference(bad_values)
	return invalid_total

# first need to find which value goes where
# best way: test each column for a fit

def find_potential_orders(criterias, ticket_collection):
	# test each column now.
	potential_orders = {}
	for criteria in criterias:
		good_values = set()
		for ranges in criterias[criteria]:
			start, end = ranges
			good_values.update(set([x for x in range(start, end+1)]))
		# now test each column
		for col in range(len(criterias)):
			match = True
			for index, ticket_bundle in enumerate(ticket_collection["nearby tickets:"]):
				# print(ticket_bundle[col], criteria, criterias[criteria])
				if ticket_bundle[col] not in good_values:
					match = False
					break
			if match:
				if criteria not in potential_orders:
					potential_orders[criteria] = set()
				potential_orders[criteria].add(col)
	# order will have all pathways a departure can be in
	# the correct path will be the path which only belongs to one category.
	# we will use a priority queue to do this.
	return potential_orders

def find_exact_order(potential_orders):
	ticket_pq = PriorityQueue()
	order = {}
	seen = set()
	for category in potential_orders:
		ticket_pq.put((len(potential_orders[category]), category))
	# using a min queue, we will start by first matching the smallest potential categories
	while not ticket_pq.empty():
		cur_category_details = ticket_pq.get()
		cols_len, category = cur_category_details
		for col in potential_orders[category]:
			if col not in seen:
				seen.add(col)
				order[category] = col
				break
	return order

if __name__ == "__main__":
	criterias, ticket_collection = load_tickets("tickets.txt")
	invalids = remove_invalid_values(criterias, ticket_collection)
	potential_orders = find_potential_orders(criterias, ticket_collection)
	exact_order = find_exact_order(potential_orders)
	your_ticket_total = 1
	departure_fields = [key for key in criterias if "departure" in key[0]]
	for wanted_field in departure_fields:
		field_location = exact_order[wanted_field] # the index the field exists in
		your_ticket_total *= ticket_collection["your ticket:"][field_location]
	print("The total of all invalid values found is", invalids)
	print("Your ticket fields for depature multipled is:", your_ticket_total)