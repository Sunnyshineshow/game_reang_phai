import json
import random
from src.GameObjects.Quest.Quest import Quest


### Quest Checking is available in "src > GameObjects > Board > Board.py"
class QuestPool:
    def __init__(self):
        self.quest_pool = []
        with open("./src/GameObjects/Quest/QuestPool.json", "r") as json_file:
            self.quest_pool = json.load(json_file)["quest"]

    def get_pool(self):
        return self.quest_pool

    def random_quest(self):
        return Quest(random.choice(self.get_pool()))
