import pyinputplus as pyip
import random, time


number_of_questions = 10
correct_answers = 0

for question_num in range(number_of_questions):
    num_one = random.randint(0, 9)
    num_two = random.randint(0, 9)

    prompt = "#%s: %s x %s = " % (question_num, num_one, num_two)

    try:
        pyip.inputNum(
            prompt,
            allowRegexes=["^%s$" % (num_one * num_two)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=5,
            limit=3,
        )

    except pyip.TimeoutException:
        print("Too slow!")

    except pyip.RetryLimitException:
        print("Out of tries!")

    else:
        print("Correct!")
        correct_answers += 1

    time.sleep(1)


print(f"Score: {correct_answers} / {number_of_questions}")
