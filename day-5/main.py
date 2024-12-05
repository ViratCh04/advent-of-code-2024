#with open('test') as f:
with open('input') as f:
    content = f.readlines()

ordering_rules = content[:1176]
updates = content[1177:]
#ordering_rules = content[:21]
#updates = content[22:]

print(ordering_rules)
#print(len(ordering_rules))
print(updates)
#print(len(updates))

def setup_rules(rules):
    # storing rules as list of tuples
    rule_pairs = []
    for rule in rules:
        before, after = map(int, rule.strip().split('|'))
        rule_pairs.append((before, after))
    return rule_pairs

def is_valid_sequence(sequence, rules):
    # Convert update sequence to list
    nums = list(map(int, sequence.strip().split(',')))
    
    for before, after in rules:
        # Skipping rules where either number isn't in sequence cuz redundant
        if before not in nums or after not in nums:
            continue
            
        # rules apply: check if before comes before(😭) after
        if nums.index(before) > nums.index(after):
            return False
            
    return True

def solve(rules, updates):
    rule_pairs = setup_rules(rules)
    total = 0
    
    for update in updates:
        if is_valid_sequence(update, rule_pairs):
            nums = list(map(int, update.strip().split(',')))
            middle = nums[len(nums)//2]
            total += middle
            
    return total

print(solve(ordering_rules, updates))