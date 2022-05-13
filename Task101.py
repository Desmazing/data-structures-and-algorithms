# write program to display all student names except those starting with 'f'

names = ['Faith', 'Collins', 'Evans', 'Gilly', 'Florence', 'Jackson']
newlst = []

for name in names:
	newlst.append(name.lower())
	
for i in newlst:
	if not i.startswith('f') and not i.endswith('n'):
		print(i.capitalize())