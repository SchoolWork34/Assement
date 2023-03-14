#Welcomes the user
print("Welcome to this maths quiz. We will be using BEDMAS.")

#Asks for their name
userName = input("Name please ")

#Says lets get started with what ever their name is
print("Lets get started " + userName)

#Says what the math methods are 
print("/ = divide, * = multiply, - = subtract, + = add")

#The question list
Question = ['''1 = 4+5(2*3)''', '''2 = 5-2+3*5''', '''3 = 2/2-1*100''', '''4 = 2+2-2*2/2(2*4)''', '''5 = 15/3*5(2+3+4)''', '''6 = 7*14/2+1''', '''7 = 2*2*2*22*1+2''', '''8 = 3+4-5*6/7''', '''9 = 10/1*3+5-7(9-11)''', '''10 = 10-10*15''']

#prints the questions to the screen
for x in Question:
  print(x)

print("Let's see how many you got correct")

#Answers list
Answers = ['''1 = 34''', '''2 = 18''', '''3 = -99''', '''4 = 3.75''', '''5 = 227''', '''6 = 50''', '''7 = 178''', '''8 = 2.71''', '''9 = 49''', '''10 = -140''']

#Loops through the answers list 
for x in Answers:
  print(x)