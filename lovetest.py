print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#LOWERCASE INPUT
person1 = name1.lower()
person2 = name2.lower()

#TRUE LETTERS COUNT
person1.count('t')
person1.count('r')
person1.count('u')
person1.count('e')

person2.count('t')
person2.count('r')
person2.count('u')
person2.count('e')

#LOVE LETTERS COUNT
person1.count('l')
person1.count('o')
person1.count('v')
person1.count('e')

person2.count('l')
person2.count('o')
person2.count('v')
person2.count('e')

#LOVE SCORE FIRST NUMBER
num1 = person1.count('t')+person1.count('r')+person1.count('u')+person1.count('e')+person2.count('t')+person2.count('r')+person2.count('u')+person2.count('e')

#LOVE SCORE SECOND NUMBER 
num2 = person1.count('l')+person1.count('o')+person1.count('v')+person1.count('e')+person2.count('l')+person2.count('o')+person2.count('v')+person2.count('e')

#LOVE SCORE
num3 = str(f"{num1}{num2}")
love_score = int(num3)


#LOVE ANALYSIS
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

#OUTPUT TEST SECTION
