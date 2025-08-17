import random


dates = {
    1:["Tomorrow You will die","You will be an Goverment Officer","You will have CGPA of 9"],
    2:["You may live 100 for Years","Your wife will be an doctor","You may have heart attack in 24 hours"],
    3:["You will die within 24 hours","Your girlfriend will be loyal to you","You will be doing good in future"],
    4:["You will become homeless in Future","You will get lottery in Future","Your wife be an Sundar-Sushil ladki"],
    5:["Balak You need to focus on study","Keep eyes on your Girlfriend"]
}

#IT JUST ACCEPTS THE BIRTHDATES TILL 5 , IT IS MADE FOR JUST FUN

print("HI MY NAME IS BABA TILLU AND I PREDICT THE FUTURE AND GIVES ADVICE FOR FUTURE")


running = True
while running:
    birth_date = int(input("Enter birthdate :"))
    client_name = input("Enter Your Name Balak :").lower()

    if client_name == "exit":
         running = False
    
    elif birth_date:
       tillu_baba_reply = random.choice(dates[birth_date])
       print(tillu_baba_reply)














