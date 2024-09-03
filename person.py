class Person():
    #metodo que se llama cuando se crea el objeto
    def __init__(self,name, lastname):
        self.name = name
        self.lastname = lastname
romi = Person("romina","godoy")
print(romi.name, romi.lastname)
bob = Person("bob","esponja")
print(bob.name, bob.lastname)
patricio = Person("patricio","estrella")
print(patricio.name, patricio.lastname)
