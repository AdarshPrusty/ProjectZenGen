import numpy as np
from keras.utils.data_utils import get_file
import io

class Cleaner:
    def __init__(self):
        pass

    def grabberFromURL(self):
        origin = input("Paste/ Write the URL to the direct *text* file of which you would like to train the model with")
        path = get_file('URLfile.txt', origin)
        with io.open(path, encoding='utf-8') as f:
            text = f.read().lower()
        print('corpus length:', len(text))
        return(text)

    def grabberFromLocal(self):
        path = input("Paste/ Write the system path to the *text* file of which you would like to train the model with")
        with io.open(path, encoding='utf-8') as f:
            text = f.read().lower()
        print('corpus length:', len(text))
        return(text)

    def fileLocationChooser(self):
        ChosenMethod = 0
        while ChosenMethod != "1" and ChosenMethod != "2":
            ChosenMethod = input("Choose whether you would like to train the model with a local file [1] or online [2]")
        if int(ChosenMethod) == 1:
            text = self.grabberFromLocal()
        elif int(ChosenMethod) == 2:
            text = self.grabberFromURL()
        return(text)

    def cleanUp(self, text): 
        chars = sorted(list(set(text)))
        print('total chars:', len(chars))
        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))

        maxlen = 40
        step = 3
        sentences = []
        next_chars = []
        for i in range(0, len(text) - maxlen, step):
            sentences.append(text[i: i + maxlen])
            next_chars.append(text[i + maxlen])
        print('nb sequences:', len(sentences))
        return (sentences, maxlen, chars, char_indices, indices_char, next_chars)

    def vectorisation(self, sentences, maxlen, chars, char_indices, indices_char, next_chars):
        print('Vectorization...')
        x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
        y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                x[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1
        return(maxlen, chars, x, y)

    def mainClean(self):
        text = self.fileLocationChooser()
        sentences, maxlen, chars, char_indices, indices_char, next_chars = self.cleanUp(text)
        maxlen, chars, x, y = self.vectorisation(sentences, maxlen, chars, char_indices, indices_char, next_chars)
        return (maxlen, chars, x, y, text, chars, char_indices, indices_char, next_chars)
