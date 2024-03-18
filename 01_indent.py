number = 5  # initialization of variable

"""
if (number > 6            # comment 1
        and number > 8    # comment 2
        or number < 3):   # comment 3
    pass
"""


class MyClass:
    """ Dosctring for a class
    something
    something
    """
    pass


def add_numbers(a, b):
    """ My docstring """
    return a + b


a = 5
print(add_numbers(b=2, a=3))

# we don't compare Boolean values to True and False
is_prime = True

if is_prime:  # nepoužíváme is_prime == True
    print("Is prime")

if not is_prime:  # nepoužíváme is_prime == False
    print("Is not prime")

my_string = ""  # False
my_string2 = "a"  # True


def my_function(name):
    """Purpose of the function.

    Description of parameters (optional)

    Return Values (optional)

    Preconditions (optional)

    Side effects (optional)

    Additional information (further explanations, bibliography references, examples of use) (optional)
    """
    pass


print(my_function.__doc__)
