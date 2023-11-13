from src.GameObjects.Quest.QuestPool import QuestPool
from src.GameObjects.Quest.Quest import Quest


### Quest Checking is available in "src > GameObjects > Board > Board.py"
class QuestBoard:
    def __init__(self):
        self.quest_board_field = []
        self.pool = QuestPool()

    def add_new_quest_to_board(self):
        quest = self.pool.random_quest()
        counter = 0
        while quest in self.quest_board_field:
            quest = self.pool.random_quest()
            counter += 1
            if counter == 100:
                print("No Available Quest")
                return
        self.quest_board_field.append(quest)

    def add_quest_to_board(self, raw_quest):
        print(Quest(raw_quest))
        self.quest_board_field.append(Quest(raw_quest))

    def remove_quest_from_board(self, quest):
        self.quest_board_field.remove(quest)

    def get_board(self):
        return self.quest_board_field

    def view_quest_board(self):
        _arr = []
        for i in self.quest_board_field:
            _arr.append(i.view_quest())

        return _arr
