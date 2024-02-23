mixte = "Mixte"
upper_body = "Upper Body"
lower_body = "Lower Body"
full_body = "Full Body"

STRUCTURE = {
"EMOM" : {
    "6" : {
        full_body : [[upper_body, lower_body],
                     [lower_body, upper_body]]
    }
}
}

class Wod():
    def __init__(self):
        self.time = None
        self.difficulty = None
        self.part = None
        self.type = None
    def initialisation(self):
        self.structure = STRUCTURE[self.type][self.time][self.part]
    
    