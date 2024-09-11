class WordsFinder:
    file_names = []

    def __init__(self, *files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        for i in self.files:
            with open(i, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                p = [',', '.', '=', '!', '?', ';', ':', ' - ']
                string_ = ''
                for j in range(len(text)):
                    if text[j] not in p:
                        string_ += text[j]
                list_text = string_.split()
                all_words[i] = list_text
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        place_word = {}
        w = word.lower()
        for file_name, words in all_words.items():
            if w in words:
                pos = words.index(w) + 1
                place_word[file_name] = pos
            return place_word

    def count(self, word):
        all_words = self.get_all_words()
        count_word = {}
        w = word.lower()
        for file_name, words in all_words.items():
            c = words.count(w)
            count_word[file_name] = c
            return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
