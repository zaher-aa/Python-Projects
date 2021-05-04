# Download_Videos_From_Youtube = """from pytube import YouTube

# link = input("Enter URL Please: ")
# video = YouTube(link)

# def completed():
#     print("download completed")

# video.streams.get_highest_resolution().download(output_path="C:/desktop", filename="الحمار زين")
# video.register_on_complete_callback(completed())"""

# Download_PlayLists_From_Youtube = """from pytube import Playlist


# link = input("Enter Playlist Link: ")
# playlist = Playlist(link)

# def completed():
#     print("download completed")

# for video in playlist.videos:
#     video.streams.get_highest_resolution().download(output_path="C:/desktop")
# video.register_on_complete_callback(completed())
# """

class Employee:
    def __init__(self, name, salary_nis, no_of_children):
        self.__name = name.title()
        self.__salary_nis = salary_nis
        self.__no_of_children = no_of_children

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary_nis(self):
        return self.__salary_nis

    def set_salary_nis(self, salary):
        self.__salary_nis = salary

    def get_no_of_children(self):
        return self.__no_of_children

    def set_no_of_children(self, number_of_children):
        self.__no_of_children = number_of_children

    def get_salary_dollar(self):
        return self.__salary_nis / 3.5

    def get_tax(self):
        if self.get_no_of_children() == 1 or self.get_no_of_children() == 2:
            tax = self.get_salary_dollar() * 0.1
        elif self.get_no_of_children() == 3 or self.get_no_of_children() == 4:
            tax = self.get_salary_dollar() * 0.05
        else:
            tax = self.get_salary_dollar() * 0.025
        return tax

    def get_net_pay_dollar(self):
        net_pay = self.get_salary_dollar() - self.get_tax()
        return net_pay

    def get_net_pay_nis(self):
        net_pay = self.get_salary_nis() - (self.get_tax() * 3.5)
        return net_pay

    @staticmethod
    def get_childern_avg(emp_list):
        childern_num_sum = 0
        for employee in emp_list:
            childern_num_sum += employee.get_no_of_children()
        children_num_avg = childern_num_sum / len(emp_list)
        return children_num_avg

    @staticmethod
    def get_salary_avg_dollar(emp_list):
        sum_salary_in_dollar = 0
        for employee in emp_list:
            sum_salary_in_dollar += employee.get_salary_dollar()
        salaries_avg = sum_salary_in_dollar / len(emp_list)
        return salaries_avg

    @staticmethod
    def get_salary_avg_nis(emp_list):
        return Employee.get_salary_avg_dollar(emp_list) * 3.5

    @staticmethod
    def get_maximum_salary_and_his_owner_dollar(emp_list):
        emp_dict = {}
        for employee in emp_list:
            emp_dict[employee.get_salary_dollar()] = employee.get_name()
        return f"Maximum Salary Is: ${max(emp_dict):0.2f}, And His Owner Is: {emp_dict[max(emp_dict)]}"

    @staticmethod
    def get_maximum_salary_and_his_owner_nis(emp_list):
        emp_dict = {}
        for employee in emp_list:
            emp_dict[employee.get_salary_dollar()] = employee.get_name()
        return f"Maximum Salary Is: {(max(emp_dict) * 3.5):0.2f} Shekels, And His Owner Is: {emp_dict[max(emp_dict)]}"


emp_list = [
    Employee("zaher", 2000, 3),
    Employee("ali", 3456, 5),
    Employee("khalil", 3214, 3),
    Employee("mahmoud", 900, 2),
    Employee("ibrahim", 345, 1),
    Employee("osama", 748.54, 5),
    Employee("osman", 356, 6),
    Employee("abd el raouf", 3000, 7),
    Employee("hamada", 4000, 5),
    Employee("salman", 25000, 1),
    Employee("Abd Elrahman", 50000, 6)
]

print(Employee.get_salary_avg_dollar(emp_list))
print(Employee.get_salary_avg_nis(emp_list))
print(Employee.get_maximum_salary_and_his_owner_dollar(emp_list))
print(Employee.get_childern_avg(emp_list))
