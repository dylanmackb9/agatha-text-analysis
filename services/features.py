

import os
import json





file_list_names = os.listdir(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/jsons'))  # All json file names

def getBookList(file_list_names):
  """
  Takes list of json files for word and sentence lists, and returns 
  unique list of book names + publish dates 
  """

  book_list_names = []  # unique list of book names + publish date
  for fname in file_list_names:
    if fname[-10:-5] == "words":
      if fname[:-12] not in book_list_names:
        book_list_names.append(fname[:-12])

    elif fname[-10:-5] == "ences":
      if fname[:-16] not in book_list_names:
        book_list_names.append(fname[:-16])

  return book_list_names


book_names = getBookList(file_list_names)
book_names.sort(key= lambda s : int(s[-4:]))  # Sorting based on publish date



labels = []
words = []
sentences = []
for book in book_names:

  wordlist = open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/jsons/')+book + ", words.json")
  sentencelist = open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/jsons/')+book + ", sentences.json")

  wordlist = wordlist.read()
  sentencelist = sentencelist.read()

  wordlist = json.loads(wordlist)
  sentencelist = json.loads(sentencelist)

  labels.append(book)
  words.append(wordlist)
  sentences.append(sentencelist)



