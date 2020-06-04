from pyo import *

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