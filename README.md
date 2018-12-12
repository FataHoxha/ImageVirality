# Virality+

## 1) CLEAN: comment and caption cleaning step (removing digits, punctuation, lemmatization,...)

	-> In both the cleaning phase be aware to check the correct path of the file in input and output

	# 1_clean_caption.py -> clean all the caption generated during through NeuralTalk.

	Execution:
	```
	python3 1_clean_caption.py filename.json
	```

	As an output, a .json file is saved under the folder /caption_cleaned/

	# 1_clean_comment.py -> cleans all the comment that are present in .json file crawled from Google+.\n

	execution:
	```
	python3 1_clean_comment.py filename.json
	```
	As an output, a .json file is saved under the folder /comment_cleaned/

## 2) COMPARE: 

## 3) CLUSTERING

