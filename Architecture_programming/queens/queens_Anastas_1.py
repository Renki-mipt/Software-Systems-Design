from itertools import permutations


class PlacingChecker:
	def __init__(self):
		print('init...')


	def check_diags(self, placing):
		for k in range(8):
			col = 0
			for i in range(k):
				j = k - i
				if placing[i][j] == 1:
					col += 1
				if col > 1:
					return False				
		return True
	
	def zercalizev(self, placing):
		a = placing
		for i in range(8):
			for j in range(4):
				a[i][j], a[i][7-j] = a[i][7-j], a[i][j] 
		return a
	
	def zercalizeg(self, placing):
		a = placing
		for i in range(4):
			for j in range(8):
				a[7 - i][j], a[i][j] = a[i][j], a[7 - i][j] 
		return a


	
	def check(self, placing):
		if not self.check_diags(placing):
			return False
		
		#print('Plaaaaacing')
		#for plac in placing:
		#	print(*plac)
		zercv = self.zercalizev(placing)
		#print('zeeeeerc')
		#for zer in zerc:
		#	print(*zer)
		if not self.check_diags(zercv):
			return False
		zercg = self.zercalizeg(placing)
		if not self.check_diags(zercg):
			return False
		return True
		
	

class PlacingGenerator:
	all_combinations = []
	permut = []
	def __init__(self):
		print('init...')
		for i in range(8):
			cur = [0] * 8
			cur[i] = 1
			self.permut.append(cur)
		self.all_combinations = list(permutations(self.permut))

	def get_placing_gen(self):
		return self.all_combinations


class Printer:
	def __init__(self):
		print('init ...')
	def print_placing(self, placing):
		print('New placement')
		for line in placing:
			print(*line)



gen_class = PlacingGenerator()
gen = gen_class.get_placing_gen()

checker = PlacingChecker()
printer = Printer()
for placing in gen:
	if checker.check(placing):
		printer.print_placing(placing)

