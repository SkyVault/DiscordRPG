import pickle
import os.path

class Data():
    def __init__(self):
        self.db = {
            users : {}
        }

        if os.path.isfile("db"):
            save(self)

    async def save(self):
        self.db = pickle.load(open("db", "rb"))

    async def load(self):
        pickle.dump(self.db, open( "db", "wb" ))
