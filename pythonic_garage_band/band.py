#from _typeshed import Self


class Band:
    instances = []
    
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return Musician.play_solo(self)

    @classmethod
    def to_list(cls):
        return cls.instances
    

# *************************************************
class Musician:
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The band {self.name}"
    
    def __repr__(self):
        return f"Band instance. name={self.name}"

    def play_solo(self):
        return f"Play"
    

# *************************************************
class Guitarist(Musician):
  
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return f"guitar"

    def play_solo(self) :
        return f"face melting guitar solo"


# *************************************************
class Bassist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return f"bass"
    
    def play_solo(self) :
        return f"bom bom buh bom"

# *************************************************
class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
      
    def get_instrument(self):
        return f"drums"
    
    def play_solo(self) :
        return f"rattle boom crash"


# *************************************************
if __name__ == "__main__":
    Joan = Guitarist("Joan Jett")
    print(Joan.name)