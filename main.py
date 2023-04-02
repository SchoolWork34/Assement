correct = 0
def CorrectTest(correct):
  if Answers_0 == Answers:
    correct + 1

def PercentageTest(correct):
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
 

print(CorrectTest(correct))

print(PercentageTest(correct))