#!/usr/bin/env python3

#Importing allows us to use items from these three libraries: utils, open_color, and arcade
import utils, open_color, arcade

#Checks to make sure we are using python 3.7
utils.check_version((3,7))

#The next three lines set constants so that if we want to change something later, like window size
#we can just change it here instead of everywhere it occurs in the code
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

#This line creates a new class that is given the window from arcade as a parameter
class Faces(arcade.Window):
    """ Our custom Window Class"""

    #Initializing the class, a constructor?
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        #This explanation is already given. It calls the parent constructor and gives it the size of the window
        #along with the title we want
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        #These two lines are setting the  and y to half of the length and width, giving us the center of the window.
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

        #Changes the color ofthe background to white
        arcade.set_background_color(open_color.white)

    #The on_draw method, which will re-draw the face every time the mouse moves
    def on_draw(self):
        """ Draw the face """
        #This line initializes the rendering
        arcade.start_render()
        #Sets the center of the face to the middle of the screen to start
        face_x,face_y = (self.x,self.y)
        #Changed these three lines to make the picture closer to the example
        #Each of the next 5 non-comment lines draw the face, all of the positioning relative to the center
        #of the outline
        smile_x,smile_y = (face_x + 0,face_y + 0)
        eye1_x,eye1_y = (face_x - 30,face_y + 50) 
        eye2_x,eye2_y = (face_x + 30,face_y + 50)
        #Changed shine position to be closer to example
        catch1_x,catch1_y = (face_x - 25,face_y + 63) 
        catch2_x,catch2_y = (face_x + 35,face_y + 63) 

        #Again, changed eye size to match example
        #These arcade.draw lines just color the face, specifically:
        #The whole face yellow
        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        #The outline black
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        #The two eyes black
        arcade.draw_ellipse_filled(eye1_x,eye1_y,30,50,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,30,50,open_color.black)
        #The shining of the eyes gray
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        #And the smile black
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)

    #This method updates the x and y coordinates for the center of the circle
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        #Sets the x to the current x of the mouse
        self.x = x
        #Sets the y to the current y of the mouse
        self.y = y


#Replacing the window with our new faces class
window = Faces()
#Runs the arcade
arcade.run()