import curses
import random

def play_func(stdscr):
    init_y = 40
    init_x = 80
    stdscr = curses.initscr()
    curses.resize_term(init_y, init_x)
    curses.curs_set(0)
    stdscr.keypad(True)
    k = 0
    pos = [[init_y//2, init_x//2]]
    rand_piece = 0

    while k != 'q':
        
        stdscr.clear()
        
        while True:
            if not rand_piece:
                rand_piece = [
                    random.randint(0, init_y-1), random.randint(0, init_x-1)
                ]
                if rand_piece not in pos:
                    break
            break
        
        for coord in pos:
            stdscr.addstr(*coord, '*')
        stdscr.addstr(*rand_piece, '*')

        stdscr.refresh()

        k = stdscr.getkey()

        if k not in ('KEY_UP', 'KEY_DOWN', 'KEY_RIGHT',
                    'KEY_LEFT', 'q'):
            continue
        elif k == 'KEY_UP':
            pos.append([pos[-1][0]-1, pos[-1][1]])
        elif k == 'KEY_DOWN':
            pos.append([pos[-1][0]+1, pos[-1][1]])
        elif k == 'KEY_RIGHT':
            pos.append([pos[-1][0], pos[-1][1]+1])
        elif k == 'KEY_LEFT':
            pos.append([pos[-1][0], pos[-1][1]-1])

        if pos[-1][0] > init_y:
            pos[-1][0] = 0
        elif pos[-1][0] < 0:
            pos[-1][0] = init_y-1
        elif pos[-1][1] > init_x:
            pos[-1][1] = 0
        elif pos[-1][1] > init_x:
            pos[-1][1] = init_x-1
        
        if pos[-1] in pos[0:-1]:
            print('You lost!')
            break

        if rand_piece == pos[-1]:
            rand_piece = 0
        else:
            pos.pop(0)

curses.wrapper(play_func)