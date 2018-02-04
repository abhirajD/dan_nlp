import sys
import re
import math
import itertools
from tabulate import tabulate

def preprocess_text(raw_string):
  #Eliminate conflicting alphanum words
  raw_string = re.sub(r'\.( [a-z])', '\g<1>', raw_string) #A period followed by a lowercase isnt a new sentence
  raw_string = re.sub(r'\'s','', raw_string) #Remove "'s" from for eg Apple's

  #Keep only Alpha
  raw_string = re.sub(r'[,\(\)\[\]"\'—]','', raw_string)
  raw_string = re.sub(r'-', ' ', raw_string)

  #Handle Start and end of sentence
  raw_string = '<s> ' + raw_string[:-1] + ' <\s>' if raw_string.endswith('.') else '<s> ' + raw_string + ' <\s>'
  raw_string = re.sub(r'\. ([A-Z])',' <\s> <s> \g<1>', raw_string)

  raw_string = raw_string.lower()
  raw_string = re.sub(r' {2,}', ' ', raw_string)
  
  return raw_string


class bigram_model():
  def __init__(self, corpus, smoothing=False):
    self.smoothing = smoothing
    #Getting UNIGRAM frequencies
    #We'll need them when calculating probabilities
    self.unigrams = raw_corpa.split(' ')
    self.unigram_set = set(self.unigrams)
    self.unigram_freq = dict()
    
    #We will have an entry for (End of sentence, Start of sentence)
    #It is noise and needs to be removed
    self.unigram_set.remove('<s>')
    self.unigram_set.remove('<\s>')
    
    #Count unigrams
    for unigram in self.unigram_set:
      self.unigram_freq[unigram] = self.unigrams.count(unigram)
    
    #Calc Vocabulary size
    self.vocab_size = len(self.unigram_freq)
    
    #MAKE BIGRAMS
    self.bigrams = list(zip(raw_corpa.split(' ')[:-1], raw_corpa.split(" ")[1:]))
    self.bigram_set = set(self.bigrams)
    self.bigram_freq = dict()
    
    #Remove(End of sentence, Start of sentence) 
    self.bigram_set.remove(('<\s>', '<s>'))
    
    #Count bigrams
    for bigram in self.bigram_set:
      self.bigram_freq[bigram] = self.bigrams.count(bigram)
  
  #Calculate Bigram Probability
  #Pass Wn-1 and Wn; (Previous word and word)
  def calculate_bigram_prob(self, prev_word, word):
    bigram_prob_numtr = self.bigram_freq.get((prev_word, word), 0)
    bigram_prob_dentr = self.unigram_freq.get(prev_word, 0)

    #Add one smoothing:
    if self.smoothing:
      bigram_prob_numtr += 1
      bigram_prob_dentr += self.vocab_size
    #Return prob
    if bigram_prob_numtr == 0 or bigram_prob_dentr == 0:
      return 0.0
    else:
      return float(bigram_prob_numtr) / float(bigram_prob_dentr)
  
  #Calculate count
  #Pass Wn-1 and Wn
  def calculate_bigram_count(self, prev_word, word):
    if self.smoothing:
      return self.bigram_freq.get((prev_word, word), 0) + 1
    else:
      return self.bigram_freq.get((prev_word, word), 0)
  
  #Calculate Complete Sentence Probability
  #Pass preprocessed sentence
  def calculate_bigram_sentence_prob(self, sentence, normalize_prob=True):
    bigram_sentence_prob_sum = 0
    bigram_pairs = list(zip(sentence.split(' ')[:-1], sentence.split(' ')[1:]))
    
    for bigram_pair in bigram_pairs:
      bigram_prob = self.calculate_bigram_prob(bigram_pair[0], bigram_pair[1])
      bigram_sentence_prob_sum += bigram_prob
    return bigram_sentence_prob_sum


#___________________________________________________________________________

if __name__ == '__main__':
  #SYS args
  path_to_corpus = str(sys.argv[1])
  s1 = str(sys.argv[2])
  s2 = str(sys.argv[3])

  #Open and preporcess corpus
  with open(path_to_corpus,'r' ,encoding='utf-8') as f:
    raw_corpa = f.read()

  raw_corpa = preprocess_text(raw_corpa)

  def print_prob_count_tables(sentence, lang_model):
    list_s1 = sentence.split(' ')
    count_list = []
    prob_list = []
    
    #Calculating count and prob for all word combinations
    for prev_word in list_s1:
      prev_word_count_list = [prev_word]
      prev_word_prob_list = [prev_word]
      
      for word in list_s1:
        prev_word_count_list.append(lang_model.calculate_bigram_count(prev_word,word))
        prev_word_prob_list.append(lang_model.calculate_bigram_prob(prev_word,word))
        
      count_list.append(prev_word_count_list)
      prob_list.append(prev_word_prob_list)

    print("===========================================================================================")
    print("::SENTENCE = ",sentence)
    print("___________________________________________________________________________")
    print(':WORD COUNT TABLE')
    print(tabulate(count_list,headers=['*']+list_s1))
    print("___________________________________________________________________________")
    print(':WORD PROBABILITY TABLE')
    print(tabulate(prob_list,headers=['*']+list_s1))
    print("___________________________________________________________________________")

    return [count_list,prob_list]
    
  #Define Language models
  lang_model = bigram_model(raw_corpa)
  lang_model_smooth = bigram_model(raw_corpa, smoothing = True)

  s1 = preprocess_text(s1)
  s2 = preprocess_text(s2)

  print('+++::SMOOTHING::FALSE+++')
  print_prob_count_tables(s1,lang_model)
  print('::PROBABILITY = ',lang_model.calculate_bigram_sentence_prob(s1), '\n')
  print_prob_count_tables(s2,lang_model)
  print('::PROBABILITY = ',lang_model.calculate_bigram_sentence_prob(s2), '\n')

  print('+++::SMOOTHING::TRUE+++')
  print_prob_count_tables(s1,lang_model_smooth)
  print('::PROBABILITY = ',lang_model_smooth.calculate_bigram_sentence_prob(s1), '\n')
  print_prob_count_tables(s2,lang_model_smooth)
  print('::PROBABILITY = ',lang_model_smooth.calculate_bigram_sentence_prob(s2), '\n')

  




