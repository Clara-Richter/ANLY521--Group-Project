import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import requests
from bs4 import BeautifulSoup
import argparse
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


class SumText:

    """
    This class does summarization
    """

    def __init__(self, text):
        self.text = text

    def summarize(self, per=0.1):
        """
        Takes a body of text as an input and returns a summarized version of that text
        :param per: setting size of summarization
        :return: reduced size text
        """
        nlp = spacy.load('en_core_sci_sm')
        doc = nlp(self.text)
        tokens = [token.text for token in doc]
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in list(STOP_WORDS):
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word] / max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
        select_length = int(len(sentence_tokens) * per)
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ''.join(final_summary)
        return summary

    def add_definitions(self):
        """
        Takes a body of text as an input and returns definition added version of that text
        :param self: text data
        :return: reduced size text
        """
        stop_words = set(stopwords.words('english'))
        text = self.text.split()
        definitions = []
        for word in text:
            if len(word) > 1 and word not in stop_words:
                merriam_webster_parts = ['https://www.merriam-webster.com/dictionary/', word]
                merriam_webster = ''.join(merriam_webster_parts)
                try:
                    r = requests.get(merriam_webster)
                except requests.exceptions.TooManyRedirects:
                    continue
                soup = BeautifulSoup(r.content, 'html.parser')
                definition = soup.find('div', class_='vg')
                if definition is not None:
                    text = definition.get_text().strip().split('\n')[0:10]
                    text = list(filter(lambda x: len(x) > 2, text))
                    #text = '<span style="color: red;">({})</span>'.format(text)
                    #word = '<span style="color: blue;">{}</span>'.format(word)
                    text = '{} ({})'.format(word, text)
                    definitions.append(text)
                else:
                    definitions.append(word + ' ')
            else:
                definitions.append(word + ' ')
        definitions = ''.join(definitions)
        return definitions
