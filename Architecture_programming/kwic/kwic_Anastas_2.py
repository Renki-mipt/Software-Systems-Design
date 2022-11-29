def shift_line(line):
	words = line.strip().split()
	words.append(words.pop(0))
	return ' '.join(words)

def get_shifts(line):
	words_num = len(line.split())
	shifts = [line]
	shifted = line
	for i in range(words_num - 1):
		shifted = shift_line(shifted)
		shifts.append(shifted)
	return shifts

def roll_lines(lines):
	rolled_lines = []
	for line in lines:
		rolled_lines += get_shifts(line)
			
	return rolled_lines

inp_file = open("input.txt", "r")

lines = inp_file.readlines()

rolled_lines = roll_lines(lines)

sorted_lines = sorted(rolled_lines)

for line in sorted_lines:
	print(line)
