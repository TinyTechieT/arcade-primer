# imports
import arcade

#constants
screen_width = 600
screen_height = 800
screen_title = "welcome to arcade"
radius = 150

arcade.open_window(screen_width, screen_height, screen_title)

arcade.set_background_color(arcade.color.RED)

arcade.start_render()

arcade.draw_circle_filled(screen_width/2, screen_height/2, radius, arcade.color.ALICE_BLUE)

arcade.finish_render()

arcade.run()