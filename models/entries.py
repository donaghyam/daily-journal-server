from pickle import NONE


class Entries():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, entry, mood_id, mood = None):
        self.id = id
        self.entry = entry
        self.mood_id = mood_id
        self.mood = mood
