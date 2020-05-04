from experta import *

class MedicalExpert(KnowledgeEngine):
    @DefFacts()
    def _initial_action_(self):
        print("Hi. I am an Expert System who can help you in medical diagnosis. So, please answer the following questions to find out the disease and the cure")
        print("Please enter the number against any symptom which you are experiencing?")
        print("1. Fever")
        print("2. Cough")
        print("3. Runny Nose")
        print("4. Headache")
        yield Fact(action="start")
        yield Fact(symptoms="none")
        
    @Rule(Fact(action="start"),NOT(Fact(name=W())))
    def askNameGender(self):
        self.declare(name=input("What's your name?"))
        self.declare(gender=input("what's your gender?(m/f)"))
        self.declare(type=input("Is your reason physical or mental"))

if __name__ == "__main__":
    engine=MedicalExpert()
    engine.reset()
    engine.run()
