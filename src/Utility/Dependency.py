import pygame
from src.Utility.Util import SpriteManager

sprite_collection = SpriteManager().spriteCollection

quest_image_list = [sprite_collection["sample_quest"].image]

food_image_list = [
    sprite_collection["food_maki"].image,
    sprite_collection["food_omurice"].image,
    sprite_collection["food_spaghetti"].image,
    sprite_collection["food_fried"].image,
    sprite_collection["food_takoyaki"].image,
    sprite_collection["food_sandwich"].image,
    sprite_collection["food_hotdog"].image,
    sprite_collection["food_bao"].image,
    sprite_collection["food_pizza"].image,
    sprite_collection["food_hamburger"].image,
    sprite_collection["food_sushi"].image,
    sprite_collection["food_ramen"].image,
]

sweet_image_list = [
    sprite_collection["sweet_tanghulu"].image,
    sprite_collection["sweet_biskit"].image,
    sprite_collection["sweet_yamroll"].image,
    sprite_collection["sweet_chocolate"].image,
    sprite_collection["sweet_pudding"].image,
    sprite_collection["sweet_shavedice"].image,
    sprite_collection["sweet_icecream"].image,
    sprite_collection["sweet_macaron"].image,
    sprite_collection["sweet_cake"].image,
    sprite_collection["sweet_mochi"].image,
    sprite_collection["sweet_taiyaki"].image,
    sprite_collection["sweet_cupcake"].image,
    sprite_collection["sweet_crape"].image,
    sprite_collection["sweet_donut"].image,
]

drink_image_list = [
    sprite_collection["drink_tea"].image,
    sprite_collection["drink_cartonmilk"].image,
    sprite_collection["drink_latte"].image,
    sprite_collection["drink_pop"].image,
    sprite_collection["drink_icedcoffee"].image,
    sprite_collection["drink_bottlemilk"].image,
    sprite_collection["drink_yakult"].image,
    sprite_collection["drink_momodrink"].image,
    sprite_collection["drink_cherry"].image,
    sprite_collection["drink_pineapplejuice"].image,
    sprite_collection["drink_coconutjuice"].image,
    sprite_collection["drink_wine"].image,
    sprite_collection["drink_beer"].image,
    sprite_collection["drink_water"].image,
    sprite_collection["drink_bottlecola"].image,
    sprite_collection["drink_cannedcola"].image,
    sprite_collection["drink_bananamilk"].image,
    sprite_collection["drink_boba"].image,
]

fruit_image_list = [
    sprite_collection["fruit_grape"].image,
    sprite_collection["fruit_cherry"].image,
    sprite_collection["fruit_orange"].image,
    sprite_collection["fruit_pineapple"].image,
    sprite_collection["fruit_lemon"].image,
    sprite_collection["fruit_watermelon"].image,
    sprite_collection["fruit_strawberry"].image,
    sprite_collection["fruit_mango"].image,
    sprite_collection["fruit_berry"].image,
    sprite_collection["fruit_carrot"].image,
    sprite_collection["fruit_mangosteen"].image,
    sprite_collection["fruit_melon"].image,
    sprite_collection["fruit_dragonfruit"].image,
    sprite_collection["fruit_avocado"].image,
    sprite_collection["fruit_banana"].image,
    sprite_collection["fruit_peach"].image,
    sprite_collection["fruit_apple"].image,
    sprite_collection["fruit_rambutan"].image,
]

none_image_list = [sprite_collection["none_none"].image]

heart_image_list = [
    sprite_collection["heart_unfilled"].image,
    sprite_collection["heart_filled"].image,
]

logo = sprite_collection["logo"].image

start_image_list = [
    sprite_collection["start_unselected"].image,
    sprite_collection["start_selected"].image,
]

exit_image_list = [
    sprite_collection["exit_unselected"].image,
    sprite_collection["exit_selected"].image,
]

retry_image_list = [
    sprite_collection["retry_unselected"].image,
    sprite_collection["retry_selected"].image,
]

main_menu_image_list = [
    sprite_collection["main_menu_unselected"].image,
    sprite_collection["main_menu_selected"].image,
]

tray_image = sprite_collection["tray"].image

arrows_image_list = [
    sprite_collection["arrow_left_unselected"].image,
    sprite_collection["arrow_left_selected"].image,
    sprite_collection["arrow_right_unselected"].image,
    sprite_collection["arrow_right_selected"].image,
]

gameover_logo = sprite_collection["gameover"].image
gameover_bg = sprite_collection["gameover_bg"].image

discs_image_list = [
    sprite_collection["disc_food"].image,
    sprite_collection["disc_sweet"].image,
    sprite_collection["disc_drink"].image,
    sprite_collection["disc_fruit"].image,
    sprite_collection["disc_none"].image,
]
