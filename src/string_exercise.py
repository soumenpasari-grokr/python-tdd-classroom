class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels_list = ['a','e','i','o','u']
        if character.lower() in vowels_list:
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sentence = sentence.split(' ')
        caught_word = {'max':0,'index':None}
        for index_point,word in enumerate(sentence):
            if len(word) > caught_word['max']:
                caught_word['max'] = len(word)
                caught_word['index'] = index_point
        return sentence[caught_word['index']]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        result_list = []
        for word in text.split(' '):
            result_list.append(len(word))
        return result_list