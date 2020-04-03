from __future__ import print_function
from keras.callbacks import LambdaCallback
from cleaner import Cleaner
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.models import Sequential
import random
import numpy as np
import sys

class ModelTrainer:
    def __init__(self):
        pass

    def sample(self, preds, temperature=1.0):
        # helper function to sample an index from a probability array
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)


    def on_epoch_end(self, model, epoch, text, maxlen, chars, char_indices, indices_char):
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
                next_index = self.sample(preds, diversity)
                next_char = indices_char[next_index]

                sentence = sentence[1:] + next_char

                sys.stdout.write(next_char)
                sys.stdout.flush()
            print()

    def process(self):
        maxlen, chars, x, y, text, chars, char_indices, indices_char, next_chars = Cleaner().mainClean()
        model = self.createModel(maxlen, chars)
        print_callback = LambdaCallback(on_epoch_end=self.on_epoch_end(model, self.on_epoch_end(), text, maxlen, chars, char_indices, indices_char))
        ModelTrainer().main(print_callback, model, x, y)

    def main(self, print_callback, model, x, y):
        model.fit(x, y,
            batch_size=128,
            epochs=60,
            callbacks=[print_callback])

    def createModel(self, maxlen, chars):
        print('Build model...')
        model = Sequential()
        model.add(LSTM(128, input_shape=(maxlen, len(chars))))
        model.add(Dense(len(chars), activation='softmax'))

        optimizer = RMSprop(learning_rate=0.01)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer)
        return model