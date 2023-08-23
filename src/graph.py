import os
import numpy as np

def plot_channel_function(subscribers_array):
    RED = 31
    GREEN = 32
    WHITE = 37
    def writeAt (y, x, input):
        print("\033[%d;%dH" % (y, x) + input)

    def draw(color):
        print("\033[%dm" % (color))

    os.system("clear")

    #subscribers_array = [100, 50, 200, 500, -400, -1000, 200, 500, -400, 300]
    GRAPH_HEIGHT = 21
    GRAPH_WIDTH = 100
    MIDDLE = GRAPH_HEIGHT/2
    MEAN = np.mean(subscribers_array)
    MAX = np.max(np.absolute(subscribers_array))
    MIN = 0 #np.min(EXAMPLE_NUMBERS)
    TOTAL_SCALE_SUM = np.max(np.absolute(MAX), 0)
    INCREMENT = TOTAL_SCALE_SUM / GRAPH_HEIGHT

    # ●
    ### []  PLOT THE DATA
    ### [X] MAKE THE LINE/DOT GRAPH LOOK GOOD
    ### []  PUT THE VALUE ON TOP OF POINT
    ### []  PLOT PERCENTAGE OF CHANGE OF SUBSCRIBERS

    ### DRAW GRAPH
    for i in range(GRAPH_WIDTH):
        if i == 1:
            writeAt(GRAPH_HEIGHT+1, i, "╋")
        else:
            writeAt(GRAPH_HEIGHT+1, i, "━")
            writeAt(MIDDLE+1, i, "─")


    for i in range(GRAPH_HEIGHT+1):
        if i == GRAPH_HEIGHT+1 or i == MIDDLE+1:
            writeAt(i, 0, "╋")
        else:
            writeAt(i, 0, "┃")


    ### DRAW POINTS

    for index, item in enumerate(subscribers_array):
        y_position = round((GRAPH_HEIGHT - (item / INCREMENT))/2)
        x_position = (GRAPH_WIDTH/len(subscribers_array)) * (index + 1)

        if y_position > MIDDLE + (MIDDLE/2/2):
            draw(RED)
        elif y_position < MIDDLE - (MIDDLE/2/2):
            draw(GREEN)
        else:
            draw(WHITE)
        writeAt(y_position, x_position, str(f'● {item}'))

        # while y_position < MIDDLE-1:
        #     y_position = y_position + 1
        #     writeAt(y_position, x_position, '●')

        # while y_position > MIDDLE+1:
        #     y_position = y_position - 1
        #     writeAt(y_position, x_position, '●')

    #writeAt(30, 1, str(INCREMENT))
    #writeAt(31, 1, str(TOTAL_SCALE_SUM))


    ### STOPS THE PROGRAM (REMOVE LATER)
    input()
