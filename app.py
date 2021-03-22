form_1 = """import requests
    from bs4 import BeautifulSoup

    url = input("Enter URL: ")
    search_word = input("Enter Search Word: ")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='SearchResults')
    job_emps = results.find_all('section', class_='card-content')
    a_s = results.find_all('a')
    count = 0
    for job_emp, a in zip(job_emps, a_s):
        if job_emp.find('h2', class_='title', string=lambda text: search_word in text.lower()):
            title = job_emp.find('h2', class_='title')
            company = job_emp.find('div', class_='company')
            location = job_emp.find('div', class_='location')
            link = a['href']
            if None in (title, company, location):
                continue
            print("Title: " + title.text.strip())
            print("Company: " + company.text.strip())
            print("Location: " + location.text.strip())
            print("Apply Here: " + link)
            print("\n")
            count += 1
    print(f"{count} Results Founded")"""

form_2 = """import requests
    from bs4 import BeautifulSoup
    import csv

    url = 'https://www.monster.com/jobs/search/?q=Arabic-Transcription'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='SearchResults')
    job_emps = results.find_all('section', class_='card-content')
    a_s = results.find_all('a')
    f = open("jobs.csv", "w")
    field_names = ["Title", "Company", "Location", "Time", "Link"]
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for job_emp, a in zip(job_emps, a_s):
        title = job_emp.find('h2', class_='title')
        company = job_emp.find('div', class_='company')
        location = job_emp.find('div', class_='location')
        time = job_emp.find('time', datetime=any)
        link = a['href']
        if None in (title, company, location, time, link):
            continue
        writer.writerow({"Title": title.text.strip(), "Company": company.text.strip(
        ), "Location": location.text.strip(), "Time": time.text.strip(), "Link": link})
        # print(f"title: {title.text.strip()}")
        # print(f"company: {company.text.strip()}")
        # print(f"location: {location.text.strip()}")
        # print(f"time: {time.text.strip()}")
        # print(f"link: {link}")
        # print("\n")
    f.close()"""

vowel_checker = """
    def vowel_check():
        with open("file.txt", "r") as file:
            all_lines_no_edit = file.readlines()
            all_lines_with_edit = []
            for line in all_lines_no_edit:
                if line[-1] == "\n":
                    line = line[:-1]
                all_lines_with_edit.append(line)
            final_text = " ".join(all_lines_with_edit)
        print(f"Your Text: {final_text}")
        splitted_text = final_text.split(" ")
        words_count = 0
        palendrom_count = 0
        palendrom_list = []
        chars_dict = {}
        for word in splitted_text:
            for char in word.lower():
                if char in "aeiouAEIOU":
                    if char in chars_dict:
                        chars_dict[char] += 1
                    else:
                        chars_dict[char] = 1
            for char in word.lower():
                if char in "aeiouAEIOU":
                    words_count += 1
                    break
            if word.lower() == word[::-1].lower():
                palendrom_count += 1
                palendrom_list.append(word)
        print(
            f"Number Of Palendrom Words: {palendrom_count} ==> {palendrom_list if len(palendrom_list) != 0 else None}")
        print(f"Number Of Words Containing Vowels: {words_count}")
        print(f"All Vowels With Their Presence:-")
        for key, value in chars_dict.items():
            print(f"{key} ==> {value}")


    vowel_check()
"""


class Student:
    def __init__(self, name, age, collage, gpa):
        self.__name = name.title()
        self.__age = age
        self.__collage = collage.title()
        self.__gpa = gpa

    def __repr__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nCollage: {self.__collage}\nGPA: {self.__gpa}"


students_objects_list = []
length = int(input("How Many Students Are There: "))
for i in range(length):
    name = input("Name: ")
    age = int(input("Age: "))
    collage = input("Collage: ")
    gpa = float(input("GPA: "))
    print()
    student = Student(name, age, collage, gpa)
    students_objects_list.append(student)

for student in students_objects_list:
    print(f"{student}\n")
