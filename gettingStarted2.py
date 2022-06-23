import arcade

screen_width = 600
screen_height = 800
screen_title = "welcome to arcade"
radius = 150

# Classes
class welcome(arcade.Window):
    def __init__(self): # initialise the window

        super().__init__(screen_width, screen_height, screen_title) # calling parent class constructor

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render() # clear screen and start working

        arcade.draw_circle_filled(screen_width/2, screen_height/2, radius, arcade.color.AERO_BLUE)

# main function
if __name__ == "__main__":
    app = welcome()
    arcade.run()