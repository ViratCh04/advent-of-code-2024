data = []
#with open('day-2/test') as f:
with open('input') as f:
    while True:
        line = f.readline()
        if not line:
            break
        items = [int(x) for x in line.split()]
        data.append(items)

print(data)
print(len(data))

safe_count_1 = 0
for i in range(len(data)):
#    inc, dec = False, False
    constraint_violation = False
    print(data[i])
    if data[i] != sorted(data[i]) and data[i] != sorted(data[i], reverse=True):
        continue
    for j in range(len(data[i]) - 1):
        diff = data[i][j + 1] - data[i][j]
        print(diff, end=" ")
        if abs(diff) >= 1 and abs(diff) <= 3:
            continue
        constraint_violation = True
        break
    print()
#    print(f"\nincreasing: {inc}, decreasing: {dec}")
#    if (inc or dec) and not constraint_violation:
    if not constraint_violation:
        safe_count_1 += 1
        
print()
print(safe_count_1)

safe_count_2 = 0
for i in range(len(data)):
    for k in range(len(data[i])):
        new_data = [x for a, x in enumerate(data[i]) if a != k]
        if new_data == sorted(new_data) or new_data == sorted(new_data, reverse=True):
            constraint_violation = False
            for j in range(len(new_data) - 1):
                diff = new_data[j + 1] - new_data[j]
                if abs(diff) >= 1 and abs(diff) <= 3:
                    continue
                constraint_violation = True
                break
            if not constraint_violation:
                safe_count_2 += 1
                break

print(safe_count_2)