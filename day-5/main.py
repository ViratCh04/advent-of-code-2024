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

def is_valid_sequence(update, rules):
    # Convert update sequence to list
    nums = list(map(int, update.strip().split(',')))
    
    for before, after in rules:
        # Skipping rules where either number isn't in sequence cuz redundant
        if before not in nums or after not in nums:
            continue
            
        # rules apply: check if before comes before(😭) after
        if nums.index(before) > nums.index(after):
            return False
            
    return True

def solve_p1(rules, updates):
    rule_pairs = setup_rules(rules)
    total = 0
    
    for update in updates:
        if is_valid_sequence(update, rule_pairs):
            nums = list(map(int, update.strip().split(',')))
            middle = nums[len(nums)//2]
            total += middle
            
    return total

print(solve_p1(ordering_rules, updates))


# Part 2
def reorder_sequence(update, rule_pairs):
    nums = list(map(int, update.strip().split(',')))
    n = len(nums)
    
    # Fumble sort because I'm a fumbling idiot
    for i in range(n):
        # swap pairs if they should be swapped according to rules
        for j in range(0, n-i-1):
            a, b = nums[j], nums[j+1]
            # checking if this pair exists in any rule
            for before, after in rule_pairs:
                if (a,b) == (after, before):
                    # found da rule saying a should placed after b 
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    break
    
    return nums

def solve_p2(rules, updates):
    rule_pairs = setup_rules(rules)
    total = 0
    
    for update in updates:
        if not is_valid_sequence(update, rule_pairs):
            # Only process incorrect sequences
            nums = reorder_sequence(update, rule_pairs)
            middle = nums[len(nums)//2]
            total += middle
            
    return total

print(solve_p2(ordering_rules, updates))
