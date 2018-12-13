import json
import sys
import time
import csv

filename = sys.argv[-1]
print("~> Adding word from", filename)
start_time = time.time()

dict_list=[]
with open(filename,'r') as json_data:
	data = json.load(json_data)
	for d in data:
		keywords = d['keyword']
		#print (keywords)
		for k in keywords:
			dict_list.append(k)
			print (k)
print("final dict_list")
print(dict_list)


with open('word_list.csv', 'a', newline='') as csv_out:
	writer = csv.writer(csv_out)
	for item in dict_list:
		writer.writerow([item])

end_time = time.time()
difference_time = end_time - start_time
print("~> Cleaned", filename, "in: ", difference_time)
