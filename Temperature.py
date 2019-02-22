# Temperature Converter

class Temperature:
    
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def getCelsius(self):
        return self.celsius

    def getFahrenheit(self):
        return self.fahrenheit
        
    def convertCelsius(self): #convert to f
        self.convertCel = (self.celsius * (9/5)) + 32
        return self.convertCel

    def convertFahrenheit(self): #convert to c
        self.convertFahr = (self.fahrenheit - 32) * (5/9)
        return self.convertFahr

class Interface:

    def __init__(self,celsius, fahrenheit):
        self.temp = Temperature(celsius, fahrenheit)
        #self.degree = degree if degree is not None else

   # def degreeOfTemp(self):
    #    self.degree = float(input("""Whats the degree of temperature you'd like to convert?: """))
     #   return self.degree
    
    def selectUnits(self):
        
        #d = degreeOfTemp()
        x = input("""What temperature scale are you converting, Celsius or Fahrenheit?: """)
        while x not in ("F","f","Fahrenheit","fahrenheit","C","c","Celsius","celsius"):
            print("Temperature scale was not found. Try again!")
        if x in ("F","f","Fahrenheit","fahrenheit"):
            print("Fahrenheit converts to",round(self.temp.convertFahrenheit(),1),"Celsius.")
        else:
            print("Celsius converts to", round(self.temp.convertCelsius(),1),"Fahrenheit.")
            
def main():

    print("""This program will help convert temperate from celsius to
fahrenheit and vice versa.\n""")
    x = float(input("""Whats the degree of temperature you'd like to convert?: """))
    #y = float(input("""Whats the degree of temperature you'd like to convert for F?: """))
    t = Temperature(x,x) #not needed in terms of converting but assigned object to class
    i = Interface(x,x)  #needs two parameters but since user will choose degree and scale to convert,
                        #   it will not make a difference
    iprint = i.selectUnits()
    print(x, iprint)
    
    
    

main()
