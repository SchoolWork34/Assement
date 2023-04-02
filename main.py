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

#The question list
Questions = {
  "4+5(2*3):"['1: 34': '2: 35': '3: 36'],
  "5-2+3*5:"['1: 17': '2: 18': '3: 19'],
  "2/2-1*100:"['1: 97': '2: 98': '3: 99'],
  "2+2(2*4):"['1: 18': '2: 19': '3: 20'],
  "15/3*5(2+3+4):"['1: 226': '2: 227': '3: 228'],
  "7*14/2+1:"['1: 49': '2: 50': '3: 51'],
  "2*2*2*22*1+2:"['1: 176': '2: 177': '3: 178'],
  "3+4-5*6:"['1: 22': '2: 23': '3: 24'],
  "10/1*3+5-7(9-11):"['1: 48': '2: 49': '3: 50'],
  "10-10*15:"['1: 140': '2: 141': '3: 142']
}

score = 0  
for question_number,question in enumerate(Questions):
    print ("Question",question_number+1) 
    print (question)
    for options in Questions[question][:-1]: 
        print (options)
    user_choice = input("Make your choice : ")
    if user_choice == Questions[question][-1]: 
        score += 1 

def percentage(z):
  if score == 1:
    return(userName + "you got 10% correct")
  if score == 2:
    return(userName + "you got 20% correct")
  if score == 3:
    return(userName + "you got 30% correct")
  if score == 4:
    return(userName + "you got 40% correct")
  if score == 5:
    return(userName + "you got 50% correct")
  if score == 6:
    return(userName + "you got 60% correct")
  if score == 7:
    return(userName + "you got 70% correct")
  if score == 8:
    return(userName + "you got 80% correct")
  if score == 9:
    return(userName + "you got 90% correct")
  if score == 10:
    return(userName + "you got 100% correct")

print(percentage)
