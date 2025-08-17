import random
import os
import time as t

print("Test Your typing Speed...")

#Basically it Says if the os is windows then cls else clear
os.system('cls' if os.name == 'nt' else 'clear')

l1 = []
splited = []


#When we take words from txt file it also comes with space 
with open("Words.txt") as f:
    for i in f:
        i1 = i.strip("\n").strip()
        l1.append(i1)

options = random.sample(l1,5)
print(options)

s = t.time()
user_input = input("Here Type the each word By giving space :")
st = t.time()
time_taken  = st-s

length = len(user_input.split())
wpm = length/time_taken*60

print("Your WPM is :",int(wpm))


#For Accurancy
Correct_words = 0
user_entered = user_input.split()


len1 = len(options)
len2 = len(user_entered)


for i in range(len2):
    if user_entered[i]==options[i]:
        Correct_words = Correct_words+1

# print(Correct_words)

accuracy  = Correct_words/len1*100
print("Your Accuracy Was :",accuracy)

 





    



    

