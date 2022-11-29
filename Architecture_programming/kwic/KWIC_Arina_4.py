#метод №4
#введены две сущности: TextReader и DictWriter
#Первая занимается чтением текста и созданием события "найдено слово", о чем уведомляется вторая сущность
#Вторая по сигналу находит по координатам, переданных по сигналу, слово и записывает фреймы с ним к себе в словарь

window_width = int(input())
text = input()
class DictWriter:
    def init(self):
        self.dictionary = {}
        self.left = 0
        self.right = text[1:].find(" ")
        while self.right < window_width:
            self.right = text[self.right+1:].find(' ')
    def add_frames(left, right):
        result = self.dictionary.get(text[left+1, right])
        if result == None:
            self.dictionary.update({text[left+1, right], [text[self.left, self.right]]})
        else:
            self.dictionary[text[left+1, right]].append(text[self.left, self.right])
        self.left = text[left+1:].find(' ')
        self.right = text[right+1:].find(' ')
    def print_contexts(word):
        idx = self.dictionary.get(word)
        if idx != None:
            for i in range(len(self.dictionary[word])):
                import pprint; pprint.pprint(self.dictionary[word][i]+'\n\r')
class TextReader:
    def init(self, e_l):
        self.text = text
        self.event_listner = e_l
    def event_creating(self):
        i = self.border_width/2
        prev_space = -1
        space_ind = self.text.find(' ')
        while space_ind < i & space_ind != -1:
            prev_space = space_ind
            space_ind = self.text[space_ind+1:].find(' ')
        while space_ind < self.text.len() - self.border_width/2 & space_ind!=-1 :
            self.event_listner.add_frames(prev_space, space_ind)
            
MyDict = DictWriter()
MyReader = TextReader(MyDict)
MyReader.event_creating()
MyDict.print_contexts("lolol")
