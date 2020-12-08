def load_rules():
	# creates a graph for calculating!
	bag_rules = {}
	rules_input = open("rules.txt", "r")
	for rule in rules_input:
		rule = rule.strip()
		main_bag, holds = rule.split(" bags contain ")
		bags_inside = holds.split(",")
		if 'no other bags.' in bags_inside:
			bags_inside = []
		else:
			for index, bag in enumerate(bags_inside):
				# clean out the numbers and get colors
				num, color = bag.strip().split(" ", 1)
				bags_inside[index] = ( color[:color.index('bag')].strip(), int(num))
		bag_rules[main_bag] = bags_inside
	rules_input.close()
	return bag_rules

def count_bags(cur_color, rules, seen):
	color_only, color_count = cur_color
	if not rules[color_only]:
		# if there's no children, simply return the bag count
		return color_count
	else:
		seen[color_only] = 0
		for color in rules[color_only]:
			computed = (color_count * count_bags(color, rules, seen))
			print("Computed" ,color[0], "in", color_only, "-", computed, "bags.")
			seen[color_only] += computed
			print(color_only, "currently has", seen[color_only], "bags in it.")
		# factor in the original bag(s)
		seen[color_only] += color_count
		return seen[color_only]

def find_bags_in_target(target):
	bag_rules = load_rules()
	seen = {}
	count = 0
	print("Search:", bag_rules[target])
	for color in bag_rules[target]:
		print(target, "bag has", color[1], color[0], "bags in it.")
		count += count_bags(color, bag_rules, seen)
	return count

print("There are", find_bags_in_target('shiny gold'), "bags in your shiny gold bag!")