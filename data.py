import pickle
import os.path

class Data():
    def __init__(self):
        self.db = {
            "users" : {}
        }

        if not os.path.isfile("db"):
            self.save()

    def load(self):
        self.db = pickle.load(open("db", "rb"))

    def save(self):
        pickle.dump(self.db, open( "db", "wb" ))
