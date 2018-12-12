import json
import sys
import re
import time
import spacy

from spacy.lang.en import English

nlp = spacy.load('en_core_web_md', disable=['tagger','ner', 'parser'])
nlp.add_pipe(nlp.create_pipe('sentencizer'))

cap_filename = sys.argv[-1]
cap_path="/Users/fatbardha/Desktop/text_process/caption_cleaned/"
comm_filename= sys.argv[-2]
comm_path="/Users/fatbardha/Desktop/text_process/comment_cleaned/"
#print("~> Comparing", cap_filename,comm_filename)
start_time = time.time()

def clean_file_name(filename,dir_path):
	#remove_extension=re.sub(r'\.json', "", filename)
	remove_dir = re.sub((r""+dir_path),"", filename)
	return remove_dir

#cap_file=clean_file_name(cap_filename, cap_path)
cap_file=re.sub(r'/Users/fatbardha/Desktop/test_cap', "" , cap_filename)
comm_file=re.sub(r'/Users/fatbardha/Desktop/test_comm',"",comm_filename)
filename= comm_file
print("~> Comparing", cap_file,comm_file)
obj={}
final_data=[]
"""
with open(filename) as json_data:
	data = json.load(json_data)
	for d in data:
		image_id = d['image_id']
		caption = d['caption']
"""
with open(cap_filename) as json_cap:
	cap_data = json.load(json_cap)
	
	with open(comm_filename) as json_comm:
		comm_data = json.load(json_comm)
		
		for cap in cap_data:
			cap_id=cap['image_id']
			caption=cap['caption']
			
			for comm in comm_data:
				comm_id =comm['id']
				comments = comm['comments']
				final_id=None
				final_comment=""
				if (cap_id == comm_id):
					#print("~> Check match for the same id:", cap_id)
					for comm_text in comments:
						comment = comm_text['text']
						final_comment+=comment 
						comment_id = comm_text['id']
						doc_caption = nlp(caption)
						doc_comment = nlp(comment)

						#print("~> Tokenizing caption & comment")
						for token_caption in doc_caption:
							for token_comment in doc_comment:
								#convert from unicode to string 
								token_comment=str(token_comment)
								token_caption=str(token_caption)
								
								#find the same string and count the occurence of that string 
								#in all the comment related with that id
								#print("~> Check match for token_caption & token_comment")
								if token_caption==token_comment:
									#save that id, and save all the comment contained in it
									final_id = comm_id
									#print (comment_id)
				if (final_id!=None):
					obj={"id":final_id,
					"plusoners": comm['plusoners'] ,
					"reshare": comm['reshares'],
					"replies" : comm['replies'],
					"score":comm["score"],
					"caption":caption,
					"comments":final_comment}
					final_data.append(obj)
					print("~> Adding info for id", final_id)

#Encode JSON data
with open('/Users/fatbardha/Desktop/text_process/text_compared/'+ filename, 'w') as f:
	json.dump(final_data, f, indent=4)


end_time = time.time()
difference_time = end_time - start_time
print("~> Compared", cap_file,"and",comm_file, "in: ", difference_time)


