import numpy as np
import matplotlib.pyplot as plt
import string
import os
import json
import csv

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

from scipy import stats

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# DATA CLEANING FUNCTIONS

def removePunct(text, exception=''):
  """
  Removes all punctuation from text with exception
  """
  punctuation = string.punctuation
  punctuation = punctuation.replace(exception, '')

  for c in text:
    if c in punctuation:
      text = text.replace(c, '')
  return text

def createwordList(text):
  """
  Takes string texts and returns text as list of words 
  using nltk tokenize function
  """

  return word_tokenize(removePunct(text))

def createsentenceList(text):
  """
  Takes string texts and returns text as list of sentences 
  using nltk tokenize function, keeping . to do so
  """

  return sent_tokenize(removePunct(text, '.'))
  
  
# CREATING JSONS


books = os.listdir(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/books')) # PUT TEXT FILES IN BOOKS FOLDER


#print(books)

for fname in books:
  
  text = open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/books/') + fname)
  text = text.read()

  words = createwordList(text)
  sentences = createsentenceList(text)
  
  with open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/')+fname[0:-4]+', words.json', 'w') as fp:
    json.dump(words, fp, sort_keys=True, indent=4)
  with open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/')+fname[0:-4]+', sentences.json', 'w') as fp:
    json.dump(sentences, fp, sort_keys=True, indent=4)


    

  