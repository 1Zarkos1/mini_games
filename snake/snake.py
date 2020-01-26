import curses
import random

""" width = int(input('Choose screen width (10 to 100): '))
height = int(input('Choose board height (10 to 100): '))
speed = int(input('Choose speed of the game (1 (fastest) to 20): ')) """

width = 40
height = 20
speed = 2


def play_func(stdscr):
    stdscr = curses.initscr()
    curses.resize_term(height, width)
    curses.curs_set(0)
    stdscr.keypad(True)
    next_step = 0
    pos = [[height//2, width//2]]
    rand_piece = 0
    stdscr.timeout(speed*10)
    prev_step = 0

    while next_step != 'q':

        stdscr.clear()

        while True:
            if not rand_piece:
                rand_piece = [
                    random.randint(0, height-1), random.randint(0, width-1)
                ]
                if rand_piece not in pos:
                    break
            break

        for coord in pos:
            stdscr.addstr(*coord, '*')
        stdscr.addstr(*rand_piece, '*')

        stdscr.refresh()

        try:
            next_step = stdscr.getkey()
        except Exception:
            next_step = prev_step

        if next_step not in ('KEY_UP', 'KEY_DOWN', 'KEY_RIGHT',
                     'KEY_LEFT', 'q'):
            continue
        elif next_step == 'KEY_UP':
            pos.append([pos[-1][0]-1, pos[-1][1]])
        elif next_step == 'KEY_DOWN':
            pos.append([pos[-1][0]+1, pos[-1][1]])
        elif next_step == 'KEY_RIGHT':
            pos.append([pos[-1][0], pos[-1][1]+1])
        elif next_step == 'KEY_LEFT':
            pos.append([pos[-1][0], pos[-1][1]-1])

        if pos[-1][0] >= height:
            pos[-1][0] = 0
        elif pos[-1][0] < 0:
            pos[-1][0] = height-1
        elif pos[-1][1] >= width:
            pos[-1][1] = 0
        elif pos[-1][1] < width:
            pos[-1][1] = width-1

        if pos[-1] in pos[0:-1]:
            print(f'The game is over! Your score: {len(pos[0:-1])}!')
            break

        if rand_piece == pos[-1]:
            rand_piece = 0
        else:
            pos.pop(0)

        prev_step = next_step

curses.wrapper(play_func)