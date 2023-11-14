from src.Utility.Dependency import *
from src.GameObjects.Quest.QuestPool import QuestPool
from src.GameObjects.Quest.Quest import Quest


### Quest Checking is available in "src > GameObjects > Board > Board.py"
class QuestBoard:
    def __init__(self):
        self.x = 1080
        self.y = 10
        self.quest_board_field = []
        self.pool = QuestPool()

        self.image = quest_image_list[0]
        self.medium_font = pygame.font.Font("./fonts/font.ttf", 12)

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

    def render(self, screen):
        counter = 0
        screen.blit(self.image, (self.x, self.y))
        for quest in self.quest_board_field:
            con = quest.condition
            strin = ""
            for c in con:
                strin += str(c.type)[9:] + " "

            t_start_color = (0, 0, 0)
            t_start = self.medium_font.render(strin, False, t_start_color)
            rect = t_start.get_rect(center=(self.x + 100, self.y + 50 + counter * 50))
            screen.blit(t_start, rect)
            counter += 1
