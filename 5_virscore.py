import json
import sys
import time
import csv

filename = sys.argv[-1]
print("~> Reading score from", filename)
start_time = time.time()



with open(filename,'r') as json_data:
	with open('score_values.csv', 'a') as out_file:
		writer = csv.writer(out_file)
		#writer.writerow(('image_id', 'score','plusoners','replies','reshare'))
		data = json.load(json_data)
		image_score=float
		for d in data:
			image_id = d['id']
			image_score = d['score']
			print('image_score')
			plusoners = d['plusoners']
			print ('plusoners',plusoners)
			replies=d['replies']
			print('replies:', replies)
			reshares=d['reshare']
			print('reshare',reshares)
			#score_dict[image_id] = (image_score,plusoners,replies,reshare)
			writer.writerow([image_id, image_score,plusoners,reshares,replies])

"""with open('score_values.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(('image_id', 'score','plusoners','replies','reshare'))
    for key, values in score_dict.items():
        writer.writerow([key, values])
        """

end_time = time.time()
difference_time = end_time - start_time
print("~> Score values added in score_values.csv in: ", difference_time)
