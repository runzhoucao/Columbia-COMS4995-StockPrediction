from __future__ import print_function

import csv

if __name__ == '__main__':
	filename = 'result1-end.csv'
	out = 'bullishness.csv'
	countDict = {}
	bullishnessDict = {}
	with open(filename, 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			date = str(row['date'])
			#print(row)
			if row['entity-label'] == 'pos':
				#print('pos1')
				if date in countDict:
					countDict[date] += 1
					bullishnessDict[date] += float(row['entity-confidence'])
				else :
					countDict[date] = 1
					bullishnessDict[date] = float(row['entity-confidence'])
			elif row['entity-label'] == 'neg':
				#print('neg1')
				if date in countDict:
					countDict[date] += 1
					bullishnessDict[date] -= float(row['entity-confidence'])
				else :
					countDict[date] = 1
					bullishnessDict[date] = float(row['entity-confidence']) * -1.0
			# now neutral sentiment will be assigned 0 
			else:
				if date in countDict:
					countDict[date] += 1
					#no change in the score
				else:
					countDict[date] = 1
					bullishnessDict[date] = 0
 	with open(out, "wb") as csvfile:
		fieldnames = ('date', 'bullishness')
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for row in bullishnessDict:
			#print(row)
			writer.writerow({
            	'date' : row,
            	'bullishness' : bullishnessDict[row]/countDict[row]
            	})

