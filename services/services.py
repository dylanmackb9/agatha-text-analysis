
import numpy as np
import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag



########## SERVICES ###########
# Functions used to provide insight on books




# CREATING YEARS

def createYears(labels):
  """
  Returns list of ordered years of books published.
  """

  years = []
  for book in labels:
    years.append(book[-4:])
  return years





# CONCORDANCE

def createConcordance(labels, words):
  """
  Creates a concordance of each book, which is a dictionary that contains
  each word used and its frequency. Concordance is a list of dictionaries for
  each book, in publishing order. Concordance is sorted, not capitalization is
  not changed.
  """

  concordance = [] # list of dictionaries,  
  for i, wordlist in enumerate(words):
    
    conc_dict = {}
    for w in wordlist:
      if w.isalpha():
        if w in conc_dict:
          conc_dict[w] += 1
        elif w not in conc_dict:
          conc_dict[w] = 1
    
    ranked_conc_dict = sorted(conc_dict, key=conc_dict.get , reverse=True)
    
    final = {}
    for w in ranked_conc_dict:
      final[w] = conc_dict[w]
    concordance.append(final)
  return concordance





def concordanceNoStops(concordance, stopwords):
  """
  Creates the same concordance list but with stopwords removed
  """

  nostop_concordance = []
  for conc in concordance:
    nostop_dict = {}

    for word in conc:
      if word not in stopwords:
        nostop_dict[word] = conc[word]

    nostop_concordance.append(nostop_dict)
    
  return nostop_concordance





def concordanceNNP(nostop_concordance, stopwords):
  """
  Creates same concordance list but only with words tagged as proper nouns
  """

  nnp_concordance = []
  for i, conc in enumerate(nostop_concordance):
    nnp_dict = {}
    tagged_text = pos_tag(list(nostop_concordance[i]))
    nnps = [word for word,pos in tagged_text if pos == 'NNP']
    
    for word in conc:
      if word in nnps:
        nnp_dict[word] = conc[word]
        

    nnp_concordance.append(nnp_dict)

  return nnp_concordance


  



# FREQUENCY FINDER

def frequencyFinder(word, concordance):
  """
  Returns how many times a given word is used in each book.
  """

  frequency = []
  for book in concordance:
    try:
      frequency.append(book[word])
    except:
      frequency.append(0)
  return frequency





# UNIQUE WORDS 

def uniqueWords(number_of_books, labels, concordance, words):
  """
  Returns tuple of number of words in each book that 
  are unique and the total number of words
  """

  unique_words = np.zeros((number_of_books, ))
  total_words = np.zeros((number_of_books, ))
  for i in range(number_of_books):
    unique_words[i] = len(concordance[i])
    total_words[i] = len(words[i])

  return unique_words, total_words

  



# AVERAGE LENGTH OF SENTENCE

def sentenceLength(number_of_books, sentences):
  """
  Returns the average length of a sentence by character for each book
  """

  average_sentence_length_c = np.zeros((number_of_books, ))
  average_sentence_length_w = np.zeros((number_of_books, ))
  for i in range(number_of_books):
    
    sentence_length_total_c = 0
    sentence_length_total_w = 0
    for sentence in sentences[i]:
      sentence_length_total_c += len(sentence)
      sentence_length_total_w += len(sentence.split(" "))
    
    average_sentence_length_c[i] = sentence_length_total_c / len(sentences[i])
    average_sentence_length_w[i] = sentence_length_total_w / len(sentences[i])

  return average_sentence_length_c, average_sentence_length_w




def totalNumStop(number_of_books, stopwords, words):
  """
  Returns total number of stop words in book
  """

  total_stops = np.zeros((number_of_books, ))
  for i, book in enumerate(words):

    total = 0
    for w in book:
      if w.lower() in stopwords:
        total += 1
    total_stops[i] = total
  
  return total_stops


def totalNNP(number_of_books, nnp_concordance, words):
  
  total_nnp = np.zeros((number_of_books, ))
  for i, book in enumerate(words):

    tagged_text = pos_tag(list(words[i]))
    nnps = [word for word,pos in tagged_text if pos == 'NNP']
    total_nnp[i] = len(nnps)
  
  return total_nnp


def totalUniqueStop(number_of_books, stopwords, concordance):
  """
  Returns total number of unique stopwords used
  """

  total_unique_stops = np.zeros((number_of_books, ))
  for i, conc in enumerate(concordance):
    total = 0
    for w in conc:
      if w.lower() in stopwords:
        total += 1
    total_unique_stops[i] = (total)
  
  return total_unique_stops


def totalUniqueNNP(number_of_books, nnp_concordance):
  """
  Returns total number of unique NNPs used
  """

  total_unique_nnps = np.zeros((number_of_books, ))
  for i, conc in enumerate(nnp_concordance):
    total_unique_nnps[i] = len(conc)
  
  return total_unique_nnps


def numPronoun(number_of_books, pronouns, concordance):
  """
  Counts the frequency of pronouns
  """

  
  numpronouns = np.zeros((number_of_books, ))
  for w in pronouns:
    numpronouns += frequencyFinder(w, concordance)
   
  return numpronouns


def avgposPerSentence(number_of_books, concordance, pos, sentences, tagdicts):
  """
  Counts the number of specified POS in a sentence
  """

  assert type(pos) == list

  avgpos_per_sentence = np.zeros((number_of_books, ))
  for i, book in enumerate(sentences):
    pos_in_sentence = np.zeros((len(book), ))  # Number of sentences in book
    print(i)
    for j, sen in enumerate(book):
      total_num_pos = 0  # per sentence
      tok_sen = word_tokenize(sen)
      
      counter = 0
      #print(tok_sen)
      for w in tok_sen:

        if w.isalpha():
          counter += 1
          if tagdicts[i][w] in pos:  # pos are alway uppercase, forcing the param here
            total_num_pos += 1
      if counter > 0:
        pos_in_sentence[j] = total_num_pos / counter
    avgpos_per_sentence[i] = np.average(pos_in_sentence)
  
  return avgpos_per_sentence





def postagDict(concordance):
  """
  Creates a list of dictionaries, one for each book, with words as keys
  and their tags as values
  """

  tagdicts = []
  for i, book in enumerate(concordance):
    mydict = {}
    tagged = nltk.pos_tag(book.keys())
    for w in tagged:
      mydict[w[0]] = w[-1]
    tagdicts.append(mydict)
  return tagdicts

