# My attempt at the 2024 advent of code

## interesting stuff ive learned or reviewed so far:

###### (markdown syntax tips: https://www.markdownguide.org/basic-syntax/)

### problem 4:

you can use numpy to help count diagonal char sequences via np.diag

the docs for that can be found here: https://numpy.org/doc/stable/reference/generated/numpy.diag.html

### problem 5:
defaultdict from collections is useful if you want to create a dictionary with items where the default value is an empty list. To do that, you can do the following

    from collections import defaultdict
    example_dict = defaultdict(list)

useful for when you want to associate multiple elements with a specific unique value. In this case it was ordering information for a specific page

### problem 6:
eumerate is useful if you want to also use the index while iterating through a list of elements. Just remember that the first element when initializing the for loop is the index number

    for i, element in enumerate(a_list):
        print(i, element)

### problem 7
generating a product for a char sequence

refer to this page: https://stackoverflow.com/questions/30672738/python-how-to-generate-permutations-of-size-greater-than-the-number-of-list-el

I was having issues with generating what I thought were permutations for the operation sequences needed to check if the equations between the numbers were valid

for example, the operators given in part 1 were: '*' and '+'

if there was a number sequence like: 1 2 3

the operators and numbers needed to check would be the following

1+2+3
1\*2+3
1+2\*3
1\*2\*3

so I needed to check ['++', '*+', '+\*', '\*\*'], but needed to figure a way to generate that somehow. I could do that with the product function in itertools like so:

    from itertools import product
    list(product(['*','+'], repeat=len(v)-1))

product actually returns a generator since the number of items returned can be quite large. So it's unnecessary to convert the generator into a list, unless you really want to see its contents.

### problem 8
generating permutations using itertools permutations

for checking each pair of antenna of a specific type. Recall for this problem, two antenna of the same type means that they have the same character representing the antenna

example AA, 00, aa, etc...

getting the coordinates of all of a specific type of antenna, I need to check each pair of the same type of antenna and get the antinode location.

For that to happen, I need to check all possible pairs, and find a way to generate all those pairs, so the permutations function served that purpose exactly

    from itertools import permutations
    antenna_pair_permutations = permutations(antenna_locations[antenna_type], 2)

where antenna_locations is a defaultdict with lists as its values. So, the permutations function takes in a list, and generates all permutations for elements of that list containing 2 elements.

### problem 9
nothing new :/

### problem 10

had to review how to perform a breadth first search for traversing and finding the hiking trails in the problem ending with 9

used the pseudocode found at the wikipedia page to help: https://en.wikipedia.org/wiki/Breadth-first_search

also had to remember how to use a deque and set in python

sets only allow for immutable objects, so instead of adding lists to them, I had to add tuples

You can initailize a tuple just doing the following

    a_tuple = (1, 2)

a deque is a double-ended queue. Use it for queueing operations

    from collections import deque

    a_deque = deque()
    a_deque.append(1)
    a_deque.popleft() # to dequeue an element!



