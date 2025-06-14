import pickle
import datetime
class Saver:
    def __init__(self,player):
        self.player = player
    def save(self):
        data = datetime.datetime.now()
        with open(f"saves/save_character_{1}.pkl", "wb") as f:
            pickle.dump(self.player, f)

    def load(self,save_id):
        with open(f"saves/save_character_{1}.pkl", "rb") as f:
            self.player = pickle.load(f)


