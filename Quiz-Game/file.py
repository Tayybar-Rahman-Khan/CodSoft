import random

# Quiz questions and answers
quiz_questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Berlin", "D. Rome", "A"],
    "Which planet is known as the Red Planet?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn", "B"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion", "B"],
    "What is the powerhouse of the cell?": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Cytoplasm", "B"]
}

def display_question(question, choices):
    print(question)
    for choice in choices:
        print(choice)

def take_user_input():
    return input("Enter your choice: ").upper()

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def display_result(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def play_quiz():
    score = 0
    total_questions = len(quiz_questions)
    questions = list(quiz_questions.keys())

    random.shuffle(questions)

    for question in questions:
        display_question(question, quiz_questions[question][:-1])
        user_answer = take_user_input()
        is_correct = evaluate_answer(user_answer, quiz_questions[question][-1])

        display_result(is_correct, quiz_questions[question][-1])

        if is_correct:
            score += 1

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You got all the questions correct!")
    elif score >= total_questions / 2:
        print("Well done! You passed the quiz.")
    else:
        print("Better luck next time. Keep practicing!")

def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    while True:
        play_quiz()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
