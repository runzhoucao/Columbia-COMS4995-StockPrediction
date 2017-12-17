from __future__ import print_function

import csv
import collections
import sys

if __name__ == '__main__':
	market_filename = sys.argv[1] # 'stock_price.csv'
	out = sys.argv[3] #'bullishness_with_price_unfilled.csv'
	priceDict = {}
	with open(market_filename, 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			month = row['date'][0:2]

			day = row['date'][3:5]

			year = row['date'][6:8]

			priceKey = '20' + year + month + day
			priceDict[priceKey] = row['price']
			# print (priceKey)

	orderedPriceDict = collections.OrderedDict(sorted(priceDict.items()))


	sent_filename = sys.argv[2] # 'bullishness_in_order.csv'
	sentDict = {}
	with open(sent_filename, 'rU') as csvfile2:
		reader2 = csv.DictReader(csvfile2)
		for row in reader2:
			year = row['date'][0:4]
			month = row['date'][4:6]
			day = row['date'][6:8]
			sentKey = year+month+day
			sentDict[sentKey] = row['opinion']
			# print (sentKey)
	nullCounter = 0
	with open(out, "wb") as csvfile:
		fieldnames = ('date', 'opinion', 'price')
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for k, v in orderedPriceDict.items():
			#print(row)
			# there is a sent value for the day
			if k in sentDict:
				writer.writerow({
					'date' : k,
					'opinion' :sentDict[k],
					'price' : v
					})
			else:
				writer.writerow({
					'date' : k,
					'opinion' :"N/A",
					'price' : v
					})
				nullCounter +=1
	print ("There all " + str(nullCounter) + " entries that have no sentiment value")