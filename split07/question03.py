class MotorCycle: 
  
    """Class for MotorCycle"""
  
    def __init__(self): 
        self.name = 'MotorCycle'
  
    def TwoWheeler(self): 
        return 'TwoWheeler'
  
  
class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = 'Truck'


    def EightWheeler(self):
        return 'EightWheeler'
 

class Car:
    """Class for Car"""

    def __init__(self):
        self.name = 'Car'
    

    def FourWheeler(self):
        return 'FourWheeler'
    
  
class Adapter: 
    """ 
    Adapts an object by replacing methods. 
    Usage: 
    motorCycle = MotorCycle() 
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler) 
    """
  
    def __init__(self, obj, **adapted_methods): 
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.adapted_methods = adapted_methods

    
    @property
    def name(self):
        return self.obj.name


    @property
    def wheels(self):
        return self.adapted_methods['wheels']
        
  
    def original_dict(self): 
        """Print original object dict"""
        print(self.adapted_methods)


class Target:
    def request():
        pass


 	

objects = []
motorCycle = MotorCycle()
objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))
truck = Truck()
objects.append(Adapter(truck, wheels = truck.EightWheeler))
car = Car()
objects.append(Adapter(car, wheels = car.FourWheeler))
for obj in objects:
    print(f"A {obj.name} is a {obj.wheels()} vehicle")