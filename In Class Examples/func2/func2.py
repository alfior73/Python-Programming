"""
mpenta
in class
functions 2
User define function/custom functin
"""
"""
function pattern
def functionName ({parameter list}):
    statements to run
    return {value}
"""

def printGreeting():
    print("hello")
    print("how are you?")
    return

def customGreeting(name):
    print(f"hello {name}") #fstring python
    print("hello" + name)
    print("how are you?")
    return

def customGreeting2(name, salutation):
    print(f"{salutation} {name}")
    print("how are you?")
    return 

def main():
    print("what is your name")
    name = input()
    customGreeting2("hey")
    customGreeting("jose")
    
    
main()
