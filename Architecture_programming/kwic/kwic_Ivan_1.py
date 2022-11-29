# -*- coding: cp1251 -*-

import razdel
from string import punctuation
import pymorphy2




class KeyWordInContext:
    def __init__(self, text, window_len):
        self.text = [word.text for word in razdel.tokenize(text)]
        self.window_len = window_len
        self.data = dict()
        self.__install_normilizer__()
        self.__handle_text()
    
    def __install_normilizer__(self):
        pass

    def __get_handled_word__(self, word):
        return word
 
    def __handle_text(self):
        for index, word in enumerate(self.text):
            left = max(0, index - self.window_len)
            right = min(len(self.text) - 1, index + self.window_len)
            context = ''
            for word_index in range(left, right + 1):
                context += self.text[word_index]
                if word_index != right and self.text[word_index + 1] not in punctuation:
                    context += ' '
            word_norm_form = self.__get_handled_word__(word)
            if self.data.get(word_norm_form) == None:
                self.data[word_norm_form] = []
            self.data[word_norm_form].append(context)

    def get_contexts(self, word):
        return self.data.get(self.__get_handled_word__(word))

 
class KeyWordInContextImproved(KeyWordInContext):
    def __install_normilizer__(self):
        self.Normilizer = pymorphy2.MorphAnalyzer(lang='ru')

    def __get_handled_word__(self, word):
        return self.Normilizer.parse(word.lower())[0].normal_form

#example
'''
kwic = KeyWordInContextImproved(u'однажды я ходил гулять с собакой. Также мои друзья ходили со мной', 4)
print(kwic.get_contexts(u'ходим'))
'''


