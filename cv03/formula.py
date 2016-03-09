class Formula(object):
    def __init__ (self,subformulas=[]):
        self.subformulas = subformulas
       
    def subf(self):
        return self.subformulas
 
    def toString(self):
        return ''
 
    def __str__(self):
        return self.toString()
 
    def eval(self, interpretation):
        return False
 
class Variable(Formula):
    def __init__ (self,name):
        self._name = name
        Formula.__init__(self)
 
    def name(self):
        return self._name
    
    def toString(self):
        return self.name()
 
    def __repr__(self):
        return "<Variable '{}'> ".format(self.name())
 
    def eval(self,i):
        return i[self.name()]  

class Negation(Formula):
    def __init__(self,subformula):
        Formula.__init__(self,[subformula])
 
    def originalFormula(self):
         return self.subf()[0]
  
    def toString(self):
         return "-" + self.originalFormula().toString()
 
    def eval(self,i):
        return not self.originalFormula().eval(i)
     
class Disjunction(Formula):
    def __init__(self,subformulas):
        Formula.__init__(self,subformulas)
 
    def toString(self):
        return "(" + "|".join([f.toString()for f in self.subf()]) + ")"
 
    def eval(self,i):
        for f in self.subf():
            if not f.eval(i):
                return False
        return True
       
class Conjunction(Formula):
    def __init__(self,subformulas):
        Formula.__init__(self,subformulas)
 
    def toString(self):
        return "(" + "&".join([f.toString()for f in self.subf()]) + ")"
 
    def eval(self,i):
        return False not in [f.eval(i) for f in self.subf()]
   
class BinayFormula(Formula):
    def __init__(self,leftSide, rightSide):
         Formula.__init__(self,[leftSide, rightSide])
   
    def leftSide(self):
        return self.subf()[0]
 
    def rightSide(self):
        return self.subf()[1]

class Implication(BinayFormula):
    def toString(self):
        return "(" + self.leftSide().toString() + "=>" + self.rightSide().toString() + ")"
 
    def eval(self,i):
        satLeft = self.leftSide().eval(i)
        satRight = self.rightSide().eval(i)
        if satLeft and not satRight:
            return False
        else:
            return True
   
class Equivalence(BinayFormula):
    
    def toString(self):
        return "(" + self.leftSide().toString() + "<=>" + self.rightSide().toString() + ")"
 
    def eval(self,i):
        satLeft = self.leftSide().eval(i)
        satRight = self.rightSide().eval(i)
        return satLeft == satRight
