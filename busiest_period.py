# Finding the busiest period in a building given a list of data entry
# and exit {timestamp,count,entry/exit}


def busiest_time(l):
	people = 0
	stmp = l[0]['timestamp']
	how_busy = {}
	for entry in range(len(l)-1):
		next_stmp = l[entry+1]['timestamp']
		if l[entry]['type']=='enter':
			people += l[entry]['count']
		else:
			people -= l[entry]['count']
		how_busy[(stmp,next_stmp)]=people
		stmp = next_stmp

	# print(how_busy)
	maxi = 0
	time_maxi = 0
	for k,v in how_busy.items():
		if v > maxi:
			maxi = v
			time_maxi = k
	return time_maxi


l = [
{"timestamp": 1526579928, "count": 3, "type": "enter"},
{"timestamp": 1526580382, "count": 2, "type": "exit"},
{"timestamp": 1526580383, "count": 3, "type": "enter"},
{"timestamp": 1526580394, "count": 4, "type": "exit"},
{"timestamp": 1526590383, "count": 1, "type": "enter"},
{"timestamp": 1526590483, "count": 1, "type": "exit"},
]
print(busiest_time(l))
