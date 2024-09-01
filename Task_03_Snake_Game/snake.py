# Importing only userfull libraries
from tkinter import Tk, Frame, Canvas, Label, Button, ALL
from random import randint
from os import getcwd, listdir, path
import sys

def resource_path(relative_path):
    '''Getting Relative path for exe file for icon.ico file when converted to exe'''
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)

# create 'high' to store High Score in current working directory 
if "high" not in listdir(getcwd()):
    with open("high", 'w') as f:
        pass


def getHighScore():
    '''return the High Score till yet form the saved "high" file'''
    with open('high') as f:
        val = f.readline().strip()
    if val == "":   # base case if there is no high score
        return 0
    else:
        return int(val)

def putHighScore():
    '''update "high" file with new score'''
    with open('high', 'w') as f:
        f.write(str(score))


# Global Varible for Game 
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
SPACE_SIZE = 25
BODY_PARTS = 5
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    '''Create a basic Snake body and Store its Coordinates as well as Rectanugular Body as Canvas obj.'''
    def __init__(self):
        self.bodySize = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        # predefind coordinates snake body which is left top  
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            
        # Draw rectangle/body of snake as per given Coordinates.
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")        
            self.squares.append(square)
    
    def reset(self):
        '''It delete the pre-existing snake body and init Snake Function again'''
        canvas.delete("snake")
        self.__init__()
    
    
class Food:
    '''Thid Class increase game hardness as per time, generated Random Coordinated in grid to generate food.'''
    def __init__(self):
        
        global SPEED
        if score%5 == 0: #increasing Speed by 5 after every 5 food
            SPEED -= 5
        
        # get random Cordinate on the grid for generating circular food 
        x = randint(0, (GAME_WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE
        
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tags="food")
        
    def reset(self):
        '''It delete the pre-existing food and init Food Function again'''
        canvas.delete("food")
        self.__init__()


def nextTurn(snake, food):
    '''find Head Coordinates and move toward as assign "keyword" by creating new rectangular
        Updating Score Board'''
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
    if direction == "down":
        y += SPACE_SIZE
    if direction == "left":
        x -= SPACE_SIZE
    if direction == "right":
        x += SPACE_SIZE
        
    snake.coordinates.insert(0, (x, y))
    
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")        
    snake.squares.insert(0, square)
    
    # Checking if Snake eats the food or not
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        
        ScoreBoard.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food() # Genereating new food
    
    else: #deleting tail of snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    # Testing for collisions like area of snake or its own body collison with mouth
    if checkCollisions(snake):
        gameOver()
    else:
        window.after(SPEED, nextTurn, snake, food)


def changeDirection(newDirection):
    '''change direction of snake movement by 90 degree'''
    global direction
    
    if newDirection == "left":
        if direction != "right":
            direction = newDirection
    
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection
    
    elif newDirection == "up":
        if direction != "down":
            direction = newDirection
    
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection


def checkCollisions(snake):
    '''return if collision happen with Border of Same Area of Snake body with its mouth'''
    x, y = snake.coordinates[0]
    
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    
    for bodyPart in snake.coordinates[1:]:
        if x==bodyPart[0] and y==bodyPart[1]:
            return True
    return False

def gameOver():
    '''Delete Snake and Food and Show Game Over Screen when Collision happens'''
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tags="gameover")
    resetButton.grid(row=0, column=2)   # Show the Play Again Button
    
    # Updated the score if current is greater than high score
    if score>getHighScore():
        putHighScore()
        
    # Update the Score board to display Both Scores 
    ScoreBoard.config(text=f"High Score: {getHighScore()} | Your Score: {score} | ")
    
def resetGame():
    '''Reset the Same setting to its Initial Default values'''
    global direction, score, snake, food, SPEED
    direction = "down"
    score = 0
    SPEED = 80
    ScoreBoard.config(text=f"Score: {score}")
    canvas.delete(ALL) # Delete the Canvas Objects
    snake.reset()   # Reset the Snake
    food.reset()    # Rest the food
    resetButton.grid_forget()   # Hide the Reset Button
    nextTurn(snake, food) # Giving a initial Motion with direction when game restarts


#Creting Game Windows and Congiguring it
window = Tk()
window.title("Snake Game - by AKP")
window.resizable(False, False)  # Revoke option to resize the game window
window.wm_iconbitmap(resource_path("snake.ico")) # Adding Icon on top left of title

# intial Variable inside the gameloop
score = 0
direction = "down"

# Creating a frame to Show Score, High Score and Play Button
Top = Frame(window)
Top.pack()

ScoreBoard = Label(Top, text=f"Score: {score}", font=("consolas", 20), fg='blue')
ScoreBoard.grid(row=0, column=1)

resetButton = Button(Top, text="Play Again", font=("consolas", 15), fg='green', command=resetGame, pady=0, cursor="hand2")

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# making the canvas to center 
window.update()
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int(screenWidth/2 - windowWidth/2)
y = int(screenHeight/2 - windowHeight/2)

# Updating the windows Dimension/Geometry Width and Height
window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

# Binding Arrow Keys with changeDirection to control snake movement
window.bind("<Left>", lambda event: changeDirection("left"))
window.bind("<Right>", lambda event: changeDirection("right"))
window.bind("<Up>", lambda event: changeDirection("up"))
window.bind("<Down>", lambda event: changeDirection("down"))

# Creating a snake and Food Object 
snake = Snake()
food = Food()

nextTurn(snake, food) # Giving a initial motion with direction

window.mainloop()

