# class Question:

#     def __init__(self, prompt, answer, number):
#         self.prompt = prompt
#         self.answer = answer
#         self.number = number


# temporary_list_for_questions = [
#     'how old is zaher:-\na) 18\nb) 17\nc) 20\n> ',
#     'what is the name of zaher\'s mother:-\na) Rahma\nb) Reema\nc) Somaya\n> ',
#     'how many brothers and sisters does zaher has:-\na) 5\nb) 7\nc) 3\n> ',
#     'what is zaher\'s favorate sport:-\na) Swimming\nb) Horse Riding\nc) Fitnnes\n> '
# ]

# # this is equivelant to the commented part down there
# questions_list = [
#     f"{counter + 1}- {question.split(':-')[0].title()}:-{question.split(':-')[1]}"
#     for counter, question in zip(range(len(temporary_list_for_questions)), temporary_list_for_questions)
# ]

# # for question, counter in zip(temporary_list_for_questions, range(len(temporary_list_for_questions))):
# #     current_complete_question = question.split(":-")
# #     current_question = str(counter + 1) + "- " + current_complete_question[0].title() + ":-" + current_complete_question[1]
# #     questions_list.append(current_question)

# questions_numbers_list = [number + 1 for number in list(range(len(questions_list)))]

# questions_objects = [
#     Question(questions_list[0], "a", questions_numbers_list[0]),
#     Question(questions_list[1], "b", questions_numbers_list[1]),
#     Question(questions_list[2], "c", questions_numbers_list[2]),
#     Question(questions_list[3], "b", questions_numbers_list[3])
# ]


# def run_test():
#     wrong_answers = []
#     score = 0
#     for question in questions_objects:
#         answer = input("\n" + question.prompt).lower()
#         if answer == question.answer:
#             score += 1
#         else:
#             wrong_answers.append(f"Correct Answer For 'Q{question.number}' ==> '{question.answer}'")
#     print(f"You Got {score}/{len(questions_objects)} Correct.")
#     if len(wrong_answers) != 0:
#         print("\nWrong Answers:-")
#         for wrong_answer in wrong_answers:
#             print(wrong_answer)


run_test()


my_list = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]
for li in my_list:
    for number in li:
        print(number, end=' ')
    print()
