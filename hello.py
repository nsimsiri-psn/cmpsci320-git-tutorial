
class Greeter():
    def __init__(self, my_name):
        self.my_name = my_name;

    def greet(self, your_name):
        print "hello %s, from %s"%(self.my_name, your_name);

if __name__ == "__main__":
    obj = Greeter("Bob")
    obj.greet("Peter");

    obj = Greeter("A")
    obj.greet("B");
