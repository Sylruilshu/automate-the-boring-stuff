import pyinputplus as pyip, random, time


number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = "#%s: %s x %s = " % (question_number, num1, num2)
    # prompt = f"#{question_number}: {num1} x {num2} = "

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(
            prompt,
            allowRegexes=["^%s$" % (num1 * num2)],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )

    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")

    else:
        # This block runs if no exceptions were raised in the try block.
        print("Correct!")
        correct_answers += 1

    time.sleep(1)  # Brief pause to let user see the result.

print("Score: %s / %s" % (correct_answers, number_of_questions))
