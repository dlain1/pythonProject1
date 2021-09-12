# Functions to check if answer has yes or no in it
yesValues = ["y", "yes", "true", "t"]
noValues = ["n", "no", "false", "f"]
def yes(val):
    return val.lower() in yesValues
def no(val):
    return val.lower() in noValues
# ------------------------------------

# Main function that ask questions and gives the chance to choose user's question they wanna answer
if __name__ == "__main__":
    correctAnswerCounter = 0
    questions = """ 
            (1) Are encoding and encryption the same? - Yes/No
            (2) Is it possible to decrypt a message without a key? - Yes/No
            (3) Is it possible to decode a message without a key? - Yes/No
            (4) Is a hashed message supposed to be un-hashed? - Yes/No
            (5) What is the MD5 hashing value to the following message: 'NYU Computer Networking'- Use MD5 hash generator and use the answer in your code
            (6) Is MD5 a secured hashing algorithm? - Yes/No
            (7) What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number
            (8) What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number
            """
    print(questions)
    # While loop that working until user got 8 correct answer
    while correctAnswerCounter != 8:
        selected_question = int(input("Please select the question you want to answer: "))

        # Question 1 
        if selected_question == 1:
            answer = input("Answer to question 1: ")
            if no(answer): 
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 2
        if selected_question == 2:
            answer = input("Answer to question 2: ")
            if no(answer): 
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 3
        if selected_question == 3:
            answer = input("Answer to question 3: ")
            if yes(answer):
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 4
        if selected_question == 4:
            answer = input("Answer to question 4: ")
            if no(answer):
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 5
        if selected_question == 5:
            answer = input("Answer to question 5: ")
            if answer == "42b76fe51778764973077a5a94056724":
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 6
        if selected_question == 6:
            answer = input("Answer to question 6: ")
            if no(answer):
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 7
        if selected_question == 7:
            answer = int(input("Answer to question 7: "))
            if answer == 4:
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")

        # Question 8
        if selected_question == 8:
            answer = int(input("Answer to question 8: "))
            if answer == 3:
                correctAnswerCounter += 1
                print(questions)
                print("Correct!\nYou got {} correct answers now.".format(correctAnswerCounter))
            else:
                print(questions)
                print("\nWrong Answer")
    # The end of while loop means user got 8 correct answer
    # For now program can't check if user trying to answer one question correct twice, so user can answer just one question for 8 times and end the while loop
    # I could do a check for that using true/false variables for each question but its making a lot of spaghetti code that is not proffesional
    # so im gonna just leave it like that until i find a solution for that.
    print("\nWell done, you got all answers right!\n")
    input("Press anything to end the program...")