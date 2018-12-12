import spacy
import collections
import re
import enchant
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

nlp = spacy.load('en_core_web_md', disable=['tagger','ner', 'parser'])
nlp.add_pipe(nlp.create_pipe('sentencizer'))

for word in nlp.Defaults.stop_words:
    lex = nlp.vocab[word]
    lex.is_stop = True
d = enchant.Dict("en_US")
def remove_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def remove_url(text):
    #text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', text)
    return text

def remove_punctation(text):
    text = re.sub(r'[^\w\s]', ' ', text)
    text = str(text).replace('\t', ' ').replace('\n', '')
    return text

def remove_digits(text):
    text = re.sub("\d+", "", text)
    return text

def lower_case(text):
    text = text.lower()
    return text

def remove_empty_space(text):
    text=re.sub(' +',' ',text)
    return text
def non_ascii(text):
    text_encoded = text.encode("ascii", errors="ignore").decode()
    return text_encoded

def text_normalization(text):
    text_complete=""
    doc = nlp(str(text))
    string_text =''
    #print "DOC COMMENT --->", doc_comment
    for token in doc:
        token = token.lemma_
        doc_token = nlp(token)
        token_comm=""
        for token in doc_token:
            if (token.is_stop==False):
                if (str(token) != '-PRON-'):
                    if(d.check(str(token))==True):
                        token_comm=str(token)
                if (len(token_comm)>2):
                    string_text+=token_comm+" "
    text_complete+=string_text
    text = re.sub(' +', " ", text_complete)
    return text
