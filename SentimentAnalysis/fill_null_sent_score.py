from __future__ import print_function

import csv
import collections

if __name__ == '__main__':
	filename = 'bullishness_with_price_unfilled.csv'
	out = 'bullishness_with_price_filled.csv'
	with open(out, 'wb') as csvfile_out:
		fieldnames = ('date', 'opinion', 'price')
		writer = csv.DictWriter(csvfile_out, fieldnames = fieldnames)
		writer.writeheader()
		with open(filename, 'rU') as csvfile:
			reader = csv.DictReader(csvfile)
			prev = 0
			for row in reader:
				# if the sent score is not available, use previous day's sent score
				if row['opinion'] == 'N/A':
					row['opinion'] = prev
				prev = row['opinion']
				writer.writerow({
					'date' : row['date'],
					'opinion' :row['opinion'],
					'price' : row['price']
					})

