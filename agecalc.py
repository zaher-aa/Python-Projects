from tkinter import *
from tkinter import messagebox

# create the main aoo window and its related things
root = Tk()  # main app window
root.title("Age Calculate By Zaher.")  # change app title
root.geometry("400x200")  # set the window dimentions

# clarification lable
# tell the user to make something
lable = Label(root, text="Enter Your Age", height=2, font=("Arial", 20))
lable.pack()  # put the lable on the window

age = StringVar()  # creat age variable to store user's age
age.set("00")  # set age default value to "00"

# creat input feild
# let user to enter age
age_input = Entry(root, width=2, font=("Arial", 30), textvariable=age)
age_input.pack()  # put the input feild on the window

# a function to make every thing when press on the button


def calc():
    # age variables
    age_in_years = age.get()
    months_age = int(age_in_years) * 12
    weeks_age = months_age * 4
    days_age = int(age_in_years) * 365

    first_unit = f"Your Age In Months: {months_age} Months."
    second_unit = f"Your Age In Weeks: {weeks_age} Weeks."
    third_unit = f"Your Age In Days: {days_age} Days."

    units_list = [first_unit, second_unit, third_unit]

    messagebox.showinfo("Your Age In Units.", "\n".join(units_list))


# creat button to calculate when press
button = Button(root, width=10, height=2, text="Calculate",
                bg="yellow", fg="red", borderwidth=0, command=calc)
button.pack()  # put the button on the window

# main loop to keep the program play
root.mainloop()
