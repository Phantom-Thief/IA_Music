from pyo import *


#Accord de 3 notes
def Accord3Maj(a) :
     b=Sine(freq=[midiToHz(a),midiToHz(a+4),midiToHz(a+7)] , mul=1).out(0)
     return b

def Accord3Min(a) :
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+7)] , mul=1).out(0)
     return b

def Accord3Dim(a) :
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+6)] , mul=1).out(0)
     return b

def Accord3Aug(a) :
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+6)] , mul=1).out(0)
     return b

#Accord de 4 notes
#Accord de septième de dominante
def Accord4Dom(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+4),midiToHz(a+7),midiToHz(a+10)] ,mul=1).out(0)
     return b

#Accord de septième mineure
def Accord4Min(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+7),midiToHz(a+10)] ,mul=1).out(0)
     return b

#Accord de septième mineure et quinte diminuée
def Accord4MinDim(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+6),midiToHz(a+10)] ,mul=1).out(0)
     return b

#Accord de septième majeure
def Accord4Maj(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+4),midiToHz(a+7),midiToHz(a+11)] ,mul=1).out(0)
     return b

#Accord de septième diminuée
def Accord4Dim(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+6),midiToHz(a+9)] ,mul=1).out(0)
     return b

#Accord de septième diminuée
def Accord4MajMin(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+3),midiToHz(a+7),midiToHz(a+11)] ,mul=1).out(0)
     return b

#Accord de septième majeure et quinte augmentée
def Accord4MajAug(a):
     b=Sine(freq=[midiToHz(a),midiToHz(a+4),midiToHz(a+8),midiToHz(a+11)] ,mul=1).out(0)
     return b

#Accord 
