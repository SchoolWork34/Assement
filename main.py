#Welcomes the user
print("Welcome to this maths quiz. We will be using BEDMAS.")

print("DO NOT USE A CALCULATOR")

#Asks for their name
userName = input("Name please ")

#Says lets get started with what ever their name is
print("Lets get started " + userName)

#Says what the math methods are 
print("/ = divide, * = multiply, - = subtract, + = add")

print("Here are the questions")

#The question list
Question = ['''1 = 4+5(2*3)''', '''2 = 5-2+3*5''', '''3 = 2/2-1*100''', '''4 = 2+2-2*2/2(2*4)''', '''5 = 15/3*5(2+3+4)''', '''6 = 7*14/2+1''', '''7 = 2*2*2*22*1+2''', '''8 = 3+4-5*6/7''', '''9 = 10/1*3+5-7(9-11)''', '''10 = 10-10*15''']

#prints the questions to the screen
for x in Question:
  print(x)

print("Choose out of the four options")

#Answeroption list
AnswerOptions1 = input('1 = 30, 40, 34, 38? ')
print(AnswerOptions1)

AnswerOptions2 = input('2 = 20, 18, 15, 22? ')
print(AnswerOptions2)

AnswerOptions3 = input('3 = -99, -80, -100, -98? ')
print(AnswerOptions3)

AnswerOptions4 = input('4 = 3.50, 3.80, 3.60, 3.75? ')
print(AnswerOptions4)

AnswerOptions5 = input('5 = 220, 224, 227, 230? ')
print(AnswerOptions5)

AnswerOptions6 = input('6 = 40, 50, 60, 51? ')
print(AnswerOptions6)

AnswerOptions7 = input('7 = 180, 170, 178, 190? ')
print(AnswerOptions7)

AnswerOptions8 = input('8 = 2.50, 2.80, 2.65, 2.71? ')
print(AnswerOptions8)

AnswerOptions9 = input('9 = 48, 49, 50, 51? ')
print(AnswerOptions9)

AnswerOptions10 = input('10 = -130, -140, -150, -145? ')
print(AnswerOptions10)

print("Let's see how many you got correct")

#Answers list
Answers = ['''1 = 34''', '''2 = 18''', '''3 = -99''', '''4 = 3.75''', '''5 = 227''', '''6 = 50''', '''7 = 178''', '''8 = 2.71''', '''9 = 49''', '''10 = -140''']

#Loops through the answers list 
for x in Answers:
  print(x)

def answer_check():
  if AnswerOptions1 == 34
  if AnswerOptions2 == 18
  if AnswerOptions3 == -99
  if AnswerOptions4 == 3.75
  if AnswerOptions5 == 227
  if AnswerOptions6 == 50
  if AnswerOptions7 == 178
  if AnswerOptions8 == 2.71
  if AnswerOptions9 == 49
  if AnswerOptions10 == -140
