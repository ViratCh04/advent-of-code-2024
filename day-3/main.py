import re

with open('input', 'r') as file:
#with open('test', 'r') as file:
    content = file.read()

#print(content)
seq = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

matches = re.findall(seq, content)
sum = 0
for match in matches:
    x, y = map(int, match)
    result = x * y
    sum += result

print(sum)

# Part 2
# Extract non alternative matches with re.finditer(pick only one match at a time, pipe operator helps with this)
instructions = re.finditer(r'(?:do\(\)|don\'t\(\)|mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\))', content)

#enabled = False    # Caused minor headache, start positive my guys
enabled = True
sum_2 = 0

for match in instructions:
    instruction = match.group(0)
    if instruction == 'do()':
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif enabled and instruction.startswith('mul'):
        # Extract numbers from mult(x, y) in form of string tuple
        numbers = re.match(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)', instruction)
        if numbers:
            # Map string tuples to int and add to result
            x, y = map(int, numbers.groups())
            result = x * y
            sum_2 += result

print(sum_2)