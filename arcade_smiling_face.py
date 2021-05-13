
# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Arcade Game"
RADIUS = 150

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.CADET_GREY)

arcade.start_render() #This render the background to show

#circle face
arcade.draw_circle_filled(300, 300, 200, arcade.color.YELLOW)

#eye
arcade.draw_circle_filled(370, 350, 20, arcade.color.BLACK)

#eye2
arcade.draw_circle_filled(230, 350, 20, arcade.color.BLACK)

#mouth
#This draw he mouth
x = 300
y = 280
width = 200
height = 180
start_angle = 190
end_angle = 350
mouth_color = arcade.color.BLACK
size = 10
arcade.draw_arc_outline(x, y, width, height, mouth_color, start_angle, end_angle, size)


arcade.finish_render()


arcade.run()
