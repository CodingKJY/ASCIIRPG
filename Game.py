import curses

def newGame(stdscr = curses.initscr()):
    stdscr.clear()
    # color setting
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN   = curses.color_pair(1)

    stdscr.addstr(1, 1, 'In new Game...', GREEN)
    stdscr.refresh()
    stdscr.getch()

def loadGame(stdscr = curses.initscr()):
    stdscr.clear()
    # color setting
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN   = curses.color_pair(1)

    stdscr.addstr(1, 1, 'In load Game...', GREEN)
    stdscr.refresh()
    stdscr.getch()