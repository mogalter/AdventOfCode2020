def load_rules():
	# creates a graph for
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
				bags_inside[index] = color[:color.index('bag')].strip()
		bag_rules[main_bag] = bags_inside
	return bag_rules

def has_color(target_color, cur_color, rules, seen):
	# by storing already computed results in, we can avoid re-calculating paths
	if cur_color in seen:
		print("We've already seen", cur_color +".", "Returning", seen[cur_color])
		return seen[cur_color]
	if target_color == cur_color:
		return True
	elif target_color != cur_color and not rules[target_color]:
		# this color has no more children to visit and isn't want we want
		return  False
	else:
		target_exists = False
		for color in rules[cur_color]:
			seen[color] = has_color(target_color, color, rules, seen)
			target_exists = target_exists or seen[color]
		return target_exists
	
def find_colors(target):
	bag_rules = load_rules()
	seen = {}
	count = 0
	for color in bag_rules:
		if has_color(target, color, bag_rules, seen) and color != target:
			count += 1
	return count

print("Bags that can contain shiny gold:", find_colors('shiny gold'), "bags")