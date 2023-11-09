class QuestPool:
    def __init__(self):
        self.quest_pool = []
        with open("QuestPool.json", "r") as json_file:
            self.quest_pool = json.load(json_file)["quest"]

    def get_pool(self):
        return self.quest_pool

    def random_quest(self):
        return random.choice(self.get_pool())
