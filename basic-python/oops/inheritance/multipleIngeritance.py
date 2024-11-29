# a Chile class can inherit from multiple parent classs
# Parent Class 1
class Father:
    def traits(self):
        return "Father's traits"

# Parent Class 2
class Mother:
    def qualities(self):
        return "Mother's qualities"

# Child Class
class Child(Father, Mother):
    def child_traits(self):
        return "Child's unique traits"

# Creating an object of the Child class
child = Child()
print(child.traits())       # Inherited from Father
print(child.qualities())    # Inherited from Mother
print(child.child_traits()) # Defined in Child
