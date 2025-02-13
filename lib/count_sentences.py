import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # This will use the setter to validate the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Use regex to split the string by '.', '?', or '!' followed by a space or end of string
        sentences = re.split(r'[.!?]\s*', self.value)
        # Filter out any empty strings resulting from consecutive punctuation marks
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)