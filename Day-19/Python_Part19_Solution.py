def load_rules(filename):
    # rules format:
    # rule num : [list of rules]. 
    # If there is the len of the list of rules > 1, we assume there's an "or" operator in between.
    with open(filename, "r") as rules_messages:
        rules_collection = {}
        for rule in rules_messages:
            rule = rule.strip()
            if not rule:
                break
            rule_num, rule_seq = rule.split(":")
            if "\"" in rule_seq:
                # place raw value
                val = rule_seq[-2] 
            else:
                cur_rules = rule_seq.strip().split("|")
                val = [cur_rule.split() for cur_rule in cur_rules]
            rules_collection[rule_num] = val
        return rules_collection, [remaining_message.strip() for remaining_message in rules_messages]

rules, messages = load_rules("sample.txt")  
