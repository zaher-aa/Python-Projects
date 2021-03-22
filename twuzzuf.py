import requests
import csv
import json
from bs4 import BeautifulSoup


def get_all_jobs(base_url, search_word):
    # open csv file in writting mode
    csv_file = open("jobs.csv", "w")
    field_names = ["Job Title", "Company", "Time", "Job Responsibilities", "Location", "Salary", "Skills", "Apply Here"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    # open json file
    json_file = open("jobs.json", "w")
    page_num = 0
    base_url += "&start="
    # instanchaite two lists
    salaries, responsablities = [], []
    # while loop to see all the pages related to our search in the website
    while True:
        # connect to the supplied link (base link)
        # number = len(str(page_num))
        url = base_url + str(page_num)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        # getting needed information
        all_jobs = soup.find_all('h2', {'class': 'css-m604qf'})
        all_links = soup.find_all('a', {'class': 'css-nn640c', 'rel': 'noreferrer'})
        all_locations = soup.find_all('span', {'class': 'css-5wys0k'})
        all_companies = soup.find_all('a', {'class': 'css-17s97q8'})
        all_skills = soup.find_all('div', {'class': 'css-y4udm8'})
        all_times = soup.find_all('div', {"class": ["css-4c4ojb", "css-do6t5g"]})
        # instanchaite lists
        job_titles, jobs_links, jobs_locations, companies, skills, times, data = [], [], [], [], [], [], {}
        # for loop to get needed information from the above elements
        for job, location, link, company, skill, time in zip(all_jobs, all_locations, all_links, all_companies, all_skills, all_times):
            # filter data that contain the word Search Word
            if search_word in job.text.lower():
                # adding needed info to the above lists
                job_titles.append(job.text.strip())
                # we can use link['href'] or link.attrs['href'] (both are same)
                jobs_links.append(link['href'])
                jobs_locations.append(location.text.strip())
                companies.append(company.text.strip())
                skills.append(skill.text.strip())
                times.append(time.text.strip())
                # getting Salaries and Job Responsablities
                # connect to sub pages (child pages)
                sub_page = requests.get(link['href'])
                sub_page_soup = BeautifulSoup(sub_page.content, 'lxml')
                # Salary
                salary = sub_page_soup.find('div', {'class': 'matching-requirement-icon-container'})
                salaries.append(salary.text.strip())
                # Job Responsablities
                responsablity = sub_page_soup.find('span', {'itemprop': 'responsibilities'}).find('ul').find_all("li")
                li_temporary_str = '' 
                for li in responsablity:
                    li_temporary_str += li.text.strip() + ' | '
                li_temporary_str = li_temporary_str[:-2]
                responsablities.append(li_temporary_str)
        # filter all list so that it contains at least one element
        if len(job_titles) != 0:
            # writing information to csv file
            for job, link, location, company, skill, time, salary, responsablity, counter in zip(job_titles, jobs_links, jobs_locations, companies, skills, times, salaries, responsablities, range(len(responsablities))):
                # writing data to csv file
                writer.writerow({"Job Title": job, "Company": company, "Location": location, "Job Responsibilities": responsablity,
                                "Skills": skill, "Apply Here": link, "Time": time, "Salary": salary})
                # data for json file
                data[f"Job {counter + 1}"] = {"Job Title": job, "Company": company, "Location": location, "Job Responsibilities": responsablity,
                                                "Skills": skill, "Apply Here": link, "Time": time, "Salary": salary}
        # writing data to json file
        json.dump(data, json_file)
        page_limit = int(soup.find('strong').text.strip())
        print("----" + str(page_num) + "----")
        if page_num > page_limit // 15:
            print("Process Ended.")
            break
        page_num += 1
        url = base_url
    csv_file.close()  # close csv file
    json_file.close()  # close json file


base_url = input("Enter URL (Link): ")
search_word = input("Search Word: ").lower()
get_all_jobs(base_url, search_word)
