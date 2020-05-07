#!/usr/bin/env python

from experta import *

### Helper functions ###

def multi_input(input_str, options=[]): # returns a list of user selected values
    print(input_str)
    choice = None
    options.append("none")
    while choice is None:
        print("0) none")
        for i in range(len(options)-1):
            print(f"{i+1}) {options[i]}")
        print("Your choice: ", end='')
        try:
            choice = [ int(x)-1 for x in input().split() ]
            for x in choice:
                if x >= len(options):
                    raise ValueError("Invalid value")
                if x == -1 and len(choice)>1:
                    raise ValueError("Can't have none and other values")
        except Exception as e:
            print("Invalid value encountered. Try again")
            choice = None
    return [ options[i] for i in choice ]

def yes_no(input_str):
    input_str += " (yes/no): "
    ans = None
    while ans is None:
        ans = input(input_str).lower()
        if ans == "y" or ans == "yes" or ans == "yup":
            return "yes"
        elif ans == "n" or ans == "no" or ans == "nope":
            return "no"
        else: ans = None

def suggest_disease(disease, symptoms):
    print(f"You might be suffering from {disease}")
    symptoms = ', '.join(symptoms)
    print(f"These symptoms lead to this conclusion: {symptoms}")
    exit(0)


class MedicalExpert(KnowledgeEngine):

    @DefFacts()
    def _initial_action_(self):
        print("Hi. I am an Expert System who can help you in medical diagnosis.")
        print("When prompted with options, enter space seperated integer values corresponding to all the options which apply to you.")
        print("Please answer the following questions to find out the disease and its cure")
        # yeild all the facts you require here
        yield Fact(action="engine_start")
        
    @Rule(Fact(action="engine_start"))
    def getUserInfo(self):
        self.declare(Fact(name=input("What's your name? : ")))
        self.declare(Fact(gender=input("what's your gender?(m/f) : ")))
        # self.declare(Fact(type=input("Is your reason physical or mental : ")))
        self.declare(Fact(action="questionnaire"))
    
    @Rule(Fact(action="questionnaire"))
    def askBasicQuestions(self):
        # ask if user suffers from eye problems
        self.declare(Fact(red_eyes=yes_no("Do you suffer from red eyes? (yes/no): ")))
        # ask if user suffers from any bodily pain
        pains = multi_input("Do you suffer from any pains?", ["abdomen pain", "back pain", "chest pain", "muscle pain", "joint pain", "body pain"])
        if pains[0] != "none":
            self.declare(Fact(pain="yes"))
            for pain in pains:
                self.declare(Fact(pain))
        # ask some other basic questions
        self.declare(Fact(fever=yes_no("Do you suffer from fever?")))
        self.declare(Fact(cough=yes_no("Do you suffer from cough?")))
        self.declare(Fact(chills=yes_no("Do you suffer from chills?")))
        self.declare(Fact(short_breath=yes_no("Do you suffer from shortness of breath?")))
        self.declare(Fact(sore_throat=yes_no("Do you have a sore throat or throat inflamation?")))
        self.declare(Fact(swelling=yes_no("Do you suffer from swelling?")))
        self.declare(Fact(fatigue=yes_no("Do you suffer from fatigue?")))
        self.declare(Fact(headache=yes_no("Do you suffer from headache?")))
    
    @Rule(Fact(red_eyes="yes"))
    def askEyeStatus(self):
        self.declare(Fact(eye_burn=yes_no("Do you have a burning sensation in eyes?")))
        self.declare(Fact(eye_crusting=yes_no("Do you get pus or crusting on eyes?")))
        self.declare(Fact(eye_irritation=yes_no("Do you have eye irritation?")))
    
    @Rule(OR(Fact(eye_crusting="yes"), Fact(eye_burn="yes")), salience=1000)
    def disease_Conjunctivitis(self):
        suggest_disease("Conjunctivitis", ["Burning sensation in eyes", "Crusting of eyes", "Redness in eyes"])

    @Rule(Fact(eye_irritation="yes"), salience=900)
    def disease_EyeAllergy(self):
        suggest_disease("Eye Allergy", ["Irritation in eyes", "Redness in eyes"])


if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print("The symptoms did not match with any of diseases in my database.")