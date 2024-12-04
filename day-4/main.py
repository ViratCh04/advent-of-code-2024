with open('input') as file:
#with open('test') as file:
    content = file.read().splitlines()

rows, cols = len(content), len(content[0])
item = 'XMAS'
fw_count, bw_count, vert_count, diag_count = 0, 0, 0, 0

#print(content)
#fw_count = content.count('XMAS')
#bw_count = content[::-1].count('XMAS')
for line in content:
    for i in range(len(line) - len(item) + 1):  # decreasing redundancy 
        if item == line[i:len(item)+i]: # my dumbass was using in for comparison :) 
            fw_count += 1
        if item == line[i:len(item)+i][::-1]:
            bw_count += 1

print(fw_count, bw_count)

#verticallo
for col in range(cols):
    vert_content = ''.join(content[row][col] for row in range(rows))
    for i in range(len(vert_content) - len(item) + 1):
        if item == vert_content[i:len(item)+i]:
            vert_count += 1
        if item == vert_content[i:len(item)+i][::-1]:
            vert_count += 1

#diagonalo
# fw diag         bw diag
# X . . .         . . . X
# . M . .         . . M .
# . . A .         . A . .
# . . . S         S . . .
#for row in range(rows - len(item) + 1): #iykyk
#    for col in range(cols - len(item) + 1): #iykyk p2
for row in range(rows):
    for col in range(cols):
        if row + len(item) <= rows and col + len(item) <= cols:  #to avoid skipping diags i thought were not accessible, I narrowed down the starting points- which was bad
            diag_fw = ''.join(content[row+i][col+i] for i in range(len(item)))
            if item == diag_fw:
                diag_count += 1
            if item == diag_fw[::-1]:
                diag_count += 1

        if row + len(item) <= rows and col >= len(item) - 1:  # same :") 
            diag_bw = ''.join(content[row+i][col-i] for i in range(len(item)))
            if item == diag_bw:
                diag_count += 1
            if item == diag_bw[::-1]:
                diag_count += 1

print(vert_count, diag_count)
print(fw_count + bw_count + vert_count + diag_count)

count = 0
for row in range(1, rows - 1):#avoid edge(s)
    for col in range(1, cols - 1):  
        #check if center has A or not
        if content[row][col] == 'A':
            #check both diagonals intersecting at A
            top_left = content[row - 1][col - 1]
            bottom_right = content[row + 1][col + 1]
            top_right = content[row - 1][col + 1]
            bottom_left = content[row + 1][col - 1]

            if ((top_left + content[row][col] + bottom_right in {"MAS", "SAM"}) and
                (top_right + content[row][col] + bottom_left in {"MAS", "SAM"})):
                count += 1

print(count)