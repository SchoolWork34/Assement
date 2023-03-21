x = 0
#Says welcome to this BEDMAS quiz
print("Welcome to this BEDMAS quiz.")
def correct():
  if current_Question == Answers:
    return x +1
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
  #print(current_Question)
  #print (Question[current_Question])
