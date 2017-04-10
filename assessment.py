"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

# TODO: this always returns True
def is_hometown(town_name):
    """Determines if town given is my hometown of smithtown

    >>> is_hometown("smithtown")
    True

    >>> is_hometown("durian")
    False

    """

    if 'Smithtown' in town_name.title(): # compensate for input capatialization
        return True
    else:
        return False


def name_smusher(first_name, last_name):
    """Takes a first and last name and concatenatates them into one string

    >>> name_smusher('Natasha', 'Mitchko')
    'Natasha Mitchko'

    """
    return first_name.title() + " " + last_name.title()


def greeting(first_name, last_name, town_name):
    """Prints a greeting containing information about the users name and hometown"""
    name = name_smusher(first_name, last_name)
    if is_hometown:
        print "Hello {}, we're from the same place!".format(name)
    else:
        print "Hello {}, I'd like to visit {}!".format(name, town_name.title())


###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if 'berry' in fruit:
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    berry_truthiness = is_berry(fruit)
    if berry_truthiness == True:
        return 0
    else:
        return 5

# The problem with this is that it also changes the original list
# Except maybe it doesn't? Perhaps once the list is passed to the function a new
# instance of it is created for use only in the function's scope?
# Get help on this one
def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    lst.append(num)
    new_list = lst
    return new_list


def calculate_price(base_price, state, tax=(.05)):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    # Calculate tax
    # 1 plus tax so the total will be the price plus the tax at the given rate
    price_after_tax = base_price * (1 + tax)

    # Add fees based on state
    if state == 'CA':
        price_after_fees = price_after_tax * 1.03
    elif state == 'PA':
        price_after_fees = price_after_tax + 2
    elif state == 'MA' and base_price < 100:
        price_after_fees = price_after_tax + 1
    elif state == 'MA' and base_price > 100:
        price_after_fees = price_after_tax + 3
    else:
        price_after_fees = price_after_tax # i.e. no fees

    # return value that includes tax and fees
    return price_after_fees


    


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

#  .reduce()

# From the internet it looks like passing a function *args stores them as a tuple
# I think that because the .extend() method iterates over the argument passed to it
# it doesn't matter that we don't pass it a list as long as we pass it something iterable
# Check if this is right ^^^^
def append_multiple_to_list(lst, *items):
    """Takes list and n number of items to append to list

    >>> append_multiple_to_list([1,2,3], 4, 5, 6, 7, 8,)
    [1, 2, 3, 4, 5, 6, 7, 8]

    """
    lst.extend(items)
    return lst

def multiply_string(string):
    """Replicates input string three times

    >>> multiply_string('Cat')
    'CatCatCat'
    """
    return string * 3

def sandwhich(string):
    """Takes input and sandwhiches it between itself

   >>> sandwhich("Balloonicorn")
   ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """
    output = (string, multiply_string(string))
    return output



###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
