import json
import sys
import time
import re
import helper_functions as hf

filename = sys.argv[-1]
print("~> Cleaning", filename)
start_time = time.time()

def clean_file_name(filename):
	file_name=re.sub(r'\.json', "", filename)
	return file_name
#workaround to get just the id of the image 
def clean_image_id(image_id):
	file_name=clean_file_name(filename)
	remove_extension = re.sub(r'\.jpg', "", image_id)
	remove_dir = re.sub(r'/data0/pilzer/googleplus_dataset/images_jpg/', "", remove_extension)
	cleaned_image_id = re.sub(file_name+'/', "", remove_dir)
	return cleaned_image_id

def clean_caption(caption):
	#remove the punctation
	text = re.sub(r'[^\w\s]',' ',caption)
	#lemmatization + remove stop words
	cleaned_caption = hf.text_normalization(text)
	return cleaned_caption

obj={}
final_data=[]
with open(filename) as json_data:
	data = json.load(json_data)
	for d in data:
		image_id = d['image_id']
		caption = d['caption']
		cleaned_image_id = clean_image_id(image_id)
		cleaned_caption = clean_caption(caption)

		obj={"image_id":cleaned_image_id,"caption": cleaned_caption}
		final_data.append(obj)
		print(obj)

#Encode JSON data
with open('/Users/fatbardha/Desktop/text_process/caption_cleaned/'+ filename, 'w') as f:
     json.dump(final_data, f, indent=4)


end_time = time.time()
difference_time = end_time - start_time
print("~> Cleaned", filename, "in: ", difference_time)