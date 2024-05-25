# Basic arcade program using objects
# Displays a white window with a blue circle in the middle

# Imports
import arcade
import arcade.key
import time
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tic-Tac-No"
SCALING = (SCREEN_WIDTH/128)

# Classes
class TicTacNo(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """
        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Set the background window
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.all_sprites = arcade.SpriteList()
        self.space_sprites = arcade.SpriteList()

    def setup(self):
        # Setup the nine spaces, each currently blank
        self.space1 = arcade.Sprite("images/blank.png", SCALING)
        self.space1.center_y = self.height/6
        self.space1.center_x = self.width/6
        self.all_sprites.append(self.space1)
        self.space_sprites.append(self.space1)

        self.space2 = arcade.Sprite("images/blank.png", SCALING)
        self.space2.center_y = self.height/6
        self.space2.center_x = 3*self.width/6
        self.all_sprites.append(self.space2)
        self.space_sprites.append(self.space2)


        self.space3 = arcade.Sprite("images/blank.png", SCALING)
        self.space3.center_y = self.height/6
        self.space3.center_x = 5*self.width/6
        self.all_sprites.append(self.space3)
        self.space_sprites.append(self.space3)


        self.space4 = arcade.Sprite("images/blank.png", SCALING)
        self.space4.center_y = 3*self.height/6
        self.space4.center_x = self.width/6
        self.all_sprites.append(self.space4)
        self.space_sprites.append(self.space4)


        self.space5 = arcade.Sprite("images/blank.png", SCALING)
        self.space5.center_y = 3*self.height/6
        self.space5.center_x = 3*self.width/6
        self.all_sprites.append(self.space5)
        self.space_sprites.append(self.space5)

        self.space6 = arcade.Sprite("images/blank.png", SCALING)
        self.space6.center_y = 3*self.height/6
        self.space6.center_x = 5*self.width/6
        self.all_sprites.append(self.space6)
        self.space_sprites.append(self.space6)


        self.space7 = arcade.Sprite("images/blank.png", SCALING)
        self.space7.center_y = 5*self.height/6
        self.space7.center_x = self.width/6
        self.all_sprites.append(self.space7)
        self.space_sprites.append(self.space7)


        self.space8 = arcade.Sprite("images/blank.png", SCALING)
        self.space8.center_y = 5*self.height/6
        self.space8.center_x = 3*self.width/6
        self.all_sprites.append(self.space8)
        self.space_sprites.append(self.space8)


        self.space9 = arcade.Sprite("images/blank.png", SCALING)
        self.space9.center_y = 5*self.height/6
        self.space9.center_x = 5*self.width/6
        self.all_sprites.append(self.space9)
        self.space_sprites.append(self.space9)

        # Board tracks what each space is, current symbol tracks the next symbol that will be placed, and current space tracks which space is currently selected
        self.board = ["N","N","N",
                      "N","N","N",
                      "N","N","N"]
        self.current_symbol = "X"
        self.current_space = 5

    def on_key_press(self, symbol: int, modifiers: int):
        # Escape closes the window
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        # Hitting a number on the number pad or the keyboard sets the current space to that spot
        if symbol == arcade.key.NUM_1 or symbol == arcade.key.KEY_1:
            self.current_space = 1
        
        if symbol == arcade.key.NUM_2 or symbol == arcade.key.KEY_2:
            self.current_space = 2
                        
        if symbol == arcade.key.NUM_3 or symbol == arcade.key.KEY_3:
            self.current_space = 3

        if symbol == arcade.key.NUM_4 or symbol == arcade.key.KEY_4:
            self.current_space = 4            

        if symbol == arcade.key.NUM_5 or symbol == arcade.key.KEY_5:
            self.current_space = 5

        if symbol == arcade.key.NUM_6 or symbol == arcade.key.KEY_6:
            self.current_space = 6

        if symbol == arcade.key.NUM_7 or symbol == arcade.key.KEY_7:
            self.current_space = 7

        if symbol == arcade.key.NUM_8  or symbol == arcade.key.KEY_8:
            self.current_space = 8

        if symbol == arcade.key.NUM_9  or symbol == arcade.key.KEY_9:
            self.current_space = 9

        # Hitting enter changes that space to that image, marks it on the board, and changes the current symbol 
        if symbol == arcade.key.ENTER:
            if self.current_symbol == "X":
                match self.current_space:
                    case 1:
                        self.space1.texture = arcade.load_texture("images/X.png")
                        self.board[0] = self.current_symbol
                        self.current_symbol = "O"
                    case 2:
                        self.space2.texture = arcade.load_texture("images/X.png")
                        self.board[1] = self.current_symbol
                        self.current_symbol = "O"
                    case 3:
                        self.space3.texture = arcade.load_texture("images/X.png")
                        self.board[2] = self.current_symbol
                        self.current_symbol = "O"
                    case 4:
                        self.space4.texture = arcade.load_texture("images/X.png")
                        self.board[3] = self.current_symbol
                        self.current_symbol = "O"
                    case 5:
                        self.space5.texture = arcade.load_texture("images/X.png")
                        self.board[4] = self.current_symbol
                        self.current_symbol = "O"
                    case 6:
                        self.space6.texture = arcade.load_texture("images/X.png")
                        self.board[5] = self.current_symbol
                        self.current_symbol = "O"
                    case 7:
                        self.space7.texture = arcade.load_texture("images/X.png")
                        self.board[6] = self.current_symbol
                        self.current_symbol = "O"
                    case 8:
                        self.space8.texture = arcade.load_texture("images/X.png")
                        self.board[7] = self.current_symbol
                        self.current_symbol = "O"
                    case 9:
                        self.space9.texture = arcade.load_texture("images/X.png")
                        self.board[8] = self.current_symbol
                        self.current_symbol = "O"
            elif self.current_symbol == "O":
                match self.current_space:
                    case 1:
                        self.space1.texture = arcade.load_texture("images/O.png")
                        self.board[0] = self.current_symbol
                        self.current_symbol = "X"
                    case 2:
                        self.space2.texture = arcade.load_texture("images/O.png")
                        self.board[1] = self.current_symbol
                        self.current_symbol = "X"
                    case 3:
                        self.space3.texture = arcade.load_texture("images/O.png")
                        self.board[2] = self.current_symbol
                        self.current_symbol = "X"
                    case 4:
                        self.space4.texture = arcade.load_texture("images/O.png")
                        self.board[3] = self.current_symbol
                        self.current_symbol = "X"
                    case 5:
                        self.space5.texture = arcade.load_texture("images/O.png")
                        self.board[4] = self.current_symbol
                        self.current_symbol = "X"
                    case 6:
                        self.space6.texture = arcade.load_texture("images/O.png")
                        self.board[5] = self.current_symbol
                        self.current_symbol = "X"
                    case 7:
                        self.space7.texture = arcade.load_texture("images/O.png")
                        self.board[6] = self.current_symbol
                        self.current_symbol = "X"
                    case 8:
                        self.space8.texture = arcade.load_texture("images/O.png")
                        self.board[7] = self.current_symbol
                        self.current_symbol = "X"
                    case 9:
                        self.space9.texture = arcade.load_texture("images/O.png")
                        self.board[8] = self.current_symbol
                        self.current_symbol = "X"



    def on_update(self, delta_time: float):
        self.all_sprites.update()
        # Check if someone has won the game. If true, close the window. 
        if (self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != "N"):
            time.sleep(1)
            arcade.close_window()
        if self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != "N":
            time.sleep(1)
            arcade.close_window()
        if self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != "N":
            time.sleep(1)
            arcade.close_window()
        # If all spaces are filled, close the window
        if "N" not in self.board:
            time.sleep(1)
            arcade.close_window()


    def on_draw(self):
        """Called whenever you need to draw your window
        """
        # Clear the screen and start drawing
        self.clear()
        arcade.start_render()
        arcade.draw_line(self.width/3, self.height, self.width/3, 0, arcade.color.BLACK, 5)
        arcade.draw_line(2*self.width/3, self.height, 2*self.width/3, 0, arcade.color.BLACK, 5)
        arcade.draw_line(self.width, self.height/3, 0, self.height/3, arcade.color.BLACK, 5)
        arcade.draw_line(self.width, 2*self.height/3, 0, 2*self.height/3, arcade.color.BLACK, 5)

        # Draw the cool stuff
        self.all_sprites.draw()

def main():
    window = TicTacNo()
    window.setup()
    arcade.run()
# Main code entry point
if __name__ == "__main__":
    main()