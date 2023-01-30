import re
import string

from colorama import Fore
from bs4 import BeautifulSoup

from src.constant import CONTRACTIONS_MAPPING

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# TODO on CleanText class:
# 1. Clean
# 2. Test
# 3. Less coupling
# 4. Add docstr

class CleanText:

  color = Fore.GREEN

  def __init__(self, remove_html_tags,
               make_all_lower,
               clear_contractions,
               remove_urls,
               add_space_after_full_stop,
               remove_punctuation,
               tokenize,
               remove_stop_words,
               lemmatize,
               custom_stop_words_list=['movie', 'film', 'series'],
               verbose=True):
    
    self.remove_html_tags = remove_html_tags
    self.make_all_lower = make_all_lower
    self.clear_contractions = clear_contractions
    self.remove_urls = remove_urls
    self.add_space_after_full_stop = add_space_after_full_stop
    self.remove_punctuation = remove_punctuation
    self.tokenize = tokenize
    self.remove_stop_words = remove_stop_words
    self.lemmatize = lemmatize
    self.verbose = verbose

    if self.verbose:
      self._verbose()
    if self.tokenize:
      self.tokenizer = nltk.tokenize.WhitespaceTokenizer()
    if self.remove_stop_words:
      stop_words_list = stopwords.words('english')
      self.final_stop_words_list = stop_words_list + custom_stop_words_list
    if self.lemmatize:
      self.lemmatizer = nltk.stem.WordNetLemmatizer()

  def _remove_html_tags(self, text):
    """
    Remove the html tags from the text
    Example: <div>
    """

    text = BeautifulSoup(text, 'lxml').text
    return text

  def _make_lower(self, text):
    """
    Converte all the uppercase characters into lowercase
    """

    text = text.lower()
    return text

  def _clear_contractions(self, text):
    """
    Remove contractions from the text
    Contractions are words or combinations of words that are shortened by dropping letters and replacing them by an apostrophe.
    """

    text = ' '.join(CONTRACTIONS_MAPPING[t] if t in CONTRACTIONS_MAPPING else t for t in text.split(' '))
    return text

  def _remove_urls(self, text):
    """
    Remove urls from the text
    """

    text = re.sub(r'http\S+', '', text)
    return text

  def _add_space_after_full_stop(self, text):
    """
    Add space after full stop
    Example: My name is yahea.I am 23 years old ==> My name is yahea. I am 23 years old
    """
    
    text = re.sub(r'\.(?=\S)', '. ',text)
    return text

  def _remove_punctuation(self, text):
    """
    Remove punctuation from the text
    """

    text = "".join([word for word in text if word not in string.punctuation])
    return text

  def _tokenizer(self, text):
    """
    Tokenize the text using nltk WhitespaceTokenizer
    """

    text = self.tokenizer.tokenize(text)
    return text
  
  def _remove_stop_words(self, text):
    """
    Remove stop words from the text
    """

    if isinstance(text, str):
      text = " ".join([k for k in text.split(' ') if k not in self.final_stop_words_list])
    elif isinstance(text, list):
      text = [k for k in text if k not in self.final_stop_words_list]
    return text

  def _lemmatizer(self, text):
    """
    Lemmatize the text using nltk WordNetLemmatizer
    """

    text = [self.lemmatizer.lemmatize(w) for w in text]
    return text
  
  def _verbose(self):
    print("Text preprocessing will be performed in this order")
    if self.remove_html_tags:
      print(self.color + '- HTML tags will be removed')
    if self.make_all_lower:
      print(self.color + '- All uppercase characters will be converted into lowercase')
    if self.clear_contractions:
      print(self.color + '- Contractions will be removed')
    if self.remove_urls:
      print(self.color + '- Urls will be removed')
    if self.add_space_after_full_stop:
      print(self.color + '- Spaces will be added after full stop')
    if self.remove_punctuation:
      print(self.color + '- Punctuation will be removed')
    if self.tokenize:
      print(self.color + '- Tokenizer will be implemented')
    if self.remove_stop_words:
      print(self.color + '- Stop words will be removed')
    if self.lemmatize:
      print(self.color + '- Lemmatizer will be implemented')

  def clean(self, text):
    if self.remove_html_tags:
      text = self._remove_html_tags(text)
    if self.make_all_lower:
      text = self._make_lower(text)
    if self.clear_contractions:
      text = self._clear_contractions(text)
    if self.remove_urls:
      text = self._remove_urls(text)
    if self.add_space_after_full_stop:
      text = self._add_space_after_full_stop(text)
    if self.remove_punctuation:
      text = self._remove_punctuation(text)
    if self.tokenize:
      text = self._tokenizer(text)
    if self.remove_stop_words:
      text = self._remove_stop_words(text)
    if self.lemmatize:
      text = self._lemmatizer(text)
    return text