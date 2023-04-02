correct = 0
def correct(correct):
  if Answers_0 == 34:
    correct+=1
  if Answers_1 == 18:
    correct+=1
  if Answers_2 == -99:
    correct+=1
  if Answers_3 == 3.75:
    correct+=1
  if Answers_4 == 227:
    correct+=1
  if Answers_5 == 50:
    correct+=1
  if Answers_6 == 178:
    correct+=1
  if Answers_7 == 2.71:
    correct+=1
  if Answers_8 == 49:
    correct+=1
  if Answers_9 == -140:
    correct+=1

def percentage():
  if correct == 1:
    return(userName + "you got 10% correct")
  if correct == 2:
    return(userName + "you got 20% correct")
  if correct == 3:
    return(userName + "you got 30% correct")
  if correct == 4:
    return(userName + "you got 40% correct")
  if correct == 5:
    return(userName + "you got 50% correct")
  if correct == 6:
    return(userName + "you got 60% correct")
  if correct == 7:
    return(userName + "you got 70% correct")
  if correct == 8:
    return(userName + "you got 80% correct")
  if correct == 9:
    return(userName + "you got 90% correct")
  if correct == 10:
    return(userName + "you got 100% correct")


#Says welcome to this BEDMAS quiz
print("Welcome to this BEDMAS quiz.")
#Says do not use a calculator
print("Do not use a calculator")

#Asks for their name
userName = input("Name please ")

#Says lets get started with what ever their name is
print("Lets get started " + userName)

#Says what the math methods are 
print("/ = divide, * = multiply, - = subtract, + = add")

#Says here are the questions
print("Here are the questions")

current_Question = 0
#The question list
Question = ['4+5(2*3) = ','5-2+3*5 = ','2/2-1*100 = ','2+2-2*2/2(2*4) = ','15/3*5(2+3+4) = ','7*14/2+1 = ','2*2*2*22*1+2 = ','3+4-5*6/7 = ','10/1*3+5-7(9-11) = ','10-10*15 = ']

#Answers list
Answers = ['34','18','-99','3.75','227','50','178','2.71','49','-140']

#prints the questions to the screen
for x in Question:
  Answers_0 = input(Question[current_Question])
  current_Question+=1
  Answers_1 = input(Question[current_Question])
  current_Question+=1
  Answers_2 = input(Question[current_Question])
  current_Question+=1
  Answers_3 = input(Question[current_Question])
  current_Question+=1
  Answers_4 = input(Question[current_Question])
  current_Question+=1
  Answers_5 = input(Question[current_Question])
  current_Question+=1
  Answers_6 = input(Question[current_Question])
  current_Question+=1
  Answers_7 = input(Question[current_Question])
  current_Question+=1
  Answers_8 = input(Question[current_Question])
  current_Question+=1
  Answers_9 = input(Question[current_Question])
  current_Question+=1
  Peace = input("How do you think you did out of 10? ")

print(correct)
print(percentage)
