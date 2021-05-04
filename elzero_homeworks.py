# import random

# choices = ["r", "p", "s"]
# allowed_attempts = 3
# current_attempt = 0
# user_score = 0
# computer_score = 0
# message = """
# this is rock, paper and scissors game
# you will be playing with the computer
# you got 3 tries then the winner will be announced
# good luck :)
# """

# print(message.title())
# while current_attempt < allowed_attempts:
#     user_input = input("You: ").lower()
#     computer_input = random.choice(choices)
#     print(f"Computer: {computer_input}\n")
#     current_attempt += 1
#     if (user_input == "r" and computer_input == "s") or (user_input == "p" and computer_input == "r") or (user_input == "s" and computer_input == "p"):
#         user_score += 1
#     elif user_input == computer_input:
#         user_score += 1
#         computer_score += 1
#     else:
#         computer_score += 1
#     print(
#         f"Your Score: {user_score} || Computer Score: {computer_score} || Attempts Left: {allowed_attempts - current_attempt}")

# if user_score > computer_score:
#     print("\nYou Won!")
# elif user_score == computer_score:
#     print("\nEquality!")
# else:
#     print("\nYou Lost!")
