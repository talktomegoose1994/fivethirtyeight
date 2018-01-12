'''
Creating a process to solve the probability of dwarves sleeping in beds from 
the riddler FIVETHIRTYEIGHT question of the week 1.9.18
'''



beds = ['B','C','D','E','F','G']

start = [['A', 'B', 'C', 'D', 'E', 'F'],
 ['A', 'B', 'C', 'D', 'E', 'G'],
 ['A', 'B', 'C', 'D', 'F', 'G'],
 ['A', 'B', 'C', 'E', 'F', 'G'],
 ['A', 'B', 'D', 'E', 'F', 'G'],
 ['A', 'C', 'D', 'E', 'F', 'G']]

dwarves = ['B','C','D','E','F','G']
global found
found = 0
global bedless
bedless = 0
global overall_found
overall_found = 0
global overall_bedless
overall_bedless = 0

def recursive_bed(dwarf_list, bed_list):
	print "Hit recursion with Dwarves:{} and Beds:{}".format(dwarf_list,bed_list)
	if len(dwarf_list) == 1:
		if dwarf_list[0] in bed_list:
			print "End of Branch - Bed Found"
			global found
			global overall_found
			found += 1
			overall_found += 1
		else:
			print "End of Branch - No Bed"
			global bedless
			global overall_bedless
			bedless += 1
			overall_bedless += 1
		return
	else:
		if dwarf_list[0] in bed_list:
			index = bed_list.index(dwarf_list[0])
			new_dwarf_list = dwarf_list[1:]
			new_bed_list = bed_list[:index]+ bed_list[index+1:]
			global overall_found
			overall_found += 1
			recursive_bed(new_dwarf_list, new_bed_list)
		else:
			global overall_bedless
			overall_bedless += 1
			master_bed_list = bed_list
			for i in range(0,len(master_bed_list)):
				new_bed_list = master_bed_list[:i]+master_bed_list[i+1:]
				new_dwarf_list = dwarf_list[1:]
				recursive_bed(new_dwarf_list, new_bed_list)
		return

if __name__ == "__main__":
	for i in start:
		print "top-level"
		recursive_bed(dwarves, i)
		print found, bedless
	print "{} dwarves found bed out of {} possibilities".format(found, found+bedless)
	print "{} dwarves slept in their own beds, {} dwarves slept in other beds out of {} total".format(overall_found, overall_bedless, overall_found+overall_bedless)




