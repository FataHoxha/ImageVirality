# Virality+

## 1) Preprocessing: comment and caption cleaning step (removing digits, punctuation, lemmatization,...)
-> In both the cleaning phase be aware to check the correct path of the file in input and output

### 1_clean_caption.py -> clean all the caption generated during through NeuralTalk.

Execution:
	
```
python3 1_clean_caption.py filename.json
```

As an output, a .json file is saved under the folder path: /caption_cleaned/

### 1_clean_comment.py -> cleans all the comment that are present in .json file crawled from Google+.\n

Execution:

```
python3 1_clean_comment.py filename.json
```

As an output, a .json file is saved under the folder path: /comment_cleaned/

## 2) Compare: for every post/image, check if there is an overlap between comments and captions

Execution:
	
```
python3 2_compare.py caption_filename.json comment_filename.json
```

As an output, a .json file is saved under the folder path: /text_compared/

## 3) CLUSTERING

