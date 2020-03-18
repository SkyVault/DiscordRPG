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
        print("LOADING")
        self.db = pickle.load(open("db", "rb"))

    def save(self):
        print("SAVING")
        pickle.dump(self.db.copy(), open( "db", "wb" ))
