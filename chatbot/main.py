import pyttsx3
import csv
import sys

engine = pyttsx3.init()
engine.setProperty("rate", 140)

class JarvisBot():

    def __init__(self, user_name):
        self.user_name = user_name
        self.ai_name = "Jarvis"
        self.responses = {}
        self.history = {}

        with open("data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                input_key = row["input"].lower().strip()
                response_value = f"{row['responses']}".replace("{user}", self.user_name).replace("{ai_name}", self.ai_name)
                self.responses[input_key] = response_value

    def check_input(self):
        running = True

        while running:
            user_input = input(f"{self.user_name} Speak: ").lower().strip()

            if user_input == "exit":
                off = "Jarvis is turned off"
                engine.say(off)
                engine.runAndWait()
                running = False
                continue

            for row in self.responses:
                if user_input in row or row in user_input:
                    reply = self.responses[row]
                    engine.say(reply)
                    engine.runAndWait()
                    print(reply)
                    
                    with open("history.csv", "a", newline="") as f:
                        fieldnames = ["user_name", "user_input", "jarvis_reply"]
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        if f.tell() == 0:
                            writer.writeheader()
                        writer.writerow({
                            "user_name": self.user_name,
                            "user_input": user_input,
                            "jarvis_reply": reply
                        })
                    break
                
            else:
                n = "Sorry I can't respond, I am not that much trained yet"
                engine.say(n)
                engine.runAndWait()

                learn = input(f"{self.ai_name}: Do you want to teach me? [Y/N]: ")

                if learn.upper().strip() == "Y":
                    your_response = input(f"{self.ai_name}: What should I respond to? ").lower().strip()
                    my_reply = input(f"{self.ai_name}: What should be my reply? ").lower().strip().replace("{user}", self.user_name)
                    engine.say(my_reply)
                    engine.runAndWait()

                    with open("data.csv", "a", newline="") as file:
                        append = csv.writer(file)
                        append.writerow([your_response, my_reply])
                        self.responses[your_response] = f"{self.ai_name}: {my_reply}"

                    thanks = f"{self.ai_name}: Thank you! I became smarter now."
                    engine.say(thanks)
                    engine.runAndWait()


                with open("history.csv", "a", newline="") as f:
                    fieldnames = ["user_name", "user_input", "jarvis_reply"]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    if f.tell() == 0:
                        writer.writeheader()
                    writer.writerow({
                        "user_name": self.user_name,
                        "user_input": user_input,
                        "jarvis_reply": "sorry i am not that much trained"
                    })


try:
    name = input("Please enter your name: ").strip()
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only alphabets!")
    name = name.replace(" ", "")
except ValueError as error:
    print(error)
    sys.exit()

d1 = JarvisBot(name)
d1.check_input()
