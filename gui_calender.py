from tkinter import *
import calendar


def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("Calendar")
    new_gui.geometry("550x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()


if __name__ == "__main__":

    gui = Tk()
    gui.config(background="white")
    gui.title("Calender")
    gui.geometry("250x140")

    cal = Label(gui, text="Calendar", bg="dark gray",
                font=("times", 28, 'bold'))

    year = Label(gui, text='enter year', bg='light green')

    year_field = Entry(gui)

    Show = Button(gui, text="Show Calendar", fg="black",
                  bg="Red", command=showCal)

    exit = Button(gui, text="Exit", fg='black', bg='red', command=exit)

    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    exit.grid(row=6, column=1)

    gui.mainloop()
