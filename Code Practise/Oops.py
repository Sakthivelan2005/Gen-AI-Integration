class c1:
    def a(self):
        print("hello")

#Constructor
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def display(self):
        print("c: ",self.b, " D: ", self.c)

#Constructor Overloading
    def addition(self,*args):
       print(type(args))

    def greet(self, name="Guest"):
        print("Welcome!, ", name)

obj = c1(10,"Pom")
obj.a()
obj.display()
obj.addition(1,2,3,4)
obj.greet("7679mlk")