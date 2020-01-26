import curses
import random


# allow user to choose window size and speed of the snake (future feature)
""" width = int(input('Choose screen width (10 to 100): '))
height = int(input('Choose board height (10 to 100): '))
speed = int(input('Choose speed of the game (1 (fastest) to 20): ')) """

# default values
width = 40
height = 20
speed = 2

# main play function
def play_func(stdscr):
    stdscr = curses.initscr()
    curses.resize_term(height, width)
    curses.curs_set(0)
    next_step = 0
    prev_step = 0
    pos = [[height//2, width//2]]
    rand_piece = 0 # position of the piece to collect
    stdscr.timeout(speed*10)

    while next_step != 'q': # if 'q' button was pressed quit the game

        # randomly select position of the piece to collect
        while True:
            if rand_piece and rand_piece not in pos:
                break
            rand_piece = [
                random.randint(0, height-1), random.randint(0, width-1)
            ]

        # clear the screen and print your snake and piece
        stdscr.clear()
        for coord in pos:
            stdscr.addstr(*coord, '*')
        stdscr.addstr(*rand_piece, '*')
        stdscr.refresh()

        # as .getkey() function throws an exception if there is no input - use
        # previous value if there is not input
        try:
            next_step = stdscr.getkey()
        except Exception:
            next_step = prev_step

        x = pos[-1][1]
        y = pos[-1][0]

        # check if pressed key within accepted accepted keys and range of values
        if next_step not in ('KEY_UP', 'KEY_DOWN', 'KEY_RIGHT',
                             'KEY_LEFT'):
            continue

        # check if next position if within the window range and change the values
        # to support transition between borders
        if next_step == 'KEY_UP':
            y = y - 1 if y > 0 else height - 1
        elif next_step == 'KEY_DOWN':
            y = y + 1 if y < height - 1 else 0
        elif next_step == 'KEY_RIGHT':
            x = x + 1 if x < width - 1 else 0
        elif next_step == 'KEY_LEFT':
            x = x - 1 if x > 0 else width - 1

        # end the game if snake crashed in itself
        if [y, x] in pos:
            print(f'The game is over! Your score: {len(pos)}!')
            break

        # if piece is collected set piece coordinates to 0 and continue
        # else remove first value from list of coordinated to make snake move
        if rand_piece == [y, x]:
            rand_piece = 0
        else:
            pos.pop(0)

        # add next step to list of coordinate to move snake forward
        pos.append([y, x])
        prev_step = next_step


curses.wrapper(play_func)
