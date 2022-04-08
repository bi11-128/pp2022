import curses 
from curses import wrapper
def main(stdscr):
  stdscr.addstr("Input a student name")
  key=stdscr.getstr(0,0,4)
  GPAm=GPAcount(key)
  stdscr.addstr(f"key's GPA:{GPAm}")
  stdscr.refresh()
  stdscr.getch()

wrapper(main)


