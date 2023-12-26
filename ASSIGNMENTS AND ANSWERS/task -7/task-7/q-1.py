class Vetri :
    name =""

    def look(self):
        print("good boy")

class Boy(Vetri):
    def look(self):
        super().look()
        print("i am very good boy")
a=Boy()
a.look()
