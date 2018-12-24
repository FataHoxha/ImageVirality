import json
import sys
import time
import csv
import re

filename = sys.argv[-1]
print("~> Adding word from", filename)
start_time = time.time()

dict_list=[]
with open(filename,'r') as csv_in:
	for d in csv_in:
		text=str(d)
		text=re.sub(r'\n', "" , text)
		if text not in dict_list:
			dict_list.append(text)
			print (text)
print("final dict_list")
print(dict_list)


with open('final_word_list.csv', 'a', newline='') as csv_out:
	writer = csv.writer(csv_out)
	for item in dict_list:
		writer.writerow([item])

end_time = time.time()
difference_time = end_time - start_time
print("~> Cleaned", filename, "in: ", difference_time)