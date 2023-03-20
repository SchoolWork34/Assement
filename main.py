print("Welcome to this maths quiz. We will be using BEDMAS.")

userName = input("Name please ")

print("Lets get started " + userName)

print("/ = divide, * = multiply, - = subtract, + = add")

#Question and AnswerOptions list
Question = ('1 = 4+5(2*3)')

AnswerOptions = input('1 = 30, 40, 34, 38 ')

Question = ('2 = 5-2+3*5')

AnswerOptions = input('2 = 20, 18, 15, 22 ')

Question = ('3 = 2/2-1*100')

AnswerOptions = input('3 = -99, -80, -100, -98 ')

Question = ('4 = 2+2-2*2/2(2*4)')

AnswerOptions = input('4 = 3.50, 3.80, 3.60, 3.75 ')

Question = ('5 = 15/3*5(2+3+4)')

AnswerOptions = input('5 = 220, 224, 227, 230 ')

Question = ('6 = 7*14/2+1')

AnswerOptions = input('6 = 40, 50, 60, 51 ')

Question = ('7 = 2*2*2*22*1+2')

AnswerOptions = input('7 = 180, 170, 178, 190 ')

Question = ('8 = 3+4-5*6/7')

AnswerOptions = input('8 = 2.50, 2.80, 2.65, 2.71 ')

Question = ('9 = 10/1*3+5-7(9-11)')

AnswerOptions = input('9 = 48, 49, 50, 51 ')

Question = ('10 = 10-10*15')

AnswerOptions = input('10 = -130, -140, -150, -145 ')


for x in AnswerOptions:      
  print(x)

print("Let's see how many you got correct")

#Answers list
Answers = ['''1 = 34''', '''2 = 18''', '''3 = -99''', '''4 = 3.75''', '''5 = 227''', '''6 = 50''', '''7 = 178''', '''8 = 2.71''', '''9 = 49''', '''10 = -140''']

#Loops through the answers list 
for x in Answers:
  print(x)