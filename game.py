import arcade
import random

screen_width = 800
screen_height = 600
screen_title = "Arcade Space Shooter"
scaling = 2.0

class SpaceShooter(arcade.Window):

    # initialise the window
    def __init__(self, width:int, height:int, title:str):

        # calling parent class constructor
        super().__init__(screen_width, screen_height, screen_title) 

        # setting up enemy sprite list
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    # function to set up the bg, sounds, player
    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # set up the player
        self.player = arcade.Sprite("images/jet.png", scaling)

        # setting player position
        self.player.center_y = self.height/2
        self.player.left = 10
        self.all_sprites.append(self.player)

        # scheduling functions, spawning enemies

        arcade.schedule(self.add_enemy, 1.5) # spawns new enemy
        arcade.schedule(self.add_cloud, 3.0) # spawns new cloud

        # setting up background music

        self.bg_music = arcade.load_sound("sounds/electricSound.wav")

        # setting up sounds
        self.collision_sound = arcade.load_sound("sounds/Collision.wav")
        self.move_up_sound = arcade.load_sound("sounds/Falling_putter.wav")
        self.move_down_sound = arcade.load_sound("sounds/Rising_putter.wav")

        # starting the bg music
        arcade.play_sound(self.bg_music)

        # unpause everything
        self.paused = False
        self.collided = False
        self.collision_timer = 0.0

    # adding clouds
    def add_cloud(self, delta_time: float):
        # setting up clouds
        cloud = FlyingSprite("images/cloud.png", scaling)

        # setting up cloud position
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

        # setting up cloud velocity
        cloud.velocity = (random.randint(-5, -2), 0)

        # adding clouds to the sprite list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)


    # adding enemies
    def add_enemy(self, delta_time: float):
        # setting up missiles
        enemy = FlyingSprite("images/missile.png", scaling)

        # seeting enemy position
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # setting speed
        enemy.velocity = (random.randint(-20, -5), 0)

        # adding enemy to the sprite list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

        # removing enemy
        if enemy.right < 0:
            enemy.remove_from_sprite_lists()

        # updating enemies list
        for enemy in self.enemies_list:
            enemy.update()

    # function for keyboard input
    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.Q:
            # quit the game
            arcade.close_window()

        if symbol == arcade.key.P:
            # pause the game
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            # jump
            self.player.change_y = 250
            arcade.play_sound(self.move_up_sound)

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            # down
            self.player.change_y = -250
            arcade.play_sound(self.move_down_sound)

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            # left
            self.player.change_x = -250

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            # right
            self.player.change_x = 250


    # function for keyboard input
    def on_key_release(self, symbol: int, modifiers: int):

        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):

        # if paused, don't update anything
        if self.paused:
            return

        if self.player.collides_with_list(self.enemies_list):
            arcade.play_sound(self.collision_sound)
            arcade.close_window()

        # update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )

            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
        # self.all_sprites.update()

        # keep player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    # function to call game
    def on_draw(self):
        arcade.start_render() # clear screen and start working
        self.all_sprites.draw()

# new class based on arcade.Sprite and overides .update()
class FlyingSprite(arcade.Sprite):
    def update(self):
        # move the sprite
        super().update()

        # remove it from the screen
        if self.right < 0:
            self.remove_from_sprite_lists()

# main function
if __name__ == "__main__":
    game = SpaceShooter(
        int(screen_width * scaling), int(screen_height * scaling), screen_title
    )
    game.setup()
    arcade.run()