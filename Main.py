import curses
from curses import wrapper
from Menu import menu

def main(stdscr = curses.initscr()):
    stdscr.clear()
    # cursor invisible
    curses.curs_set(0)
    menu(stdscr)

wrapper(main)