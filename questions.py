#inorder to use a clasee of MCQ.
from MCQ import Questions

question_prompt=[
    "What is the color of an apple?\n(a) Red/Green\n(b) Purple\n(c) Black \n\n",
    "What is the color of the sky?\n(a) Pink\n(b) Blue\n(c) Green \n\n",
    "What is the color of an orange?\n(a) Red/Green\n(b) Purple\n(c) orange \n\n",
    "What is the color of an grape?\n(a) Red/Green\n(b) Purple\n(c) white \n\n",
]

questions = [
    Questions (question_prompt[0],"a"),
    Questions (question_prompt[1],"b"),
    Questions (question_prompt[2],"c"),
    Questions (question_prompt[3],"a")
]




def run_test(questions):
    # To store the score.
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if(answer == i.answer):
            score += 1
    return score

print("You got",str(run_test(questions)) + "/4 correct.")
