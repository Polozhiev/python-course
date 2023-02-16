class MyComplex:
    def __init__(self, Re, Im):
        self.Im=Im
        self.Re=Re
    
    def sum(self, other):
        return MyComplex(self.Re+other.Re, self.Im+other.Im)

    def minus(self, other):
        return MyComplex(self.Re-other.Re, self.Im-other.Im)

    def __eq__(self, other):
        return self.Re==other.Re and self.Im==other.Im 

    def mult(self, other):
        return MyComplex(self.Re*other.Re-self.Im*other.Im, self.Re*other.Im+self.Im*other.Re)

    def abs(self):
        return (self.Re * self.Re + self.Im * self.Im)**0.5