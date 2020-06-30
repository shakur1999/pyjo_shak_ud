class Sample():
	def __init__(self, param1, param2):
		self.param1 = param1
		self.param2 = param2

	def Some_Method(self):
		# perform this action
		print(self.param1)

#===============================================

class Dog():
    # class object attributes
    # same for any instance of a class
    species = "mamal"

    def __init__(self, breed, name, spots):
        # assign aruguments to attributes via
        # self attribute
        self.breed = breed 
        self.name = name
        self.spots = spots # expecting a boolead in return

#===============================================

class Circle():
    # class object attribute
    pi = 3.14

    def __init__(self, raduis=1):
        self.raduis = raduis
        self.area = raduis*raduis*Circle.pi

    # class methods
    def get_circumference(self):
        return self.raduis * Circle.pi * 2

    my_circle = Circle() #deligate Circle attr to my_circle
    my_circle.raduis
    my_circle.get_circumference() 