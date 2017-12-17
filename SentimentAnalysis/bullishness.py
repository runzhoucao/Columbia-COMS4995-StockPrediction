from __future__ import print_function

import csv
import sys

if __name__ == '__main__':
	filename = sys.argv[1] #'raw_sentiment.csv'
	out = sys.argv[2] #'bullishness.csv'
	countDict = {}
	bullishnessDict = {}
	with open(filename, 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			date = str(row['date'])
			#print(row)
			# if row['entity-label'] == 'pos':
			if row['label']=='pos':
				#print('pos1')
				if date in countDict:
					countDict[date] += 1
					# bullishnessDict[date] += float(row['entity-confidence'])
					bullishnessDict[date] += float(row['confidence'])
				else :
					countDict[date] = 1
					bullishnessDict[date] = float(row['confidence'])
			# elif row['entity-label'] == 'neg':
			elif row['label']=='neg':
				#print('neg1')
				if date in countDict:
					countDict[date] += 1
					bullishnessDict[date] -= float(row['confidence'])
				else :
					countDict[date] = 1
					bullishnessDict[date] = float(row['confidence']) * -1.0
			# now neutral sentiment will be assigned 0 
			else:
				if date in countDict:
					countDict[date] += 1
					#no change in the score
				else:
					countDict[date] = 1
					bullishnessDict[date] = 0
 	with open(out, "wb") as csvfile:
		fieldnames = ('date', 'opinion')
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for row in bullishnessDict:
			#print(row)
			writer.writerow({
            	'date' : row,
            	'opinion' : bullishnessDict[row]/countDict[row]
            	})

