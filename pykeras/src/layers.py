# La clase layer bla bla

class Layer(object):

    def __init__(self):
        self.transform = None
        self.units = None
        self.trainable = False

    def compile(self, previous_units=0):
        self.units = previous_units if self.units is None else self.units

    def forward(self, x):
        return self.transform(x)

    def is_trainable(self):
        return self.trainable

    def summary(self):
        print("# Layer SUPERCLASS. You must overwrite the summary function.")
