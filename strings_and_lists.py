#find and replace
def find_and_replace():
    words = "It's thanksgiving day. It's my birthday, too!"
    find = words.find(day)
    replace = words.replace('day', 'month')
    return (find, replace)
find_and_replace()
#min and max
def min_and_max(my_list):
    min(my_list)
    max(my_list)
    return (min, max)
min_and_max([2,3,5])
# first and last 
def first_and_last(list):
    new_list = [list[0], list[len(my_list)-1]]
    return new_list
first_and_last([5,23, "Hellp", 2, "World"])
# new list
#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
#Sort your list first. Then, split your list in half. Push the list created from 
#the first half to position 0 of the list created from the second half. 
#The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
def new_list():
    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x.sort()
    half = len(x)/2
    first_half = x[:half]
    second_half = x[half:]
    a = 0
    new_list = [a] + second_half
    new_list[0] = first_half
    return new_list
new_list()
