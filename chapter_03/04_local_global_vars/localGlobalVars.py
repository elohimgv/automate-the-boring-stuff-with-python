# This cause an error because eggs is a local variable
# and it only exists in the local scope of spam()
# Local Variables Cannot Be Used in the Global Scope
"""def spam():
    chickens = 31337
spam()
print(chickens) """

# Local Scopes Cannot Use Variables in Other Local Scopes
"""def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()"""

# Global Variables Can Be Read from a Local Scope
"""def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)"""

# Local and Global Variables with the Same Name
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'
