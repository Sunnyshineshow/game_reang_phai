import pygame
import json


class Sprite:
    def __init__(self, image):
        self.image = image


class SpriteManager:
    def __init__(self):
        self.spriteCollection = self.loadSprites(
            [
                "./sprite/Drink.json",
                "./sprite/Food.json",
                "./sprite/Fruit.json",
                "./sprite/Sweet.json",
                "./sprite/None.json",
                "./sprite/Heart.json",
                "./sprite/logo.json",
                "./sprite/Start_button.json",
                "./sprite/Exit_button.json",
                "./sprite/main_menu_button.json",
                "./sprite/retry_button.json",
                "./sprite/tray.json",
                "./sprite/arrows.json",
                "./sprite/gameover.json",
                "./sprite/gameover_bg.json",
                "./sprite/Quest.json",
                "./sprite/discs.json",
            ]
        )

    def loadSprites(self, urlList):
        resDict = {}  # result dictionary
        for url in urlList:
            with open(url) as jsonData:
                data = json.load(jsonData)
                mySpritesheet = SpriteSheet(data["spriteSheetURL"])
                dic = {}
                for sprite in data["sprites"]:
                    try:
                        colorkey = sprite["colorKey"]
                    except KeyError:
                        colorkey = None
                    try:
                        xSize = sprite["xsize"]
                        ySize = sprite["ysize"]
                    except KeyError:
                        xSize, ySize = data["size"]
                    dic[sprite["name"]] = Sprite(
                        mySpritesheet.image_at(
                            sprite["x"],
                            sprite["y"],
                            sprite["scalefactor"],
                            colorkey,
                            xTileSize=xSize,
                            yTileSize=ySize,
                        )
                    )
                resDict.update(dic)
                continue
        return resDict


class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
            self.sheet = pygame.image.load(filename)
            if not self.sheet.get_alpha():
                self.sheet = self.sheet.convert_alpha()
                self.sheet.set_colorkey((0, 0, 0))
        except pygame.error:
            print("Unable to load spritesheet image:", filename)
            raise SystemExit

    def image_at(self, x, y, scalingfactor, colorkey=None, xTileSize=16, yTileSize=16):
        rect = pygame.Rect((x, y, xTileSize, yTileSize))

        # Set SRCALPHA to support transparent
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return pygame.transform.scale(
            image, (xTileSize * scalingfactor, yTileSize * scalingfactor)
        )
