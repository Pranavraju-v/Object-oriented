class india:
    def capital(self):
        print("The capital of india is dehli")
    def language(self):
        print("Hindi is wiedly spoken in india")
    def type(self):
        print("India is a devolpoing country")
class Germany:
    def capital(self):
        print("Berlin is the capital of germany")
    def language(self):
        print("German is widly spoken in germany")
    def type(self):
        print("Germany is a devolped country")
obj_india=india()
obj_germany=Germany()
for x in(obj_india, obj_germany):
    x.capital()
    x.language()
    x.type()
