from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io
from IndexProbability import IndexProbability


def file_getter():
    global text
    path = get_file(
        'bible.txt',
        origin='http://www.gutenberg.org/cache/epub/10/pg10.txt')
    with io.open(path, encoding='utf-8') as f:
        text = f.read().lower()
    print('corpus length:', len(text))

def fileLocationChooser(self):
    global text
    ChosenMethod = 0
    while ChosenMethod != "1" and ChosenMethod != "2":
        ChosenMethod = input("Choose whether you would like to train the model with a local file [1] or online [2]")
    if int(ChosenMethod) == 1:
        text = self.grabberFromLocal()
    elif int(ChosenMethod) == 2:
        text = self.grabberFromURL()
    return(text)


def text_sorter():
    global chars, char_indices, indices_char
    chars = sorted(list(set(text)))
    print('total chars:', len(chars))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))



def text_cleaner():
    global maxlen, sentences, next_chars, i
    # cut the text in semi-redundant sequences of maxlen characters
    maxlen = 40
    step = 3
    sentences = []
    next_chars = []
    for i in range(0, len(text) - maxlen, step):
        sentences.append(text[i: i + maxlen])
        next_chars.append(text[i + maxlen])
    print('nb sequences:', len(sentences))


def vectorisation():
    global x, y, i
    print('Vectorization...')
    x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
    y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            x[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1




def model_creator():
    global model
    # build the model: a single LSTM
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len(chars))))
    model.add(Dense(len(chars), activation='softmax'))
    optimizer = RMSprop(learning_rate=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def on_epoch_end(epoch, _):
    # Function invoked at end of each epoch. Prints generated text.
    print()
    print('----- Generating text after Epoch: %d' % epoch)

    start_index = random.randint(0, len(text) - maxlen - 1)
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print('----- diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(400):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = IndexProbability().getIndex(preds, diversity)
            next_char = indices_char[next_index]

            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()


def process():
    file_getter()
    text_sorter()
    text_cleaner()
    vectorisation()
    model_creator()

    print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

    model.fit(x, y,
        batch_size=128,
        epochs=60,
        callbacks=[print_callback])


if __name__ == "__main__":
    process()