print('Hello! Welcome to my Quiz Game!')

playing= input("Do you wish to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! Let's play:) ")
score=0

answer = input("What is the full form of CPU? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer=="power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print(f'You got {score} point{"s" if score != 1 else ""}!')
print(f'You got {(score/4)*100} %.')
