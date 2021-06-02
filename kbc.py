from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):
    if question["answer"]==answer:
        return True
    else:
        return False


def lifeLine(ques):

    count = 0
    options = [1,2,3,4]
    ans = options.pop(ques["answer"]-1)
    print(options)
    return random.choice(options)
   


    
        
    
currentques=0
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    correctoptions ={"1","2","3","4","lifeline","quit"}
    lifelines=1
    while True:
        global currentques
        print(f'\tQuestion {currentques+1}: {QUESTIONS[currentques]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[currentques]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[currentques]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[currentques]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[currentques]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans.lower()=="quit":
            if currentques:
                print(f"Thanks for playing you have won till {QUESTIONS[currentques-1]['money']}")
                break
            else:
                print("Thanks for playing you have won till 0")
        if ans.lower() in correctoptions:
            if ans.lower()=="lifeline" and lifelines:
                lifelines-=1
                ques_opt = lifeLine(QUESTIONS[currentques])
                answer = QUESTIONS[currentques]["answer"]
                
                if ques_opt<QUESTIONS[currentques]["answer"]:
                    print(f'\tQuestion {currentques+1}: {QUESTIONS[currentques]["name"]}' )
                    print(f'\t\tOptions:')
                    print(f'\t\t\tOption {ques_opt}: {QUESTIONS[currentques]["option"+str(ques_opt)]}')
                    print(f'\t\t\tOption {answer}: {QUESTIONS[currentques]["option"+str(answer)]}')
                    ans=input()
                else:
                        print(f'\tQuestion {currentques+1}: {QUESTIONS[currentques]["name"]}' )
                        print(f'\t\tOptions:')
                        print(f'\t\t\tOption {answer}: {QUESTIONS[currentques]["option"+str(answer)]}')
                        print(f'\t\t\tOption {ques_opt}: {QUESTIONS[currentques]["option"+str(ques_opt)]}')
                        ans=input()
            elif ans.lower()=="lifeline" and lifelines<1:
                print("Lifeline already used!")
                continue
                

            if isAnswerCorrect(QUESTIONS[currentques], int(ans) ):
                
                print(f'You Won {QUESTIONS[currentques]["money"]} Rupees')
                print('\nCorrect !')
                currentques+=1
            else:
                
                print('\nIncorrect ! Game Over You Win:',end="")
                if currentques+1>5:
                    print("10000")
                elif currentques+1>11:
                    print("3,20,000")
                else:
                    print("0")
                break
            
        else:
            print("\tInvalid input ! enter an input from 1-4 or lifeline or quit")
    

kbc()
