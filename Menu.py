import curses
from Game import newGame, loadGame

def menu(stdscr = curses.initscr()):
    # color setting
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN   = curses.color_pair(1)

    # get screen height width
    maxHeight, maxWidth = stdscr.getmaxyx()

    # menu display texts
    displayText = [
        ' New  Game ',
        ' Load Game ',
        ' Quit Game '
    ]
    number_of_text = len(displayText)

    # menu window attributes
    boxWidth  = max([len(text) for text in displayText]) + 2
    boxHeight = 2 * number_of_text + 1
    b_y = maxHeight//2 - boxHeight//2
    b_x = maxWidth//2 - boxWidth//2 - 1
    menuWin = curses.newwin(boxHeight, boxWidth, b_y, b_x)
    
    # menuWin.border()

    # title window attributes
    t_uborder = '==========================\n'
    title     = ' A S C I I  R P G  v0.0.0 \n'
    t_dborder = '=========================='
    titleWidth  = len(title) + 3
    titleHeight = 3 
    t_y = b_y - titleHeight
    t_x = maxWidth//2 - titleWidth//2 + 1
    titleWin = curses.newwin(titleHeight, titleWidth, t_y, t_x)

    # Selection
    select = 0

    while True:
        menuWin.clear()
        # Screen border
        stdscr.clear()
        stdscr.attron(GREEN)
        stdscr.border()
        stdscr.attroff(GREEN)
        stdscr.refresh()

        # Title
        titleWin.clear()
        titleWin.addstr(t_uborder, GREEN | curses.A_BOLD)
        titleWin.addstr(title    , GREEN | curses.A_BOLD)
        titleWin.addstr(t_dborder, GREEN | curses.A_BOLD)
        titleWin.refresh()

        # update menu screen
        for i in range(0, number_of_text):
            if select == i:
                menuWin.addstr(1 + 2 * i, 0, '[', GREEN)
                menuWin.addstr(1 + 2 * i, 1, displayText[i], GREEN | curses.A_REVERSE)
                menuWin.addstr(1 + 2 * i, boxWidth - 1, ']', GREEN)
            else:
                menuWin.addstr(1 + 2 * i, 1, displayText[i], GREEN)
        menuWin.refresh()

        # get key
        key = stdscr.getch()
        if   key == ord('w'):
            select = (select - 1) % number_of_text
        elif key == ord('s'):
            select = (select + 1) % number_of_text
        elif key == 10:
            if select == -1 % number_of_text: # quit game
                break
            if select == 0: # new game
                newGame(stdscr)
            if select == 1: # load game
                loadGame(stdscr)
