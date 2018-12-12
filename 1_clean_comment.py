import json
import sys
import time
import re
import helper_functions as hf

filename = sys.argv[-1]
print("~> Cleaning", filename)

start_time = time.time()

def clean_comment(text):
	#remove the punctation
	text=hf.remove_html(text)
	text=hf.remove_url(text)
	text=hf.remove_punctation(text)
	text=hf.remove_digits(text)
	text=hf.lower_case(text)
	text=hf.non_ascii(text)
	text=hf.remove_empty_space(text)
	#lemmatization + remove stop words
	normalized_text = hf.text_normalization(text)
	normalized_text = hf.remove_empty_space(normalized_text)
	return normalized_text

with open(filename,'r') as json_data:
	data = json.load(json_data)
	for d in data:
		comments = d['comments']
		for c in comments:
			text_comment= c['text']
			text_comment=clean_comment(text_comment)
			#print (text_comment)
			c['text']=text_comment


with open('/Users/fatbardha/Desktop/text_process/comment_cleaned/'+ filename, 'w') as file:
    json.dump(data, file, indent=4)
#Encode JSON data
#with open('/Users/fatbardha/Desktop/text_process/caption_cleaned/'+ filename, 'w') as f:
#     json.dump(final_data, f, indent=4)


end_time = time.time()
difference_time = end_time - start_time
print("~> Cleaned", filename, "in: ", difference_time)
