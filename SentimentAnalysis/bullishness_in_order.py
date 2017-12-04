from __future__ import print_function

import csv
import collections

if __name__ == '__main__':
	filename = 'bullishness.csv'
	out = 'bullishness_in_order.csv'
	newDict = {}
	with open(filename, 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if len(str(row['date'])) == 7:
				month = '0' + row['date'][:1]
			
			else: 
				month = row['date'][:2]

			day = row['date'][-6:-4]

			year = row['date'][-4:]

			newKey = year + month + day
			newDict[newKey] = row['bullishness']

	od = collections.OrderedDict(sorted(newDict.items()))

	with open(out, "wb") as csvfile:
		fieldnames = ('date', 'bullishness')
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for k, v in od.items():
			#print(row)
			writer.writerow({
				'date' : k,
				'bullishness' : v
				})