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

        x = pos[-1][1]
        y = pos[-1][0]

        if next_step not in ('KEY_UP', 'KEY_DOWN', 'KEY_RIGHT',
                             'KEY_LEFT', 'q'):
            continue
        elif next_step == 'KEY_UP':
            y -= 1
        elif next_step == 'KEY_DOWN':
            y += 1
        elif next_step == 'KEY_RIGHT':
            x += 1
        elif next_step == 'KEY_LEFT':
            x -= 1

        if y >= height:
            y = 0
        elif y < 0:
            y = height-1
        elif x >= width:
            x = 0
        elif x < 0:
            x = width-1

        if [y, x] in pos:
            print(f'The game is over! Your score: {len(pos)}!')
            break

        if rand_piece == [y, x]:
            rand_piece = 0
        else:
            pos.pop(0)

        pos.append([y, x])

        prev_step = next_step


curses.wrapper(play_func)
