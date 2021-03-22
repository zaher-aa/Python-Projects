import sqlite3

# db = sqlite3.connect("skills.db")
# cr = db.cursor()
# cr.execute("CREATE TABLE IF NOT EXISTS `skills`(`ID` INTEGER, `Name` TEXT, `Age` INTEGER, `Skills` TEXT)")
# persons = ["zaher", "mahmoud", "ibrahim", "sham", "khalil", "osama", "ali"]
# ids = [n + 1 for n in range(len(persons))]
# ages = [18, 18, 18, 13, 20, 25, 30, 45]
# skills = ['None'] * len(persons)
# all_data = [(ids[i], persons[i].title(), ages[i], skills[i].title()) for i in range(len(persons))]
# cr.executemany("INSERT INTO skills Values(?, ?, ?, ?)", all_data)
# db.commit()
# db.close()
db = sqlite3.connect("skills.db")
cr = db.cursor()


# colors class
class MyColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# a function for sending success massages when an event is done
def success_message(updates, closed):
    if updates:
        print(f"{MyColors.WARNING}\nNew Updates Addet To The Database.")
    if closed:
        print(f"{MyColors.WARNING}Database Successfully Closed.")


# a function for showing users data either all of them or a specific user
def show_data():
    message = """
for showing all data ==> 1
for showing data for specific user ==> 2
> """
    type_of_show = input(message).strip()
    cr.execute("Select * From skills")
    all_data = cr.fetchall()
    if type_of_show == '1':
        for row in all_data:
            print(
                f"{MyColors.BOLD}{MyColors.OKBLUE}\nUser_ID: {row[0]}\nName: '{row[1]}'\nAge: {row[2]}\nSkills: '{row[3]}'\n")
    elif type_of_show == '2':
        user_id = int(input("ID: ").strip())
        for row in all_data:
            if row[0] == user_id:
                print(
                    f"{MyColors.BOLD}{MyColors.OKBLUE}\nUser_ID: {row[0]}\nName: '{row[1]}'\nAge: {row[2]}\nSkills: '{row[3]}'")
    db.commit()


# a function for manipulating users data
def edditing_data():
    event = input(
        "\nEdit Data ==> 1\nDelete Skills ==> 2\nDelete User ==> 3\n> ").strip()
    if event != '2':
        user_id = int(input(">ID: ").strip())
    # first case
    if event == '1':
        event_type = input(
            "\nEdit user_name ==> 1\nEdit Age ==> 2\nUpdate skills ==> 3\n> ").strip()
        # first subcase
        if event_type == '1':
            data = input("New User Name: ").strip().title()
            cr.execute(
                "Update skills set Name = ? Where ID = ?", (data, user_id))
            success_message(updates=True, closed=False)
        # second subcase
        if event_type == '2':
            data = int(input("New Age: ").strip())
            cr.execute("Update skills set Age = ? Where ID = ?",
                       (data, user_id))
            success_message(updates=True, closed=False)
        # third subcase
        if event_type == '3':
            type_of_update = input(
                "\nInsert a New Skill ==> 1\nDelete Previous Skills and Add New One/s ==> 2\n> ").strip()
            # first child subcase
            if type_of_update == '1':
                data = input("\nInsert a New Skill: ").strip().title()
                cr.execute(
                    "SELECT Skills FROM skills where ID = ?", (user_id,))
                previous_skills = cr.fetchone()[0]
                # first child child subcase
                if previous_skills != 'None':
                    final_data = previous_skills + " " + data
                    cr.execute(
                        f"UPDATE skills SET Skills = ? Where ID = ?", (final_data, user_id))
                # second child child subcase
                else:
                    cr.execute(
                        "Update skills set Skills = ? Where ID = ?", (data, user_id))
                success_message(updates=True, closed=False)
            # second child subcase
            elif type_of_update == '2':
                data = input("\nUpdate Your Skills: ").strip().title()
                cr.execute(
                    "Update skills set Skills = ? Where ID = ?", (data, user_id))
                success_message(updates=True, closed=False)
    # second case
    if event == '2':
        event_type = input(
            "\nDelete All Users Skills ==> 1\nDelete Specific User Skills ==> 2\n> ")
        # first subcase
        if event_type == '1':
            cr.execute("Update skills set Skills = ?", ("None",))
            success_message(updates=True, closed=False)
        # first subcase
        elif event_type == '2':
            user_id = int(input(">ID: ").strip())
            cr.execute(
                "Update skills set Skills = ? Where ID = ?", ("None", user_id))
            success_message(updates=True, closed=False)
    # third case
    if event == '3':
        cr.execute("Delete From skills Where ID = ?", (user_id,))
        print(f"User With ID = {user_id} Is Deleted")
    db.commit()


# a function for adding new users and give them their ID
def add_new_user():
    cr.execute("SELECT * FROM skills")
    all_data = cr.fetchall()
    new_user_id = len(all_data) + 1
    name = input("\nName: ").strip().title()
    age = int(input("Age: ").strip())
    skills = input("Skills: ").strip().title()
    cr.execute(
        "INSERT INTO skills(ID, Name, Age, Skills) values(?, ?, ?, ?)", (new_user_id, name, age, skills))
    print(
        f"{MyColors.BOLD}{MyColors.OKBLUE}\nYour Information:-\nID: {new_user_id}\nName: {name}.\nAge: {age}\nSkills: {skills}.")
    success_message(updates=True, closed=False)
    db.commit()


if __name__ == '__main__':
    instructions = """
for adding new users ==> 'a'
for edditing users data ==> 'e'
for show data ==> 's'
> """
    try:
        event = input(instructions).strip().lower()
        if event == 'a':
            add_new_user()
        elif event == 'e':
            edditing_data()
        elif event == 's':
            show_data()
        else:
            print(
                f"{MyColors.FAIL}{MyColors.BOLD}Sorry '{event}' Is Not Recognized.")
    except sqlite3.Error:
        print(f"{MyColors.FAIL}{MyColors.BOLD}An Error Occuorred While Doing Some Tasks.")
    finally:
        if db:
            db.close()
            success_message(updates=False, closed=True)
